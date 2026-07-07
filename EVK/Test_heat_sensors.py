"""
Routine script for thermal tests on Scintil EVK modules.
Testing all sensors and verifying safety cutoffs at 50°C (Interposer) and 60°C (Heatsink).
Check if TEC object can maintain 30°C under laser load and sweep currents from 125mA to 200mA.

Author: Pierre Cassagnettes
"""

import os
import sys
import time
import csv
import traceback
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

# ==============================================================================
# SCINTIL API & COMPONENTS IMPORTATION
# ==============================================================================
try:
    from ScintilAPI import (
        ScintilHAL,
        scintil_hal_module_t,
        scintil_hal_laser_t,
        scintil_hal_temp_t,
        scintil_hal_error_bit_t
    )
except ImportError:
    try:
        from ScintilAPI import (
            ScintilHAL,
            scintil_hal_module_t,
            scintil_hal_laser_t,
            scintil_hal_temp_type_t as scintil_hal_temp_t,
            scintil_hal_error_bit_t
        )
    except ImportError:
        print(" [ERROR] Unable to load the Scintil API.")
        print("Verify that 'ScintilAPI.py' is present in the same directory.")
        print("-" * 60)
        traceback.print_exc()
        print("-" * 60)
        input("\nPress Enter to close...")
        sys.exit(1)

# ==============================================================================
# APPLIED ABSTRACTION FUNCTION
# ==============================================================================
def get_api_function_return_value(api: ScintilHAL, function_name: str, return_attribute: str, *args):
    """
    Safely executes a Scintil API function,
    checks the error code, and extracts the requested attribute.
    """
    func = getattr(api, function_name, None)
    if not func:
        print(f" [ERROR] Function '{function_name}' not found in the API.")
        return None
    try:
        ret = func(*args)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            print(f" [API ERROR] {function_name} returned error code: {ret['errcode']}")
            return None
        return ret[return_attribute]
    except Exception as e:
        print(f" [API EXCEPTION] Failed to call {function_name}: {e}")
        return None

# ==============================================================================
# DEFAULT HARDWARE CONFIGURATION
# ==============================================================================
IP_HAL = "127.0.0.1"
PORT_HAL = 80

MODULES_SELECTIONNES = []
CAPTEURS_ACTIFS = []

# ==============================================================================
# GRAPHICAL CONTEXT (Limited to sensors processed in the code)
# ==============================================================================
def configurer_test_thermique_gui():
    """
    Displays the full graphical interface to configure the bench:
    1. Selection of the save folder.
    2. Choice of Scintil modules to sequence.
    3. Individual activation of the processed thermal sensors.
    4. Selection of tests (1, 2A, 2B, 3) to execute with descriptions.
    """
    root = tk.Tk()
    root.title("Thermal Routine Configuration - Scintil")
    root.geometry("620x720")  # Height increased to accommodate tests without scrolling
    root.attributes("-topmost", True)
    root.resizable(False, False)
    root.configure(bg="#F5F5F7")

    resultat = {
        "dossier": "",
        "modules": [],
        "capteurs_actifs": [],
        "tests_actifs": {}
    }

    tk.Label(
        root, text="THERMAL ROUTINE - BENCH CONFIGURATION",
        font=("Arial", 12, "bold"), bg="#F5F5F7", fg="#1D1D1F", pady=15
    ).pack()

    # --- 1. FOLDER SELECTION ---
    folder_frame = tk.LabelFrame(root, text=" Data Export Folder ", font=("Arial", 9, "bold"), bg="#F5F5F7", padx=10, pady=10)
    folder_frame.pack(fill="x", padx=20, pady=5)

    folder_path_var = tk.StringVar(value="No folder selected")
    tk.Label(folder_frame, textvariable=folder_path_var, font=("Arial", 9, "italic"), bg="#FFFFFF", fg="#8E8E93", anchor="w", relief="sunken", bd=1, width=48, padx=5, pady=3).pack(side="left", padx=(0, 10))

    def parcourir_dossier():
        dossier = filedialog.askdirectory(title="Select the results export folder")
        if dossier:
            resultat["dossier"] = dossier
            folder_path_var.set(dossier)
            verifier_validation()

    tk.Button(folder_frame, text="Browse...", command=parcourir_dossier, bg="#E5E5EA", font=("Arial", 9, "bold"), relief="flat", padx=10).pack(side="right")

    # --- 2. MODULE SELECTION ---
    modules_frame = tk.LabelFrame(root, text=" Scintil Modules to Test ", font=("Arial", 9, "bold"), bg="#F5F5F7", padx=10, pady=10)
    modules_frame.pack(fill="x", padx=20, pady=5)

    val_mod1 = tk.BooleanVar(value=True)
    val_mod2 = tk.BooleanVar(value=False)

    def on_module_toggle():
        actualiser_liste_capteurs()
        verifier_validation()

    tk.Checkbutton(modules_frame, text="Module 1", variable=val_mod1, command=on_module_toggle, font=("Arial", 10, "bold"), bg="#F5F5F7").pack(side="left", padx=30)
    tk.Checkbutton(modules_frame, text="Module 2", variable=val_mod2, command=on_module_toggle, font=("Arial", 10, "bold"), bg="#F5F5F7").pack(side="left", padx=30)
    
    def verifier_validation():
        un_module_actif = val_mod1.get() or val_mod2.get()
        dossier_rempli = bool(resultat["dossier"])
        capteurs_coches = [k for k, v in sensor_variables.items() if v.get()]
        un_capteur_actif = len(capteurs_coches) > 0
        un_test_actif = any(v.get() for v in test_variables.values())

        # The button activates only if everything is consistent
        if un_module_actif and dossier_rempli and un_capteur_actif and un_test_actif:
            btn_start.config(state="normal", bg="#4CAF50")
        else:
            btn_start.config(state="disabled", bg="#A8A8A8")
            
    # --- 3. THERMAL SENSOR SELECTION ---
    sensors_frame = tk.LabelFrame(root, text=" Active Thermal Sensors ", font=("Arial", 9, "bold"), bg="#F5F5F7", padx=10, pady=10)
    sensors_frame.pack(fill="x", padx=20, pady=5)

    grid_container = tk.Frame(sensors_frame, bg="#F5F5F7")
    grid_container.pack(fill="both", expand=True)

    sensor_checkbox_widgets = []
    sensor_variables = {}

    def actualiser_liste_capteurs():
        for widget in sensor_checkbox_widgets:
            widget.destroy()
        sensor_checkbox_widgets.clear()

        # Strict list of sensors managed by lire_toutes_temperatures()
        available_sensors = [("Mainboard", True)]

        if val_mod1.get():
            available_sensors.extend([
                ("PIC Mod0", False),
                ("Interposer Mod1", True),
                ("TEC 1 Object Temp", True),
                ("TEC 1 Sink Temp", True),
            ])

        if val_mod2.get():
            available_sensors.extend([
                ("PIC Mod1", False),
                ("Interposer Mod2", True),
                ("TEC 2 Object Temp", True),
                ("TEC 2 Sink Temp", True),
            ])

        for idx, (sensor_name, is_default_checked) in enumerate(available_sensors):
            if sensor_name not in sensor_variables:
                sensor_variables[sensor_name] = tk.BooleanVar(value=is_default_checked)
            var = sensor_variables[sensor_name]

            row = idx // 2
            col = idx % 2

            cb = tk.Checkbutton(grid_container, text=sensor_name, variable=var, font=("Arial", 9), bg="#F5F5F7", command=verifier_validation)
            cb.grid(row=row, column=col, sticky="w", padx=10, pady=2)
            sensor_checkbox_widgets.append(cb)

    # --- 4. TEST SELECTION ---
    tests_frame = tk.LabelFrame(root, text=" Selection of Tests to Execute ", font=("Arial", 9, "bold"), bg="#F5F5F7", padx=10, pady=10)
    tests_frame.pack(fill="x", padx=20, pady=5)

    liste_tests = [
        ("Test 1", "Verification of initial homogeneity"),
        ("Test 2A", "Interposer Safety (Automatic cutoff at 50°C)"),
        ("Test 2B", "TEC Heatsink Safety (Automatic cutoff at 60°C)"),
        ("Test 3", "Active regulation (30°C) & Current sweep (0-200mA)")
    ]
    test_variables = {}
    for t_id, desc in liste_tests:
        var = tk.BooleanVar(value=True)
        test_variables[t_id] = var
        tk.Checkbutton(
            tests_frame, text=f"{t_id} : {desc}", variable=var, 
            font=("Arial", 9), bg="#F5F5F7", anchor="w", command=verifier_validation
        ).pack(fill="x", padx=10, pady=2)

    # --- VALIDATION AND SAVING LOGIC ---
    def valider():
        # Saving modules
        resultat["modules"] = []
        if val_mod1.get(): resultat["modules"].append(0)
        if val_mod2.get(): resultat["modules"].append(1)
        
        # Filtering and saving checked sensors
        actuels = []
        if sensor_variables.get("Mainboard") and sensor_variables["Mainboard"].get():
            actuels.append("Mainboard")
        
        if val_mod1.get():
            for s in ["PIC Mod0", "Interposer Mod1", "TEC 1 Object Temp", "TEC 1 Sink Temp"]:
                if sensor_variables.get(s) and sensor_variables[s].get(): actuels.append(s)
                    
        if val_mod2.get():
            for s in ["PIC Mod1", "Interposer Mod2", "TEC 2 Object Temp", "TEC 2 Sink Temp"]:
                if sensor_variables.get(s) and sensor_variables[s].get(): actuels.append(s)

        resultat["capteurs_actifs"] = actuels
        
        # Saving test states (Dictionary of booleans)
        resultat["tests_actifs"] = {k: v.get() for k, v in test_variables.items()}
        
        root.quit()
        root.destroy()

    btn_start = tk.Button(root, text="Launch test routine", command=valider, font=("Arial", 11, "bold"), bg="#A8A8A8", fg="white", state="disabled", relief="flat", pady=10)
    btn_start.pack(fill="x", padx=20, pady=15)

    # Grid initialization at startup
    actualiser_liste_capteurs()
    root.mainloop()
    
    return resultat["dossier"], resultat["modules"], resultat["capteurs_actifs"], resultat["tests_actifs"]

# ==============================================================================
# READING OF ALL REAL TEMPERATURES
# ==============================================================================
def lire_toutes_temperatures(hal, modules_utilises):
    temps = {}
    try:
        mb_temp = get_api_function_return_value(hal, "scintil_hal_temperature_get_val", "temperature", scintil_hal_temp_t.SCINTIL_HAL_TEMPERATURE_MAINBOARD)
        if mb_temp is not None:
            temps["Mainboard"] = mb_temp

        for mod_idx in modules_utilises:
            module_obj = scintil_hal_module_t(mod_idx)
            mod_num = mod_idx + 1

            inter_temp = get_api_function_return_value(hal, "scintil_hal_temperature_module_get_val", "temperature", module_obj)
            if inter_temp is not None:
                temps[f"Interposer Mod{mod_num}"] = inter_temp

            obj_temp = get_api_function_return_value(hal, "scintil_hal_tec_get_object_temp", "temperature", module_obj)
            if obj_temp is not None:
                temps[f"TEC {mod_num} Object Temp"] = obj_temp

            sink_temp = get_api_function_return_value(hal, "scintil_hal_tec_get_sink_temp", "temperature", module_obj)
            if sink_temp is not None:
                temps[f"TEC {mod_num} Sink Temp"] = sink_temp

            pic_enum = scintil_hal_temp_t.SCINTIL_HAL_TEMPERATURE_PIC_1 if mod_idx == 0 else scintil_hal_temp_t.SCINTIL_HAL_TEMPERATURE_PIC_2
            pic_temp = get_api_function_return_value(hal, "scintil_hal_temperature_get_val", "temperature", pic_enum)
            if pic_temp is not None:
                temps[f"PIC Mod{mod_idx}"] = pic_temp

        print("\n--- [LIVE THERMAL READING] ---")
        for k, v in temps.items():
            if k in CAPTEURS_ACTIFS:
                print(f"  [ACTIVE] {k:<25} : {v:.2f} °C")
        print("-" * 38)
        return temps

    except Exception as e:
        print(f" [EXCEPTION] System error during temperature acquisition: {e}")
        traceback.print_exc()
        return None

# ==============================================================================
# SECURE MODULE MANAGEMENT AND SAFETY CONTROLS
# ==============================================================================
def arreter_systeme_securite(hal, mod_idx=None):
    """Cuts off the 16 lasers of the specified module (or all modules if mod_idx is None)."""
    modules_a_eteindre = [mod_idx] if mod_idx is not None else [0, 1]
    print(f"\n [SAFETY] Forced shutdown of lasers on module(s): {modules_a_eteindre}...")
    hal.scintil_hal_sys_reset_top()
    for m in modules_a_eteindre:
        module_obj = scintil_hal_module_t(m)
        for l_idx in range(16):
            laser_obj = scintil_hal_laser_t(l_idx)
            try:
                hal.scintil_hal_laser_set_current(module_obj, laser_obj, 0.0)
                hal.scintil_hal_controller_mux_loop_stop(laser_obj)
                hal.scintil_hal_controller_laser_set_value(laser_obj, 0.0)
            except Exception:
                pass

def controler_ventilateur(hal, active: bool):
    try:
        if active:
            print(" -> Activating fan (scintil_hal_fan_start)")
            hal.scintil_hal_fan_start()
        else:
            print(" -> Deactivating fan (scintil_hal_fan_stop)")
            hal.scintil_hal_fan_stop()
    except Exception as e:
        print(f" [EXCEPTION] Fan command error: {e}")

def attendre_refroidissement(hal, modules_selectionnes, nom_capteur, seuil=40.0):
    """Activates the fan and blocks execution until the sensor drops below the threshold."""
    controler_ventilateur(hal, active=True)
    print(f" Waiting for cooling of '{nom_capteur}' (Target < {seuil}°C)...")
    while True:
        t = lire_toutes_temperatures(hal, modules_selectionnes)
        if t and t.get(nom_capteur, 99.0) < seuil:
            print(f" -> Stabilization validated: {nom_capteur} = {t.get(nom_capteur):.2f}°C")
            break
        time.sleep(2)

def verifier_auto_extinction_lasers(hal, mod_idx):
    """Returns True if the 16 lasers of the targeted module have dropped back to 0.0 mA."""
    lasers_eteints = 0
    module_obj = scintil_hal_module_t(mod_idx)
    for l_idx in range(16):
        laser_obj = scintil_hal_laser_t(l_idx)
        curr = get_api_function_return_value(hal, "scintil_hal_laser_get_applied_current", "current", module_obj, laser_obj)
        if curr == 0.0 or curr is None:
            lasers_eteints += 1
    return lasers_eteints == 16

# ==============================================================================
# MAIN RUN ROUTINE (GLOBAL LOOP PER MODULE)
# ==============================================================================
def executer_routine_tests():
    global CAPTEURS_ACTIFS, MODULES_SELECTIONNES
    print("=== THERMAL TEST BENCH INITIALIZATION ===")
    
    dossier_save, MODULES_SELECTIONNES, CAPTEURS_ACTIFS, TESTS_ACTIFS = configurer_test_thermique_gui() 
    if not dossier_save:
        print(" [CANCELLATION] No folder selected. End of script.")
        return
    
    try:
        print(f"Connecting to Scintil HAL API ({IP_HAL}:{PORT_HAL})...")
        hal = ScintilHAL(IP_HAL, PORT_HAL, strictcutversion=False)
        print(" Successfully connected to the hardware.\n")
    except Exception as e:
        print(f" [ERROR] Connection to HAL API failed: {e}")
        traceback.print_exc()
        return

    # Configuration and initial global reset
    bilan_global = {}  # Stores the status of each test per module
    hal.scintil_hal_sys_reset_top()
    arreter_systeme_securite(hal)

    # --------------------------------------------------------------------------
    # MAIN AND GLOBAL LOOP ON EACH SELECTED MODULE
    # --------------------------------------------------------------------------
    for mod_idx in MODULES_SELECTIONNES:
        mod_num = mod_idx + 1
        print("\n" + "#"*80)
        print(f" START OF COMPLETE SEQUENCING FOR MODULE {mod_num}")
        print("#"*80 + "\n")
        
        module_obj = scintil_hal_module_t(mod_idx)
        INTERPOSER_SENSOR = f"Interposer Mod{mod_num}"
        HEATSINK_SENSOR = f"TEC {mod_num} Sink Temp"
        TEC_OBJECT_SENSOR = f"TEC {mod_num} Object Temp"

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        csv_path = os.path.join(dossier_save, f"thermal_results_Mod{mod_num}_{timestamp}.csv")
        img_path = os.path.join(dossier_save, f"thermal_plot_Mod{mod_num}_{timestamp}.png")
        
        historique_donnees = []
        champs_csv = ["Timestamp", "Test_Etape", "Laser_Current_mA"] + CAPTEURS_ACTIFS

        test1_valide = False
        test2a_valide = False
        test2b_valide = False

        # ======================================================================
        # TEST 1 : Initial Module Homogeneity
        # ======================================================================
        if TESTS_ACTIFS.get("Test 1", True):
        
            print(f"--- [MOD {mod_num}] TEST 1 : Temperature Homogeneity ---")
            temps_t1 = lire_toutes_temperatures(hal, [mod_idx])
            
            if temps_t1 is not None:
                # Filter active sensors belonging to the module or global (Mainboard)
                valeurs = [v for k, v in temps_t1.items() if k in CAPTEURS_ACTIFS]
                if valeurs and not all(v == 0.0 for v in valeurs):
                    delta_t = max(valeurs) - min(valeurs)
                    SEUIL_HOMOGENEITE = 5.0
                    print(f"Max deviation observed on Module {mod_num}: {delta_t:.2f}°C")
                    if delta_t <= SEUIL_HOMOGENEITE:
                        print(f" -> TEST 1 PASSED for Module {mod_num}")
                        test1_valide = True
                    else:
                        print(f" -> TEST 1 FAILED: Temperature deviation too high (> {SEUIL_HOMOGENEITE}°C).")
                else:
                    print(" -> TEST 1 FAILED: Sensors inaccessible (0.0°C).")

            if not test1_valide:
                print(f" [STOP] Routine interrupted for Module {mod_num} because Test 1 failed.")
                continue

            print("\n" + "-"*50 + "\n")
            if delta_t <= SEUIL_HOMOGENEITE:
                print(f" -> TEST 1 PASSED for Module {mod_num}")
                test1_valide = True
                bilan_global.setdefault(mod_num, {})["Test 1"] = "Passed"
            else:
                test1_valide = False
                bilan_global.setdefault(mod_num, {})["Test 1"] = f"Failed (Deviation of {delta_t:.2f}°C > {SEUIL_HOMOGENEITE}°C)"
        else:
            test1_valide = True
            bilan_global.setdefault(mod_num, {})["Test 1"] = "Ignored"
            
        # ======================================================================
        # TEST 2A : Interposer Cutoff Safety at 50°C
        # ======================================================================
        if TESTS_ACTIFS.get("Test 2A", True):
      
            print(f"--- [MOD {mod_num}] TEST 2A : Interposer Safety (Cutoff at 50°C) ---")
            controler_ventilateur(hal, active=False)
            #hal.scintil_hal_config_load()
            hal.scintil_hal_sys_enable(True)
            
            # Turning off the TEC to force global thermal rise
            hal.scintil_hal_tec_output_set_enable(module_obj, False)
            
            print(f" -> Turning on the 16 lasers of Module {mod_num} at 150mA...")
            for l_idx in range(16):
                hal.scintil_hal_laser_set_current(module_obj, scintil_hal_laser_t(l_idx), 0.15)
                
            timeout_t2a = time.time() + 300
            while time.time() < timeout_t2a:
                time.sleep(1)
                temps_actuelles = lire_toutes_temperatures(hal, [mod_idx])
                if not temps_actuelles: continue
                
                temp_inter = temps_actuelles.get(INTERPOSER_SENSOR, 0.0)
                print(f"\r Interposer Temperature Mod {mod_num}: {temp_inter:.1f}°C", end="", flush=True)
                if hal.scintil_hal_sys_enabled()['enabled']==0:
                    print(f" -> TEST 2A PASSED: Interposer safety validated at 50°C. Safety activated.")
                    test2a_valide = True
                    bilan_global.setdefault(mod_num, {})["Test 2A"] = "Passed"
                    break
                if temp_inter >= 50:
                    
                    print(f"\n [INFO] Interposer threshold reached ({temp_inter:.2f}°C). Analyzing trigger...")
                    time.sleep(2)
                    
                    if verifier_auto_extinction_lasers(hal, mod_idx):
                        print(f" -> TEST 2A PASSED: Interposer safety validated at 50°C.")
                        bilan_global.setdefault(mod_num, {})["Test 2A"] = "Passed"
                        test2a_valide = True
                    else:
                        print(" -> TEST 2A FAILED: Lasers did not cut off automatically!")
                        bilan_global.setdefault(mod_num, {})["Test 2A"] = "Failed (No automatic laser cutoff at 50°C)"
                        arreter_systeme_securite(hal, mod_idx)
                    break
                    
            if not test2a_valide and time.time() >= timeout_t2a:
                print("\n -> TEST 2A FAILED: Timeout reached without cutting off.")
                arreter_systeme_securite(hal, mod_idx)

            # Mandatory cooling required between the two sub-tests
            attendre_refroidissement(hal, [mod_idx], INTERPOSER_SENSOR, seuil=40.0)

            print("\n" + "-"*50 + "\n")
        else:
            print(f"--- [MOD {mod_num}] TEST 2A : Ignored by user ---")
            test2a_valide = True # Forced to True for the remaining steps
            
        # ======================================================================
        # TEST 2B : Heatsink/TEC Cutoff Safety at 60°C
        # ======================================================================
        if TESTS_ACTIFS.get("Test 2B", True):
        
            if not test2a_valide:
                print(f" [STOP] Routine interrupted for Module {mod_num} because Test 2A failed.")
                continue
            else:
                print(f"--- [MOD {mod_num}] TEST 2B : TEC Heatsink Safety (Cutoff at 60°C) ---")
                controler_ventilateur(hal, active=False)
                #hal.scintil_hal_config_load()
                hal.scintil_hal_sys_enable(True)
                hal.scintil_hal_tec_set_target_object_temp(module_obj, 30.0) 
                hal.scintil_hal_tec_output_set_enable(module_obj, True)
                
                print(f" -> Turning on the 16 lasers of Module {mod_num} again at 150mA...")
                for l_idx in range(16):
                    hal.scintil_hal_laser_set_current(module_obj, scintil_hal_laser_t(l_idx), 0.15)
                    
                timeout_t2b = time.time() + 300
                while time.time() < timeout_t2b:
                    time.sleep(1)
                    temps_actuelles = lire_toutes_temperatures(hal, [mod_idx])
                    if not temps_actuelles: continue
                    
                    temp_hs = temps_actuelles.get(HEATSINK_SENSOR, 0.0)
                    print(f"\r Heat Sink Temperature Mod {mod_num}: {temp_hs:.1f}°C", end="", flush=True)
                    if hal.scintil_hal_sys_enabled()['enabled'] == 0:
                        if temp_hs > 55:
                            print(f" -> TEST 2B PASSED: Interposer safety validated at 50°C. Safety activated.")
                            test2b_valide = True
                            bilan_global.setdefault(mod_num, {})["Test 2B"] = "Passed"
                            break
                        else:
                            print(" -> TEST 2B FAILED: Interposer activated safety instead of heatsink, TEC must be in error mode")
                            bilan_global.setdefault(mod_num, {})["Test 2B"] = "Failed Interposer activated safety instead of heatsink, TEC must be in error mode"
                            arreter_systeme_securite(hal, mod_idx)
                            break
                    if temp_hs >= 60:
                        print(f"\n [INFO] Heatsink threshold reached ({temp_hs:.2f}°C). Analyzing trigger...")
                        time.sleep(1)
                        
                        if verifier_auto_extinction_lasers(hal, mod_idx):
                            print(f" -> TEST 2B PASSED: Heatsink safety validated at 60°C.")
                            test2b_valide = True
                            bilan_global.setdefault(mod_num, {})["Test 2B"] = "Passed"
                        else:
                            print(" -> TEST 2B FAILED: Lasers did not cut off automatically!")
                            bilan_global.setdefault(mod_num, {})["Test 2B"] = "Failed (No automatic laser cutoff at 60°C)"
                            arreter_systeme_securite(hal, mod_idx)
                        break
                        
                if not test2b_valide and time.time() >= timeout_t2b:
                    print("\n -> TEST 2B FAILED: Timeout reached without cutting off.")
                    arreter_systeme_securite(hal, mod_idx)

                # Mandatory cooling after Test 2B
                attendre_refroidissement(hal, [mod_idx], HEATSINK_SENSOR, seuil=40.0)

                print("\n" + "-"*50 + "\n")
                    
        else:
            print(f"--- [MOD {mod_num}] TEST 2B : Ignored by user ---")
            test2b_valide = True # Forced to True for the remaining steps
            
        # ======================================================================
        # TEST 3 : Sweep and Active Regulation Stability
        # ======================================================================
        if TESTS_ACTIFS.get("Test 3", True):
        
            if not test2b_valide:
                print(f" [STOP] Routine interrupted for Module {mod_num} because Test 2B failed.")
                continue

            print(f"--- [MOD {mod_num}] TEST 3 : TEC Stability (Target = 30°C) & Sweep ---")
            hal.scintil_hal_fan_start()
            #hal.scintil_hal_config_load()
            hal.scintil_hal_sys_enable(True)
            hal.scintil_hal_tec_set_target_object_temp(module_obj, 30.0) 
            hal.scintil_hal_tec_output_set_enable(module_obj, True)
            
            courants_sweep = [0.125,0.15,0.175, 0.2] # in A
            test3_echoue = False
            raison_echec = ""
            
            with open(csv_path, mode='w', newline='') as f_csv:
                writer = csv.DictWriter(f_csv, fieldnames=champs_csv)
                writer.writeheader()
                temps_zero = time.time()
                
                for courant in courants_sweep:
                    if test3_echoue: break
                        
                    print(f"\n Step: Applying {courant*1000} mA on the lasers of Module {mod_num}...")
                    for l_idx in range(16):
                        laser_obj = scintil_hal_laser_t(l_idx)
                        try:
                            hal.scintil_hal_laser_set_current(module_obj, laser_obj, float(courant))
                        except Exception as e:
                            print(f" [WARNING] Error configuring Laser {l_idx} Mod {mod_num}: {e}")
                    
                    # Step stabilization variables initialization
                    historique_stabilisation = {k: [] for k in CAPTEURS_ACTIFS}
                    est_stabilise = False
                    temps_stabilise = None
                    timeout_palier = time.time() + 1500 
                    
                    print(f" Waiting for thermal stabilization of all sensors (Deviation < 0.2°C)...")
                    while time.time() < timeout_palier:
                        if hal.scintil_hal_sys_enabled()['enabled'] == 0:
                            break
                        time.sleep(2)  # Sampling every 2 seconds
                        t_courantes = lire_toutes_temperatures(hal, [mod_idx])
                        if not t_courantes: continue
                            
                        # Standard logging in CSV and graphical history
                        timestamp_relatif = round(time.time() - temps_zero, 2)
                        ligne_data = {"Timestamp": timestamp_relatif, "Test_Etape": f"Sweep_{courant}mA", "Laser_Current_mA": courant}
                        for k in CAPTEURS_ACTIFS:
                            ligne_data[k] = t_courantes.get(k, 0.0)
                        writer.writerow(ligne_data)
                        f_csv.flush()
                        historique_donnees.append(ligne_data)
                        
                        # --- STABILIZATION CALCULATION (Sliding window of 8 measurements / 10 seconds) ---
                        tous_stabilises = True
                        for k in CAPTEURS_ACTIFS:
                            if k in t_courantes:
                                historique_stabilisation[k].append(t_courantes[k])
                                if len(historique_stabilisation[k]) > 11:
                                    historique_stabilisation[k].pop(0)  # On garde uniquement les 11 derniers points
                                
                                # Si on n'a pas encore assez de points, ou si l'écart Max-Min de ce capteur >= 0.2°C
                                if k == HEATSINK_SENSOR:
                                    if len(historique_stabilisation[k]) < 11 or abs(historique_stabilisation[k][-1] - historique_stabilisation[k][0]) >= 0.1:
                                        tous_stabilises = False
                                else:
                                    if len(historique_stabilisation[k]) < 11 or abs(max(historique_stabilisation[k]) - min(historique_stabilisation[k])) >= 0.3:
                                        tous_stabilises = False
                            else:
                                tous_stabilises = False
                        
                        # Triggering the 15-second safety margin
                        if tous_stabilises and not est_stabilise:
                            print("\n -> Temperatures stabilized! Starting safety countdown (15s)...")
                            est_stabilise = True
                            temps_stabilise = time.time()
                            
                        if est_stabilise:
                            temps_restant = 15 - (time.time() - temps_stabilise)
                            if temps_restant <= 0:
                                print("\n -> 15s margin successfully elapsed.")
                                break
                            else:
                                print(f"\r Remaining margin before next step: {round(temps_restant)}s ", end="", flush=True)

                        # --- CRITICAL SAFETY MONITORING OF THE TEC OBJECT ---
                        if TEC_OBJECT_SENSOR in CAPTEURS_ACTIFS and t_courantes.get(TEC_OBJECT_SENSOR, 0.0) > 40.0:
                            test3_echoue = True
                            raison_echec = f"The temperature of the TEC object {mod_num} exceeded the safety threshold of 40°C ({t_courantes.get(TEC_OBJECT_SENSOR):.2f}°C)."
                            break
                    
                    if time.time() >= timeout_palier and not est_stabilise:
                        print("\n [WARNING] The step failed to stabilize before the hardware timeout.")
                        
                        if not test3_echoue:
                            t_fin = lire_toutes_temperatures(hal, [mod_idx])
                            if TEC_OBJECT_SENSOR in CAPTEURS_ACTIFS:
                                v_obj = t_fin.get(TEC_OBJECT_SENSOR, 30.0)
                                if not (29.0 <= v_obj <= 31.0):
                                    test3_echoue = True
                                    raison_echec = f"The TEC {mod_num} drifted out of the allowed range ({v_obj:.2f}°C)."

            if not test3_echoue:
                bilan_global.setdefault(mod_num, {})["Test 3"] = "Passed"
            else:
                bilan_global.setdefault(mod_num, {})["Test 3"] = f"Failed ({raison_echec})"
            
            # Targeted safety shutdown at the end of the module run
            arreter_systeme_securite(hal, mod_idx)
            hal.scintil_hal_tec_output_set_enable(module_obj, False)
        else:
            print(f"--- [MOD {mod_num}] TEST 3 : Ignored by user ---")
            
        # Targeted safety shutdown at the end of the module run
        arreter_systeme_securite(hal, mod_idx)
        
        # ======================================================================
        # MODULE GRAPHICAL REPORT GENERATION
        # ======================================================================
        if historique_donnees:
            try:
                plt.figure(figsize=(10, 6))
                timestamps = [d["Timestamp"] for d in historique_donnees]
                for nom_capteur in CAPTEURS_ACTIFS:
                    if nom_capteur in historique_donnees[0]: # Avoids sensors of the non-concerned module
                        y_vals = [d[nom_capteur] for d in historique_donnees]
                        plt.plot(timestamps, y_vals, label=nom_capteur)
                
                plt.title(f"Temperature Evolution - Module {mod_num} (Test 3)")
                plt.xlabel("Time (seconds)")
                plt.ylabel("Temperature (°C)")
                plt.grid(True)
                plt.legend(loc="upper left")
                plt.savefig(img_path)
                print(f"Module {mod_num} graph saved: {img_path}")
                plt.show()
                
                # Displaying the summary graphical popup
                popup = tk.Toplevel()
                popup.title("Thermal Routine Summary")
                popup.geometry("550x450")
                popup.attributes("-topmost", True)
                popup.configure(bg="#F5F5F7")
                
                tk.Label(popup, text="FINAL TEST REPORT", font=("Arial", 12, "bold"), bg="#F5F5F7", fg="#1D1D1F", pady=10).pack()
                
                txt = tk.Text(popup, font=("Consolas", 10), padx=10, pady=10, relief="flat", bd=0)
                txt.pack(fill="both", expand=True, padx=15, pady=5)
                
                msg = ""
                for m, tests in bilan_global.items():
                    msg += f"==================== MODULE {m} ====================\n"
                    for t_name, status in tests.items():
                        msg += f" [{t_name:<7}] : {status}\n"
                    msg += "\n"
                    
                txt.insert("1.0", msg)
                txt.config(state="disabled")
                tk.Button(popup, text="Close", command=popup.destroy, font=("Arial", 10, "bold"), bg="#E5E5EA", relief="flat", pady=5).pack(pady=10)
                popup.mainloop()
            except Exception as e:
                print(f" [WARNING] Graphical tracing impossible for Mod {mod_num}: {e}")

    # Force reactivating the fan at the end of the global routine
    controler_ventilateur(hal, active=True)

if __name__ == "__main__":
    try:
        executer_routine_tests()
    except KeyboardInterrupt:
        print("\n [CANCELLATION] Interrupted by user.")
    print("\n" + "="*50)
    input("All test routines are completed. Press Enter to quit...")
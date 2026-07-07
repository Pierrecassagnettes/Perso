# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import numpy as np
import pandas as pd
import json
import logging
from datetime import datetime
import threading
import traceback

# Matplotlib integration in Tkinter
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Custom imports
from ESA import AG8563
from MeasurementSession import MeasurementSession


class InstrumentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scintil Photonics - Advanced ESA Tool")
        self.root.geometry("1450x1024")
        
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Instrument & Cache Control Variables
        self.ESA_inst = None
        self.is_connected = False
        self.json_entries = {}
        self.current_json_path = os.path.join(self.script_dir, "esa_parameters_wide.json")
        self.title_info = {}
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Build UI Structure
        self.create_widgets()
        self.load_json_parameters()
        

    def create_widgets(self):
        # Main layout split (Left: Controls and Tabs, Right: Graph Preview)
        main_paned = ttk.PanedWindow(self.root, orient="horizontal")
        main_paned.pack(fill="both", expand=True, padx=10, pady=5)
        
        left_frame = ttk.Frame(main_paned)
        right_frame = ttk.Frame(main_paned)
        
        main_paned.add(left_frame, weight=1)
        main_paned.add(right_frame, weight=1)
        
        # ----------------------------------------------------
        # 1. Left Side: Notebook (Tabs Setup)
        # ----------------------------------------------------
        self.notebook = ttk.Notebook(left_frame)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)
        
        tab_single = ttk.Frame(self.notebook)
        tab_multi = ttk.Frame(self.notebook)
        
        self.notebook.add(tab_single, text=" Single Mode & Metadata ")
        self.notebook.add(tab_multi, text=" Multi-Range Configuration ")
        
        # --- TAB 1 CONTENT: Metadata & JSON Params ---
        self.param_frame = ttk.LabelFrame(tab_single, text=" Laser Metadata ", padding=10)
        self.param_frame.pack(fill="x", padx=5, pady=5)
        
        self.entries = {}
        fields = [
            ("Package Name", "LA1-9"),
            ("Laser Name", "F0"),
            ("Temperature (°C)", "30"),
            ("current (mA)", "150"),
            ("DC Optical Power PR (mA)", "0.967"),
            ("Lot ID", "None"),
            ("Wafer ID", "None"),
            ("Product ID", "None"),
            ("Prober ID", "S02"),
            ("Operator", "Pierre Cassagnettes")
        ]
        
        for i, (label_text, default_val) in enumerate(fields):
            lbl = ttk.Label(self.param_frame, text=label_text)
            lbl.grid(row=i, column=0, sticky="w", pady=2, padx=5)
            entry = ttk.Entry(self.param_frame, width=25)
            entry.insert(0, default_val)
            entry.grid(row=i, column=1, columnspan=2, sticky="ew", pady=2, padx=5)
            if label_text != "Laser Name":
                dict_key = label_text.lower().split(" ")[0]
            else:
                dict_key = label_text
            self.entries[dict_key] = entry
            
        # Saving Directory Row
        curr_row = len(fields)
        lbl_saving = ttk.Label(self.param_frame, text="Saving Directory")
        lbl_saving.grid(row=curr_row, column=0, sticky="w", pady=2, padx=5)
        entry_saving = ttk.Entry(self.param_frame, width=25)
        entry_saving.insert(0, r"C:\Users\pierre.cassagnettes\Documents\RIN_scripts\Test")
        entry_saving.grid(row=curr_row, column=1, sticky="ew", pady=2, padx=5)
        self.entries["saving"] = entry_saving
        
        btn_browse = ttk.Button(self.param_frame, text="Browse...", command=self.browse_directory)
        btn_browse.grid(row=curr_row, column=2, sticky="w", pady=2, padx=5)
        self.param_frame.columnconfigure(1, weight=1)
        
        self.json_param_frame = ttk.LabelFrame(tab_single, text=" Single Run Setup (JSON Constants & Scales) ", padding=10)
        self.json_param_frame.pack(fill="x", padx=5, pady=5)
        
        # --- TAB 2 CONTENT: Fully Editable Multi-Range Matrix Grid ---
        r_info_lbl = ttk.Label(tab_multi, text="Modify frequency ranges profile settings as needed:", font=("Helvetica", 9, "italic"))
        r_info_lbl.pack(anchor="w", padx=10, pady=5)
        
        self.multi_frame = ttk.LabelFrame(tab_multi, text=" Frequency Grid Parameters Table ", padding=10)
        self.multi_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        headers = ["Active", "Range Segment Name", "Center (MHz)", "Span (MHz)", "RBW (kHz)", "VBW (kHz)"]
        for col_idx, h_text in enumerate(headers):
            h_lbl = ttk.Label(self.multi_frame, text=h_text, font=("Helvetica", 9, "bold"))
            h_lbl.grid(row=0, column=col_idx, padx=6, pady=5, sticky="w")
            
        self.default_ranges = [
            {"active": True, "name": "100 kHz - 10 MHz", "center": "5.05", "span": "9.9", "rbw": "10", "vbw": "3"},
            {"active": True, "name": "10 MHz - 100 MHz", "center": "55.0", "span": "90.0", "rbw": "30", "vbw": "10"},
            {"active": True, "name": "100 MHz - 1 GHz", "center": "550.0", "span": "900.0", "rbw": "100", "vbw": "30"},
            {"active": True, "name": "1 GHz - 10 GHz", "center": "5500.0", "span": "9000.0", "rbw": "1000", "vbw": "300"},
            {"active": True, "name": "10 GHz - 26 GHz", "center": "18000.0", "span": "16000.0", "rbw": "2000", "vbw": "3000"}
        ]
        
        self.range_rows_widgets = []
        for row_idx, r_data in enumerate(self.default_ranges, start=1):
            act_var = tk.BooleanVar(value=r_data["active"])
            cb = ttk.Checkbutton(self.multi_frame, variable=act_var)
            cb.grid(row=row_idx, column=0, padx=5, pady=3)
            
            ent_name = ttk.Entry(self.multi_frame, width=22)
            ent_name.insert(0, r_data["name"])
            ent_name.grid(row=row_idx, column=1, padx=5, pady=3, sticky="ew")
            
            ent_center = ttk.Entry(self.multi_frame, width=12)
            ent_center.insert(0, r_data["center"])
            ent_center.grid(row=row_idx, column=2, padx=5, pady=3, sticky="ew")
            
            ent_span = ttk.Entry(self.multi_frame, width=12)
            ent_span.insert(0, r_data["span"])
            ent_span.grid(row=row_idx, column=3, padx=5, pady=3, sticky="ew")
            
            ent_rbw = ttk.Entry(self.multi_frame, width=10)
            ent_rbw.insert(0, r_data["rbw"])
            ent_rbw.grid(row=row_idx, column=4, padx=5, pady=3, sticky="ew")
            
            ent_vbw = ttk.Entry(self.multi_frame, width=10)
            ent_vbw.insert(0, r_data["vbw"])
            ent_vbw.grid(row=row_idx, column=5, padx=5, pady=3, sticky="ew")
            
            self.range_rows_widgets.append({
                "active": act_var, "name": ent_name, "center": ent_center,
                "span": ent_span, "rbw": ent_rbw, "vbw": ent_vbw
            })
            
        self.multi_frame.columnconfigure(1, weight=2)
        
        # ----------------------------------------------------
        # 2. Left Side: Bottom Universal Instrument Control Panel
        # ----------------------------------------------------
        control_frame = ttk.LabelFrame(left_frame, text=" Execution & Hardware Control ", padding=10)
        control_frame.pack(fill="x", padx=5, pady=5, side="bottom")
        
        # Row 1: Connection Status
        conn_frame = ttk.Frame(control_frame)
        conn_frame.pack(fill="x", pady=2)
        self.btn_connect = ttk.Button(conn_frame, text="Connect Instrument", command=self.connect_instrument)
        self.btn_connect.pack(side="left", padx=5)
        
        self.ind_canvas = tk.Canvas(conn_frame, width=16, height=16, highlightthickness=0)
        self.ind_canvas.pack(side="left", padx=5)
        self.status_led = self.ind_canvas.create_oval(2, 2, 14, 14, fill="red")
        self.lbl_status = ttk.Label(conn_frame, text="Disconnected", foreground="red")
        self.lbl_status.pack(side="left", padx=5)
        
        
        # Row 3: Measurement Trigger Actions Buttons
        action_btn_frame = ttk.Frame(control_frame)
        action_btn_frame.pack(fill="x", pady=6)
        
        self.btn_run_single = ttk.Button(action_btn_frame, text="Run Single Scan (JSON Config)", command=lambda: self.start_meas_thread(mode="single"), state="disabled")
        self.btn_run_single.pack(side="left", fill="x", expand=True, padx=4)
        
        self.btn_run_multi = ttk.Button(action_btn_frame, text="Run Multi-Range Scan & Stitch", command=lambda: self.start_meas_thread(mode="multi"), state="disabled")
        self.btn_run_multi.pack(side="right", fill="x", expand=True, padx=4)
        
        self.progress = ttk.Progressbar(control_frame, orient="horizontal", mode="indeterminate")
        self.progress.pack(fill="x", pady=4)
        
        # ----------------------------------------------------
        # 3. Right Side: Figure Presentation Panel
        # ----------------------------------------------------
        plot_frame = ttk.LabelFrame(right_frame, text=" Spectral Plot Graphic Visualization Display ", padding=10)
        plot_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    # ----------------------------------------------------
    # Configuration Parsing & Helper Logic Methods
    # ----------------------------------------------------
    def load_json_parameters(self):
        for widget in self.json_param_frame.winfo_children():
            widget.destroy()
        self.json_entries = {}
        if not os.path.exists(self.current_json_path):
            return
        try:
            with open(self.current_json_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                
            if "esa_ref_level (dBm)" not in json_data:
                json_data["esa_ref_level (dBm)"] = -10
            if "esa_log_scale (dB/div)" not in json_data:
                json_data["esa_log_scale (dB/div)"] = 5
                
            for i, (key, value) in enumerate(json_data.items()):
                lbl = ttk.Label(self.json_param_frame, text=key)
                lbl.grid(row=i, column=0, sticky="w", pady=1, padx=5)
                entry = ttk.Entry(self.json_param_frame, width=18)
                entry.insert(0, str(value))
                entry.grid(row=i, column=1, sticky="ew", pady=1, padx=5)
                self.json_entries[key] = entry
                
            btn_save = ttk.Button(self.json_param_frame, text="Save Settings to File", command=self.save_json_parameters)
            btn_save.grid(row=len(json_data), column=0, columnspan=2, pady=5, sticky="ew")
            self.json_param_frame.columnconfigure(1, weight=1)
        except Exception as e:
            print(f"Error reading JSON setup fields: {e}")

    def save_json_parameters(self):
        try:
            with open(self.current_json_path, "r", encoding="utf-8") as f:
                orig = json.load(f)
            new_data = {}
            for k, entry in self.json_entries.items():
                val_str = entry.get()
                t = type(orig.get(k, -10))
                new_data[k] = val_str.lower() in ("true", "1") if t == bool else t(val_str)
            with open(self.current_json_path, "w", encoding="utf-8") as f:
                json.dump(new_data, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Success", "Configuration file synchronization complete.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed saving options matrix: {e}")

    def get_active_ui_ranges_list(self):
        parsed_ranges = []
        for idx, row in enumerate(self.range_rows_widgets):
            if row["active"].get():
                try:
                    parsed_ranges.append({
                        "row_index": idx,
                        "name": row["name"].get(),
                        "center": float(row["center"].get()),
                        "span": float(row["span"].get()),
                        "rbw": float(row["rbw"].get()),
                        "vbw": float(row["vbw"].get())
                    })
                except ValueError:
                    pass
        return parsed_ranges

    

    def browse_directory(self):
        initial_dir = self.entries["saving"].get()
        if not os.path.exists(initial_dir):
            initial_dir = "C:\\"
        selected = filedialog.askdirectory(initialdir=initial_dir, title="Select Saving Folder Context Location")
        if selected:
            self.entries["saving"].delete(0, tk.END)
            self.entries["saving"].insert(0, os.path.normpath(selected))

    def connect_instrument(self):
        try:
            self.ESA_inst = AG8563('ESA_8563')
            self.ESA_inst.set_vbw(3.0)
            self.ind_canvas.itemconfig(self.status_led, fill="green")
            self.lbl_status.config(text="Connected to AG8563", foreground="green")
            self.is_connected = True
            self.btn_run_single.configure(state="normal")
            self.btn_run_multi.configure(state="normal")
            messagebox.showinfo("Success", "GPIB communication interface linked successfully.")
        except Exception:
            self.ind_canvas.itemconfig(self.status_led, fill="red")
            self.lbl_status.config(text="Connection Refused", foreground="red")
            self.is_connected = False
            messagebox.showerror("Hardware Error", f"Instrument connection failed:\n\n{traceback.format_exc()}")

    
    def start_meas_thread(self, mode):
        self.btn_run_single.configure(state="disabled")
        self.btn_run_multi.configure(state="disabled")
        self.progress.start(10)
        threading.Thread(target=self.run_measurement_sequence, args=(mode,), daemon=True).start()

    def run_measurement_sequence(self, mode):
        try:
            p_name = self.entries["package"].get()
            l_name = self.entries["Laser Name"].get()
            temp = self.entries["temperature"].get()
            l_curr = self.entries["current"].get()
            dc_opt = float(self.entries["dc"].get())
            parent_dir = self.entries["saving"].get()
            
            with open(self.current_json_path, "r", encoding="utf-8") as f:
                json_static = json.load(f)
                
            esa_resistance = json_static["esa_resistance (ohm)"]
            pr_responsivity = json_static["pr_responsivity"]
            pr_ac_factor = json_static["pr_ac_factor"] / 2.0
            alpha = 1.128
            attenuation_input = json_static["input's attenuation (dB)"]
            esa_average = json_static["esa_average"]
            
            ref_level = float(json_static.get("esa_ref_level (dBm)", -10))
            log_scale = float(json_static.get("esa_log_scale (dB/div)", 5))
            scan_tasks = []
            center = float(self.json_entries["esa_center_frequency (Mhz)"].get())
            if mode == "single":
                scan_tasks.append({
                    "center": center,
                    "span": float(self.json_entries["esa_span_frequency (Mhz)"].get()),
                    "rbw": float(self.json_entries["esa_rbw (Khz)"].get()),
                    "vbw": float(self.json_entries["esa_vbw (Khz)"].get()),
                    "filename": f'{l_name}_{center/1000}GHz_{l_curr}mA_{temp}C'  
                })
            else:
                active_ranges = self.get_active_ui_ranges_list()
                if not active_ranges:
                    self.root.after(0, lambda: messagebox.showwarning("Execution Aborted", "Select at least one range block spectrum."))
                    return
                for r in active_ranges:
                    scan_tasks.append({
                        "center": r["center"], "span": r["span"], "rbw": r["rbw"], "vbw": r["vbw"],
                        "filename": f'{l_name}_{r["center"]}M_{l_curr}mA_{temp}C'  
                    })

            data_dir = os.path.join(parent_dir, 'Data', p_name if (p_name != 'None' and p_name != '') else self.entries["wafer"].get(), f'{temp}C')
            os.makedirs(data_dir, exist_ok=True)
            os.chdir(data_dir)
            
            list_freqs, list_signals, list_rins= [], [], []
            
            meta_data = {'Lot_id': self.entries["lot"].get(), 'Wafer_id': self.entries["wafer"].get(),
                         'Product_id': self.entries["product"].get(), 'Acq_script': "Advanced_ESA_App",
                         'Operator': self.entries["operator"].get(), 'Prober': self.entries["prober"].get()}
            session = MeasurementSession(meta_data=meta_data)
            
            self.ESA_inst.configure_amplitude_scales(ref_level, log_scale)
            
            global_min_hz = float('inf')
            global_max_hz = float('-inf')
            
            for task in scan_tasks:
                t_key = (task["center"], task["span"], task["rbw"], task["vbw"])
                
                min_screen_hz = (task["center"] - (task["span"] / 2.0)) * 1e6
                max_screen_hz = (task["center"] + (task["span"] / 2.0)) * 1e6
                
                if min_screen_hz < global_min_hz: global_min_hz = min_screen_hz
                if max_screen_hz > global_max_hz: global_max_hz = max_screen_hz
                
                self.ESA_inst.attenuation(attenuation_input)
                self.ESA_inst.set_rbw(task["rbw"])
                self.ESA_inst.set_vbw(task["vbw"])
                self.ESA_inst.set_single_shot()
                self.ESA_inst.set_center_span(task["center"], task["span"])
                self.ESA_inst.set_average(esa_average)
                
                self.ESA_inst.trigger_measure()
                raw_data = self.ESA_inst.get_data()
                
                f_axis = raw_data[:, 0]
                m_dBm = raw_data[:, 1]
                
                screen_mask = (f_axis >= min_screen_hz) & (f_axis <= max_screen_hz) & (m_dBm != 90)
                
                f_axis = f_axis[screen_mask]
                m_dBm = m_dBm[screen_mask]
                if len(f_axis) == 0:
                    continue
                
                p_meas_lin = 10.0 ** (m_dBm / 10.0)
                corrected_lin = p_meas_lin
                corrected_dBm = 10.0 * np.log10(corrected_lin)
                esa_nbw = task["rbw"] * alpha * 1000.0
                dc_opt_power = dc_opt / pr_responsivity * 0.001
                
                epsd = 10.0**(corrected_dBm / 10.0) * 0.001 / esa_nbw
                evsd = esa_resistance * epsd
                opsd = evsd / (pr_ac_factor ** 2)
                rin_lin = opsd / (dc_opt_power ** 2)
                rin_dB = 10.0 * np.log10(rin_lin)
                
                list_freqs.append(f_axis)
                list_signals.append(corrected_dBm)
                list_rins.append(rin_dB)
                    
                data_np = np.column_stack((f_axis, corrected_dBm, rin_dB))
                data_pd = pd.DataFrame(data_np, columns=['Frequency__Hz', 'Power_Corrected__dBm', 'RIN_dB_Hz'])
                m_obj = session.create_measurement(
                    data_pd, die_id='None', package_id=p_name, temperature=temp, device_id=f'{l_name}',
                    measurement_type='ESA', RBW=f'{task["rbw"]}kHz', VBW=f'{task["vbw"]}kHz',
                    center_frequancy=f'{task["center"]}MHz', span_frequancy=f'{task["span"]}MHz',
                    Laser_current=f"{l_curr}mA", DC_optical_power_PR=f'{dc_opt}mA'
                    )
                m_obj.save_to_txt_old(task["filename"], overwrite=True)
                
            full_f = np.concatenate(list_freqs)
            full_s = np.concatenate(list_signals)
            full_r = np.concatenate(list_rins)
            
            sort_idx = np.argsort(full_f)
            final_f = full_f[sort_idx]
            final_s = full_s[sort_idx]
            final_r = full_r[sort_idx]
            
            
            global_name = f'ESA_{l_curr}mA_{temp}_C'
            
            self.root.after(0, lambda: self.render_plots_log_scale(final_f, final_s, final_r, global_name, data_dir, global_min_hz, global_max_hz,mode))
            self.root.after(0, lambda: messagebox.showinfo("Success", f"Measurement sequence complete [{mode.upper()}]."))
            
        except Exception:
            err = traceback.format_exc()
            self.root.after(0, lambda: messagebox.showerror("Sequence Failure Fault", f"Execution crashed:\n\n{err}"))
        finally:
            self.root.after(0, self.end_execution_ui)

    def render_plots_log_scale(self, f, s, r, filename, data_dir, limit_min_hz, limit_max_hz,mode):
        self.fig.clear()
        ax0 = self.fig.add_subplot(211)
        ax1 = self.fig.add_subplot(212)
        
        f_ghz = f * 1e-9
        xlim_min = limit_min_hz * 1e-9 
        xlim_max = limit_max_hz * 1e-9
        largeur = xlim_max - xlim_min
        if mode == 'single' :
            xlim_min -= 0.03*largeur
            xlim_max+= 0.03*largeur
        # Upper Spectrum Graph
        ax0.plot(f_ghz, s, color='tab:blue', label="Signal")
        
            
        ax0.set_ylabel("Signal Corrected (dBm)")
        if mode != 'single':
            ax0.set_xscale('log')
        ax0.set_xlim(xlim_min, xlim_max)
        ax0.grid(True, which="both", linestyle="--")
        ax0.set_title(f"{filename.replace('_',' ')}", fontsize=9, fontweight="bold")
        
        # Lower RIN Spectrum Graph
        ax1.plot(f_ghz, r, color='tab:orange')
        ax1.set_ylabel("RIN (dB/Hz)")
        ax1.set_xlabel("Frequency Vector (GHz)")
        if mode != 'single':
            ax1.set_xscale('log')
        ax1.set_xlim(xlim_min, xlim_max)
        ax1.grid(True, which="both", linestyle="--")
        
        self.fig.tight_layout()
        self.canvas.draw()
        if mode =='single':
            self.fig.savefig(os.path.join(data_dir, f"{filename}_{largeur/2}.png"))
        else:
            self.fig.savefig(os.path.join(data_dir, f"{filename}.png"))

    def end_execution_ui(self):
        self.progress.stop()
        self.btn_run_single.configure(state="normal")
        self.btn_run_multi.configure(state="normal")

    def on_closing(self):
        plt.close('all')
        self.root.quit()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = InstrumentApp(root)
    root.mainloop()
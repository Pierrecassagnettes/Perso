# -*- coding: utf-8 -*-
"""
Tkinter GUI for Scintil Photonics Multi-Wafer Sorting & Loss Analysis Workflow.
Regrouped Figures Edition - English Version - Fully Debugged Checkbox Edition.

Author: Pierre Cassagnettes
"""

import os
import sys
import yaml
import tempfile
import textwrap
import threading
import numpy as np
import pandas as pd
from collections import defaultdict

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
matplotlib.use("Agg") 

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import WaferMap

import ctypes

# Attempt to configure High DPI scaling for crisp fonts and graphics on Windows
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass


def display_image(root, file_path):
    """
    Creates a top-level window to preview a generated PNG plot image, scaling it 
    optimally to fit within 75% of the user's current screen resolution.

    Args:
        root (tk.Tk): The parent Tkinter root window.
        file_path (str): The absolute filesystem path to the PNG image.

    Returns:
        None
    """
    if not file_path or not os.path.exists(file_path):
        return
        
    img_window = tk.Toplevel(root)
    img_window.title(f"Preview: {os.path.basename(file_path)}")

    img = Image.open(file_path)
    
    # Calculate screen-relative bounding box dimensions
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    max_w = int(screen_w * 0.75)
    max_h = int(screen_h * 0.75)
    
    # Resize keeping the aspect ratio using Lanczos resampling
    img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(img_window, image=photo, bg="white")
    label.image = photo  # Keep a reference to prevent garbage collection
    label.pack(padx=10, pady=10)


def extract_loss_data(root_data, wafer, loss_type, wavelength):
    """
    Parses and filters waveguide propagation loss data from a wafer's processed result text file
    at a specific test wavelength.

    Args:
        root_data (str): The root folder path of the wafer database.
        wafer (str): The wafer identifier subdirectory.
        loss_type (str): The type of loss (e.g., 'NWG', 'RWG', 'SWG').
        wavelength (str/float): Target wavelength in nanometers.

    Returns:
        pd.DataFrame: A filtered DataFrame containing the non-null extracted loss values.
    """
    proc_dir = os.path.join(root_data, wafer, "Processing_results")
    filename = f"{wafer}_{loss_type}_loss_extraction.txt"
    filepath = os.path.join(proc_dir, filename)
    
    if not os.path.exists(filepath):
        return pd.DataFrame()
    try:
        df = pd.read_csv(filepath, sep="\t")
        if "Wavelength (nm)" in df.columns and "Result" in df.columns and "Die name" in df.columns:
            df["Wavelength (nm)"] = pd.to_numeric(df["Wavelength (nm)"], errors="coerce")
            df_filtered = df[df["Wavelength (nm)"] == float(wavelength)].copy()
            return df_filtered.dropna(subset=["Result"])
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return pd.DataFrame()


def extract_tlm_data(root_data, wafer, column_name):
    """
    Parses and extracts specific TLM (Transmission Line Measurement) metrics for a wafer 
    from its respective extraction data sheet.

    Args:
        root_data (str): The root folder path of the wafer database.
        wafer (str): The wafer identifier subdirectory.
        column_name (str): The column name representing the desired measurement parameter.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted metrics with empty fields removed.
    """
    proc_dir = os.path.join(root_data, wafer, "Processing_results")
    filename = f"{wafer}_TLM_InPN_extraction.txt"
    filepath = os.path.join(proc_dir, filename)
    
    if not os.path.exists(filepath):
        return pd.DataFrame()
    try:
        df = pd.read_csv(filepath, sep="\t")
        if column_name in df.columns and "Die name" in df.columns:
            return df.dropna(subset=[column_name])
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return pd.DataFrame()


def extract_laser_data(root_data, wafer, column_name, laser_name, temperature, current):
    """
    Retrieves and filters laser performance metrics from a wafer's processed DOE laser extraction files
    based on laser name, experimental temperature, and bias current.

    Args:
        root_data (str): The root folder path of the wafer database.
        wafer (str): The wafer identifier subdirectory.
        column_name (str): The measured parameter column to extract.
        laser_name (str): Identifier of the laser structure.
        temperature (str): Target temperature (or "Aucune" / "None" if unassigned).
        current (str): Target injected current (or "Aucune" / "None" if unassigned).

    Returns:
        pd.DataFrame: A filtered DataFrame containing non-null rows matching the user criteria.
    """
    proc_dir = os.path.join(root_data, wafer, "Processing_results")
    filename = f"{wafer}_DOE_laser_extraction.txt"
    filepath = os.path.join(proc_dir, filename)
    
    if not os.path.exists(filepath):
        return pd.DataFrame()
    try:
        df = pd.read_csv(filepath, sep="\t")
        if column_name in df.columns and "Die name" in df.columns:
            # Filter by laser layout structure name
            if "Laser name" in df.columns and laser_name:
                df = df[df["Laser name"].astype(str) == str(laser_name)]
            
            # Filter by test Temperature
            if "Temperature (C)" in df.columns and temperature:
                if temperature == "Aucune":
                    df = df[df["Temperature (C)"].isna() | (df["Temperature (C)"].astype(str).str.strip() == "")]
                else:
                    try:
                        target_temp = float(temperature)
                        df = df[pd.to_numeric(df["Temperature (C)"], errors='coerce') == target_temp]
                    except ValueError:
                        df = df[df["Temperature (C)"].astype(str) == str(temperature)]
                    
            # Filter by injection Current
            if "Current (mA)" in df.columns and current:
                if current == "Aucune":
                    df = df[df["Current (mA)"].isna() | (df["Current (mA)"].astype(str).str.strip() == "")]
                else:
                    try:
                        target_curr = float(current)
                        df = df[pd.to_numeric(df["Current (mA)"], errors='coerce') == target_curr]
                    except ValueError:
                        df = df[df["Current (mA)"].astype(str) == str(current)]
                    
            return df.dropna(subset=[column_name])
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return pd.DataFrame()


def round_to_3_sig_figs(val):
    """
    Formats a numeric value to three significant figures. Non-numeric or NaN parameters 
    are returned unchanged.

    Args:
        val (any): A numeric float/int, or NaN value.

    Returns:
        float or any: The rounded value, or original element if non-convertible.
    """
    if pd.isna(val):
        return val
    try:
        num = float(val)
        if num == 0.0:
            return 0.0
        return float(f"{num:.3g}")
    except Exception:
        return val


def generate_regrouped_plots(root_data, wafer_list, selected_wave, plot_choices, save_plots, screen_w, screen_h, wafers_db):
    """
    The core calculation and rendering backend engine. Processes the configured dataset matrix
    and compiles regrouped wafer maps alongside unified boxplot distributions with custom scaling rules.

    Args:
        root_data (str): Folder containing wafer performance folders.
        wafer_list (list): List of selected wafers to build plots for.
        selected_wave (str): The operational optical wavelength (nm) chosen for loss analysis.
        plot_choices (dict): Configuration dictionary containing bounds, scales, and target parameters.
        save_plots (bool): If True, saves outputs to disk. Otherwise, saves to a temporary directory.
        screen_w (int): Screen width used for dynamic canvas adjustment.
        screen_h (int): Screen height used for dynamic canvas adjustment.
        wafers_db (dict): Metadata mapping wafer IDs to Tapeout and Fab details.

    Returns:
        list: Filepaths of all generated PNG plot configurations.
    """
    saving_path = plot_choices.get("saving_path", "")
    generated_files = []
    target_dir = saving_path if save_plots else tempfile.gettempdir()
    
    # Calculate a responsive figure scale relative to the screen dimensions
    dynamic_width = max(13, int(screen_w * 0.0085))
    dynamic_height = max(7, int(screen_h * 0.0085))
    
    fig_groups = []

    # Waveguide loss groupings (NWG, RWG, SWG)
    for loss_key in ["NWG", "RWG", "SWG"]:
        if plot_choices.get(loss_key.lower()):
            cfg = plot_choices["loss_configs"][loss_key]
            fig_groups.append({
                "type": "loss", 
                "key": loss_key, 
                "label": f"{loss_key} Loss", 
                "items": [{
                    "type": "loss", "key": loss_key, "label": f"{loss_key} Loss", "col": "Result",
                    "spec": cfg["spec"], "ymin": cfg["ymin"], "ymax": cfg["ymax"], "cbmin": cfg["cbmin"], "cbmax": cfg["cbmax"]
                }]
            })
    
    # TLM parameter groupings
    for tlm_item in plot_choices.get("dynamic_tlm", []):
        c = tlm_item["col"]
        fig_groups.append({
            "type": "tlm", 
            "key": f"TLM_{c}", 
            "label": f"TLM {c}", 
            "items": [{
                "type": "tlm", "key": c, "label": f"TLM {c}", "col": c,
                "spec": tlm_item["spec"], "ymin": tlm_item["ymin"], "ymax": tlm_item["ymax"], "cbmin": tlm_item["cbmin"], "cbmax": tlm_item["cbmax"]
            }]
        })
        
    # Laser parameter groupings (supporting multi-plot configuration sheets)
    laser_items = plot_choices.get("dynamic_laser_items", [])
    laser_groups = defaultdict(list)
    for item_config in laser_items:
        c = item_config["col"]
        n = item_config["laser_name"]
        t = item_config["temperature"]
        curr = item_config["current"]
        gid = item_config["group_id"]
        
        parts = []
        if t != "Aucune": parts.append(f"{t}°C")
        if curr != "Aucune": parts.append(f"{curr}mA")
        cond_str = f" ({', '.join(parts)})" if parts else ""
        
        laser_groups[gid].append({
            "type": "laser",
            "key": f"{c}_{n}_{t}_{curr}",
            "label": f"Laser {n} - {c}{cond_str}",
            "col": c,
            "laser_name": n,
            "temperature": t,
            "current": curr,
            "spec": item_config["spec"],
            "ymin": item_config["ymin"],
            "ymax": item_config["ymax"],
            "cbmin": item_config["cbmin"],
            "cbmax": item_config["cbmax"]
        })
        
    # Finalize laser regrouping layouts (single display or grouped in panels)
    for gid in sorted(laser_groups.keys()):
        g_items = laser_groups[gid]
        if len(g_items) == 1:
            g_label = g_items[0]["label"]
        else:
            unique_cols = sorted(list(set(item["col"] for item in g_items)))
            g_label = f"{', '.join(unique_cols)}"
            
        fig_groups.append({"type": "laser", "key": f"Laser_Group_{gid}", "label": g_label, "items": g_items})

    # Render loop processing each data configuration group
    for group in fig_groups:
        g_type = group["type"]
        g_label = group["label"]
        g_key = group["key"]
        
        group_dfs = defaultdict(dict)
        all_wafers_with_data = set()
        group_has_data = False
        
        # Aggregate raw data across selected wafer lots
        for item in group["items"]:
            lk = item["key"]
            col_name = item["col"]
            for wafer in wafer_list:
                if g_type == "loss":
                    df_l = extract_loss_data(root_data, wafer, lk, selected_wave)
                elif g_type == "tlm":
                    df_l = extract_tlm_data(root_data, wafer, col_name)
                elif g_type == "laser":
                    df_l = extract_laser_data(root_data, wafer, col_name, item["laser_name"], item["temperature"], item["current"])
                    
                if not df_l.empty:
                    group_dfs[lk][wafer] = df_l
                    all_wafers_with_data.add(wafer)
                    group_has_data = True

        if not group_has_data:
            continue

        wafers_sorted = sorted(list(all_wafers_with_data))
        num_wafers = len(wafers_sorted)
        num_items = len(group["items"])
        
        # Validate grid layout constraints based on populated wafer lots
        valid_maps_count = 0
        for item in group["items"]:
            for wafer in wafers_sorted:
                if not group_dfs[item["key"]].get(wafer, pd.DataFrame()).empty:
                    valid_maps_count += 1

        if valid_maps_count == 0:
            continue

        # Setup responsive wafer map matrix dimension grids
        ncols_map = min(4, valid_maps_count)
        nrows_map = (valid_maps_count - 1) // ncols_map + 1
        
        fig_map, axes_map = plt.subplots(
            nrows_map, ncols_map, 
            figsize=(max(4 * ncols_map, dynamic_width), max(4 * nrows_map, dynamic_height))
        )
        title_top = f"Regrouped WaferMaps - {g_label}" + (f" at {selected_wave} nm" if g_type == "loss" else "")
        fig_map.suptitle(title_top, fontsize=13, weight="bold")
        
        if valid_maps_count == 1:
            axes_map_flat = [axes_map]
        else:
            axes_map_flat = np.array(axes_map).flatten()

        # Render wafer map matrix subplots
        map_idx = 0
        for item in group["items"]:
            lk = item["key"]
            col_name = item["col"]
            cb_range = (item["cbmin"], item["cbmax"]) if (item["cbmin"] is not None and item["cbmax"] is not None) else None
            
            for wafer in wafers_sorted:
                df_l = group_dfs[lk].get(wafer, pd.DataFrame())
                
                if df_l.empty:
                    continue 
                    
                ax = axes_map_flat[map_idx]
                    
                map_dict = {}
                for _, row in df_l.iterrows():
                    if str(col_name) == "Peak wavelength (nm)":
                        v = round(row[col_name], 2) if not pd.isna(row[col_name]) else row[col_name]
                    else:
                        v = round_to_3_sig_figs(row[col_name])
                    map_dict[str(row["Die name"]).lower()] = v
                
                w_info = wafers_db.get(wafer, {})
                w_tapeout = w_info.get("tapeout", "Unknown")
                w_fab = w_info.get("Fab_IIIV", "Unknown")
                
                if g_type == "laser":
                    p_labels = []
                    if item.get("laser_name"): p_labels.append(f"Laser: {item['laser_name']}\n")
                    if item.get("temperature") and item["temperature"] != "Aucune": p_labels.append(f"{item['temperature']}°C")
                    if item.get("current") and item["current"] != "Aucune": p_labels.append(f"{item['current']}mA")
                    title_str = f"Wafer: {wafer}\n {' '.join(p_labels)}\nTO: {w_tapeout} | Fab: {w_fab}"
                else:
                    lbl_short = item['label'].split(' - ')[0] if ' - ' in item['label'] else item['label']
                    title_str = f"Wafer: {wafer}\n{lbl_short}\nTO: {w_tapeout} | Fab: {w_fab}"
                    
                try:
                    # Draw actual wafer coordinate maps
                    if cb_range:
                        WaferMap.main(
                            (str(col_name) == "Peak wavelength (nm)"), map_dict, fig_map, ax, title_str, 
                            wafer_name=wafer, colorbar=cb_range, is_loss=(g_type == "loss")
                        )
                    else:
                        WaferMap.main(
                            (str(col_name) == "Peak wavelength (nm)"), map_dict, fig_map, ax, title_str, 
                            wafer_name=wafer, is_loss=(g_type == "loss")
                        )
                    
                    # Offset titles gracefully based on column count to prevent label overlapping
                    if valid_maps_count == 1:
                        title_str = f"Wafer: {wafer} , TO: {w_tapeout} | Fab: {w_fab}"
                        ax.set_title(title_str, y=1)
                    elif valid_maps_count == 2:
                        ax.set_title(title_str, y=0.88)
                    elif valid_maps_count == 3:
                        ax.set_title(title_str, y=0.82)
                    elif valid_maps_count == 4:
                        ax.set_title(title_str, y=0.75)
                    else:
                        ax.set_title(title_str, y=0.86)
                except Exception as map_err:
                    ax.set_title(f"Error on {wafer}")
                map_idx += 1

        # Delete any remaining empty subplot axes from grid
        for empty_idx in range(map_idx, len(axes_map_flat)):
            fig_map.delaxes(axes_map_flat[empty_idx])

        fig_map.tight_layout()
        safe_gt = str(g_key).replace(" ", "_").replace("(", "").replace(")", "").replace("@", "at").replace("/", "_").replace("°", "")
        map_file = os.path.join(
            target_dir, 
            f"Regrouped_WaferMaps_{safe_gt}_{selected_wave}nm.png" if g_type == "loss" else f"Regrouped_WaferMaps_{safe_gt}.png"
        )
        fig_map.savefig(map_file, dpi=300)
        plt.close(fig_map)
        generated_files.append(map_file)

        # --- BOXPLOTS UNIFIED AXIS ---
        fig_box, ax_box = plt.subplots(figsize=(dynamic_width, dynamic_height))
        title_box = f"Regrouped Distribution Boxplots - {g_label}" + (f" at {selected_wave} nm" if g_type == "loss" else "")
        fig_box.suptitle(title_box, fontsize=12, weight="bold")
        
        boxplot_data = []
        boxplot_labels = []
        spec_lines_to_draw = []
        
        ymin_global, ymax_global = None, None
        current_pos = 1

        for item in group["items"]:
            lk = item["key"]
            col_name = item["col"]
            
            if item["ymin"] is not None: ymin_global = item["ymin"]
            if item["ymax"] is not None: ymax_global = item["ymax"]
            
            for wafer in wafers_sorted:
                df_l = group_dfs[lk].get(wafer, pd.DataFrame())
                if not df_l.empty:
                    vals = pd.to_numeric(df_l[col_name], errors="coerce").dropna().values
                    if len(vals) > 0:
                        if str(col_name) == "Peak wavelength (nm)":
                            vals_rounded = [round(v, 2) for v in vals]
                        else:
                            vals_rounded = [round_to_3_sig_figs(v) for v in vals]
                        boxplot_data.append(vals_rounded)
                        
                        w_info = wafers_db.get(wafer, {})
                        w_tapeout = w_info.get("tapeout", "Unknown")
                        w_fab = w_info.get("Fab_IIIV", "Unknown")
                        
                        if g_type == "laser":
                            p_labels = []
                            if item.get("laser_name"): p_labels.append(f"L:{item['laser_name']}\n")
                            if item.get("temperature") and item["temperature"] != "Aucune": p_labels.append(f"{item['temperature']}°C")
                            if item.get("current") and item["current"] != "Aucune": p_labels.append(f"{item['current']}mA")
                            lbl = f"{wafer}\n{' '.join(p_labels)}\n({w_tapeout} | {w_fab})"
                        else:
                            if num_items > 1:
                                lbl = f"{wafer}\nLaser: {item['laser_name']}\n({w_tapeout} | {w_fab})"
                            else:
                                lbl = f"{wafer}\n({w_tapeout} | {w_fab})"
                        boxplot_labels.append(lbl)
                        
                        if item["spec"] is not None:
                            spec_lines_to_draw.append((current_pos, item["spec"]))
                        current_pos += 1

        if boxplot_data:
            positions = np.arange(1, len(boxplot_data) + 1)
            bp = ax_box.boxplot(boxplot_data, positions=positions, tick_labels=boxplot_labels, showfliers=False, patch_artist=True)

            # Style boxplots background
            for box in bp["boxes"]:
                box.set(facecolor="lightgray", alpha=0.7)

            # Scatter data overlay (jittered strip plot representation)
            for pos, values in zip(positions, boxplot_data):
                x_jitter = np.random.normal(pos, 0.06, size=len(values))
                ax_box.scatter(x_jitter, values, s=25, alpha=0.75, edgecolors="none")

            # Offset alternate bottom x-axis labels if density of ticks is high
            if g_type == "laser" and len(boxplot_labels) >= 6:
                for i, label in enumerate(ax_box.get_xticklabels()):
                    if i % 2 == 1:
                        label.set_y(label.get_position()[1] - 0.06)

            # Draw upper/lower operational product specification boundaries
            if spec_lines_to_draw:
                all_s_vals = [s[1] for s in spec_lines_to_draw]
                if len(set(str(v) for v in all_s_vals)) == 1:
                    s_val = all_s_vals[0]
                    if isinstance(s_val, (int, float)):
                        ax_box.axhline(s_val, color="red", linestyle="--", linewidth=1.5, label=f"Spec ({s_val})")
                    elif isinstance(s_val, (tuple, list)) and len(s_val) == 2:
                        ax_box.axhspan(s_val[0], s_val[1], color="red", alpha=0.12, label="Spec range")
                    ax_box.legend(loc='upper right')
                else:
                    for pos, s_val in spec_lines_to_draw:
                        if isinstance(s_val, (int, float)):
                            ax_box.hlines(s_val, pos - 0.4, pos + 0.4, colors="red", linestyles="--", linewidth=2)
                        elif isinstance(s_val, (tuple, list)) and len(s_val) == 2:
                            ax_box.axhspan(s_val[0], s_val[1], xmin=(pos-0.4)/current_pos, xmax=(pos+0.4)/current_pos, color="red", alpha=0.12)

            ax_box.set_ylabel(g_label if num_items == 1 else "Measured Parameter Values", fontsize=11)
            ax_box.set_xlabel("Wafer Lot / Configuration Matrix", fontsize=11)
            ax_box.grid(axis="y", linestyle="--", alpha=0.5)
            ax_box.grid(axis="x", linestyle="--", alpha=0.5)

            if ymin_global is not None or ymax_global is not None:
                ax_box.set_ylim(
                    bottom=ymin_global if ymin_global is not None else ax_box.get_ylim()[0],
                    top=ymax_global if ymax_global is not None else ax_box.get_ylim()[1]
                )

            fig_box.tight_layout()
            box_file = os.path.join(
                target_dir, 
                f"Regrouped_Boxplots_{safe_gt}_{selected_wave}nm.png" if g_type == "loss" else f"Regrouped_Boxplots_{safe_gt}.png"
            )
            fig_box.savefig(box_file, dpi=300)
            plt.close(fig_box)
            generated_files.append(box_file)

    return generated_files


def main_pipeline(tapeout, fab_filter, filter_mode, wavelength, plot_choices, save_plots, screen_w, screen_h, yaml_path, root_data):
    """
    Initializes metadata parsing and fires the core calculation execution pipeline.

    Args:
        tapeout (list): List of selected tapeout criteria.
        fab_filter (list): List of selected manufacturing fabs.
        filter_mode (str): Active selection filter mode constraint.
        wavelength (str): Current active operational optical wavelength selection.
        plot_choices (dict): Configured GUI extraction parameters workspace state.
        save_plots (bool): Directory destination storage toggler state.
        screen_w (int): Window widths context metric.
        screen_h (int): Window heights context metric.
        yaml_path (str): Filepath of the YAML wafer database.
        root_data (str): Wafer directories root directory.

    Returns:
        list: Filepaths of all generated export outputs.
    """
    if not os.path.exists(yaml_path):
        raise FileNotFoundError(f"Database 'wafer_list.yaml' missing at {yaml_path}")
        
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
    wafers_db = data.get("wafers", {})

    matched_wafers = plot_choices.get("selected_wafers", [])
    if not matched_wafers:
        return []

    return generate_regrouped_plots(root_data, matched_wafers, wavelength, plot_choices, save_plots, screen_w, screen_h, wafers_db)


def request_parameters():
    """
    Constructs, wires, and initiates the main Tkinter GUI desktop view interface. 
    Defines event-driven states, coordinate layouts, and dynamic checkbox listing displays.

    Returns:
        None
    """
    yaml_path = r"W:\50-DEVELOPMENT\TEST\Temporary data database\wafer_list.yaml"
    root_data = r"W:\50-DEVELOPMENT\TEST\Temporary data database\Data"
    
    wafers_db = {}
    unique_tapeouts = []
    unique_fabs = []
    
    # Load default wafer database if present
    if os.path.exists(yaml_path):
        try:
            with open(yaml_path, "r") as f:
                data = yaml.safe_load(f)
            wafers_db = data.get("wafers", {})
        except Exception:
            pass
        unique_tapeouts = sorted(list(set(str(w.get("tapeout")) for w in wafers_db.values() if w.get("tapeout") is not None)))
        unique_fabs = sorted(list(set(str(w.get("Fab_IIIV")) for w in wafers_db.values() if w.get("Fab_IIIV") is not None)))
        
    basket_laser_items = []
    basket_tlm_items = []
    laser_group_counter = [1]

    def choose_folder():
        """Prompts the user to select an export directory via GUI folder browser."""
        folder = filedialog.askdirectory()
        if folder:
            entry_folder.delete(0, tk.END)
            entry_folder.insert(0, folder)
            
    def on_filter_mode_changed(event=None):
        """Disables/Enables wafer lists selectively depending on active layout constraints."""
        mode = combobox_mode.get()
        if mode == "Tapeout":
            listbox_tapeout.config(state="normal")
            listbox_fab.config(state="disabled")
        elif mode == "Fab_IIIV":
            listbox_tapeout.config(state="disabled")
            listbox_fab.config(state="normal")
        else:
            listbox_tapeout.config(state="normal")
            listbox_fab.config(state="normal")
            
    def on_wafer_select(event=None):
        """Updates the selection count header display dynamically based on user selections."""
        selected_w = [listbox_matched_wafers.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_matched_wafers.curselection()]
        lbl_wafer_count.config(text=f"Wafers ({len(selected_w)}):")
        on_laser_col_select()
        
    def update_dynamic_choices(*args):
        """
        Dynamically filters, parses, and formats the wafer listbox choices, 
        TLM columns, and Laser columns based on the selected Tapeouts and Fabs.
        """
        mode = combobox_mode.get()
        t_sel = [listbox_tapeout.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_tapeout.curselection()]
        f_sel = [listbox_fab.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_fab.curselection()]
        
        # Determine wafers matching criteria subset
        matched = [k for k, w in wafers_db.items() if (
            (str(w.get("tapeout")) in t_sel if mode in ["Tapeout", "Both"] else True) and 
            (str(w.get("Fab_IIIV")) in f_sel if mode in ["Fab_IIIV", "Both"] else True)
        )]
        
        listbox_matched_wafers.delete(0, tk.END)
        for w in sorted(matched):
            listbox_matched_wafers.insert(tk.END, "☑ " + w)
        listbox_matched_wafers.selection_set(0, tk.END)
        lbl_wafer_count.config(text=f"Wafers ({len(matched)}):")

        tlm_cols, laser_cols = set(), set()
        
        # Inspect files on the shared network layout to extract actual metrics
        for wafer in matched:
            proc_dir = os.path.join(root_data, wafer, "Processing_results")
            
            # Read TLM columns
            tlm_fp = os.path.join(proc_dir, f"{wafer}_TLM_InPN_extraction.txt")
            if os.path.exists(tlm_fp):
                try:
                    df = pd.read_csv(tlm_fp, sep="\t")
                    exclude_tlm = ["Wafer name", "Die name", "Temperature (C)", "TLM name", "Test informations"]
                    for c in df.columns:
                        if c not in exclude_tlm: tlm_cols.add(c)
                except Exception: pass
                    
            # Read Laser columns
            laser_fp = os.path.join(proc_dir, f"{wafer}_DOE_laser_extraction.txt")
            if os.path.exists(laser_fp):
                try:
                    df = pd.read_csv(laser_fp, sep="\t")
                    exclude_laser = ["Wafer name", "Die name", "Laser name", "Shunt name", "Temperature (C)", "Current (mA)"]
                    for c in df.columns:
                        if c not in exclude_laser: laser_cols.add(c)
                except Exception: pass

        listbox_tlm.delete(0, tk.END)
        for c in sorted(list(tlm_cols)): listbox_tlm.insert(tk.END, c)
            
        listbox_laser_cols.delete(0, tk.END)
        for c in sorted(list(laser_cols)): listbox_laser_cols.insert(tk.END, c)
        
        listbox_laser_names.delete(0, tk.END)
        listbox_laser_temps.delete(0, tk.END)
        listbox_laser_currents.delete(0, tk.END)
        update_global_summary()

    def on_laser_col_select(event=None):
        """Populates available laser names based on selected wafer lots and test categories."""
        selected_indices = listbox_laser_cols.curselection()
        if not selected_indices: return
        selected_cols = [listbox_laser_cols.get(i) for i in selected_indices]
        
        matched = [listbox_matched_wafers.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_matched_wafers.curselection()]
        filtered_lasers = set()
        for wafer in matched:
            laser_fp = os.path.join(root_data, wafer, "Processing_results", f"{wafer}_DOE_laser_extraction.txt")
            if os.path.exists(laser_fp):
                try:
                    df = pd.read_csv(laser_fp, sep="\t")
                    for col in selected_cols:
                        if col in df.columns and "Laser name" in df.columns:
                            for val in df.dropna(subset=[col])["Laser name"].unique(): 
                                filtered_lasers.add(str(val))
                except Exception: pass

        listbox_laser_names.delete(0, tk.END)
        for n in sorted(list(filtered_lasers)): listbox_laser_names.insert(tk.END, "☐ " + n)
        listbox_laser_temps.delete(0, tk.END)
        listbox_laser_currents.delete(0, tk.END)

    def on_laser_name_select(event=None):
        """Populates available experimental temperatures based on chosen laser specifications."""
        col_idx = listbox_laser_cols.curselection()
        name_idx = listbox_laser_names.curselection()
        if not col_idx or not name_idx: return
        selected_cols = [listbox_laser_cols.get(i) for i in col_idx]
        selected_names = [listbox_laser_names.get(i).replace("☐ ","").replace("☑ ","") for i in name_idx]
        
        matched = [listbox_matched_wafers.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_matched_wafers.curselection()]
        filtered_temps = set()
        has_nan_temp = False
        
        for wafer in matched:
            laser_fp = os.path.join(root_data, wafer, "Processing_results", f"{wafer}_DOE_laser_extraction.txt")
            if os.path.exists(laser_fp):
                try:
                    df = pd.read_csv(laser_fp, sep="\t")
                    for col in selected_cols:
                        if col in df.columns and "Laser name" in df.columns:
                            df_f = df[df["Laser name"].astype(str).isin(selected_names)].dropna(subset=[col])
                            if "Temperature (C)" in df_f.columns:
                                for val in df_f["Temperature (C)"].unique():
                                    if pd.isna(val) or str(val).strip() == "": has_nan_temp = True
                                    else:
                                        try:
                                            f_val = float(val)
                                            filtered_temps.add(str(int(f_val)) if f_val.is_integer() else str(f_val))
                                        except ValueError: filtered_temps.add(str(val).strip())
                except Exception: pass
                    
        listbox_laser_temps.delete(0, tk.END)
        for t in sorted(list(filtered_temps)): listbox_laser_temps.insert(tk.END, "☐ " + t)
        if has_nan_temp: listbox_laser_temps.insert(tk.END, "☐ Aucune")
        listbox_laser_currents.delete(0, tk.END)

    def on_laser_temp_select(event=None):
        """Populates available test currents dynamically filtered by chosen laser and temperature selection."""
        col_idx = listbox_laser_cols.curselection()
        name_idx = listbox_laser_names.curselection()
        temp_idx = listbox_laser_temps.curselection()
        if not col_idx or not name_idx or not temp_idx: return
        
        selected_cols = [listbox_laser_cols.get(i) for i in col_idx]
        selected_names = [listbox_laser_names.get(i).replace("☐ ","").replace("☑ ","") for i in name_idx]
        selected_temps = [listbox_laser_temps.get(i).replace("☐ ","").replace("☑ ","") for i in temp_idx]

        matched = [listbox_matched_wafers.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_matched_wafers.curselection()]
        filtered_currents = set()
        has_nan_curr = False
        
        for wafer in matched:
            laser_fp = os.path.join(root_data, wafer, "Processing_results", f"{wafer}_DOE_laser_extraction.txt")
            if os.path.exists(laser_fp):
                try:
                    df = pd.read_csv(laser_fp, sep="\t")
                    for col in selected_cols:
                        if col in df.columns and "Laser name" in df.columns:
                            df_f = df[df["Laser name"].astype(str).isin(selected_names)].dropna(subset=[col])
                            if "Temperature (C)" in df_f.columns:
                                if "Aucune" in selected_temps:
                                    df_f = df_f[df_f["Temperature (C)"].isna() | (df_f["Temperature (C)"].astype(str).str.strip() == "")]
                                else:
                                    float_temps = [float(t) for t in selected_temps if t != "Aucune"]
                                    df_f = df_f[pd.to_numeric(df_f["Temperature (C)"].astype(str), errors='coerce').isin(float_temps)]
                            
                            if "Current (mA)" in df_f.columns:
                                for val in df_f["Current (mA)"].unique():
                                    if pd.isna(val) or str(val).strip() == "": has_nan_curr = True
                                    else:
                                        try:
                                            f_val = float(val)
                                            filtered_currents.add(str(int(f_val)) if f_val.is_integer() else str(f_val))
                                        except ValueError: filtered_currents.add(str(val).strip())
                except Exception: pass
                    
        listbox_laser_currents.delete(0, tk.END)
        for curr in sorted(list(filtered_currents), key=float): listbox_laser_currents.insert(tk.END, "☐ " + curr)
        if has_nan_curr: listbox_laser_currents.insert(tk.END, "☐ Aucune")

    def add_to_tlm_basket():
        """Saves configured TLM metrics and bounds inside the queue processing array."""
        idx = listbox_tlm.curselection()
        if not idx:
            messagebox.showwarning("Selection Missing", "Please choose a TLM column metric from the list browser.")
            return
        col = listbox_tlm.get(idx[0])
        
        def parse_v(val): return float(val.strip()) if val.strip() else None
        def parse_s(val):
            raw = val.strip()
            if not raw: return None
            return tuple(float(x) for x in raw.split(",")) if "," in raw else float(raw)
            
        try:
            item_data = {
                "col": col, "spec": parse_s(entry_tlm_spec.get()),
                "ymin": parse_v(entry_tlm_ymin.get()), "ymax": parse_v(entry_tlm_ymax.get()),
                "cbmin": parse_v(entry_tlm_cbmin.get()), "cbmax": parse_v(entry_tlm_cbmax.get())
            }
        except ValueError:
            messagebox.showerror("Error", "TLM limit coordinates criteria entries must be strictly numeric.")
            return
            
        lbl = f"TLM Canvas Grid -> {col} (Spec: {entry_tlm_spec.get() or 'None'} | Y: {entry_tlm_ymin.get() or 'Auto'}:{entry_tlm_ymax.get() or 'Auto'})"
        item_data["label_display"] = lbl
        basket_tlm_items.append(item_data)
        listbox_tlm_summary.insert(tk.END, lbl)
        
        # Reset entry parameters input fields
        entry_tlm_spec.delete(0, tk.END); entry_tlm_ymin.delete(0, tk.END); entry_tlm_ymax.delete(0, tk.END)
        entry_tlm_cbmin.delete(0, tk.END); entry_tlm_cbmax.delete(0, tk.END)
        update_global_summary()

    def remove_from_tlm_basket():
        """Deletes targeted configurations selectively from the TLM workspace queue."""
        idx = listbox_tlm_summary.curselection()
        if not idx: return
        for i in reversed(idx):
            listbox_tlm_summary.delete(i)
            basket_tlm_items.pop(i)
        update_global_summary()

    def add_to_laser_basket():
        """Appends active configured parameters into the processing Queue."""
        col_idx = listbox_laser_cols.curselection()
        name_idx = listbox_laser_names.curselection()
        temp_idx = listbox_laser_temps.curselection()
        curr_idx = listbox_laser_currents.curselection()
        
        if not col_idx or not name_idx or not temp_idx or not curr_idx:
            messagebox.showwarning("Incomplete Configuration", "Please select at least 1 Measure, 1 Laser Name, 1 Temperature, and 1 Current.")
            return

        selected_cols = [listbox_laser_cols.get(i) for i in col_idx]
        selected_names = [listbox_laser_names.get(i).replace("☐ ","").replace("☑ ","") for i in name_idx]
        selected_temps = [listbox_laser_temps.get(i).replace("☐ ","").replace("☑ ","") for i in temp_idx]
        selected_currs = [listbox_laser_currents.get(i).replace("☐ ","").replace("☑ ","") for i in curr_idx]
        
        fig_mode = var_laser_fig_mode.get()

        def parse_v(val): return float(val.strip()) if val.strip() else None
        def parse_s(val):
            raw = val.strip()
            if not raw: return None
            return tuple(float(x) for x in raw.split(",")) if "," in raw else float(raw)

        try:
            spec_val = parse_s(entry_laser_spec.get())
            ymin_val = parse_v(entry_laser_ymin.get())
            ymax_val = parse_v(entry_laser_ymax.get())
            cbmin_val = parse_v(entry_laser_cbmin.get())
            cbmax_val = parse_v(entry_laser_cbmax.get())
        except ValueError:
            messagebox.showerror("Error", "Laser threshold limits parameters must be structural floats.")
            return

        # Explode combinations sequentially inside list configurations arrays
        for col in selected_cols:
            for name in selected_names:
                for temp in selected_temps:
                    for curr in selected_currs:
                        if fig_mode == "new" and len(basket_laser_items) > 0:
                            laser_group_counter[0] += 1

                        parts = []
                        if temp != "Aucune": parts.append(f"{temp}°C")
                        if curr != "Aucune": parts.append(f"{curr}mA")
                        cond_str = f" ({', '.join(parts)})" if parts else ""
                        
                        lbl_text = f"[Fig {laser_group_counter[0]}] [{name}] {col}{cond_str} (Spec: {entry_laser_spec.get() or 'None'})"
                        
                        basket_laser_items.append({
                            "col": col, "laser_name": name, "temperature": temp, "current": curr,
                            "label_display": lbl_text, "group_id": laser_group_counter[0],
                            "spec": spec_val, "ymin": ymin_val, "ymax": ymax_val, "cbmin": cbmin_val, "cbmax": cbmax_val
                        })
                        listbox_summary.insert(tk.END, lbl_text)
        
        # Reset input coordinates fields
        entry_laser_spec.delete(0, tk.END); entry_laser_ymin.delete(0, tk.END); entry_laser_ymax.delete(0, tk.END)
        entry_laser_cbmin.delete(0, tk.END); entry_laser_cbmax.delete(0, tk.END)
        update_global_summary()

    def remove_from_laser_basket():
        """Removes the selected configuration item from the laser summary list box."""
        selected_indices = listbox_summary.curselection()
        if not selected_indices: return
        for idx in reversed(selected_indices):
            listbox_summary.delete(idx)
            basket_laser_items.pop(idx)
        update_global_summary()
        
    def clear_laser_basket():
        """Clears all configured figures out of the active Laser queue list."""
        listbox_summary.delete(0, tk.END)
        basket_laser_items.clear()
        laser_group_counter[0] = 1  # Reset canvas index counter
        update_global_summary()

    def update_global_summary(*args):
        """Displays real-time analysis details within the synchronized global layout panel."""
        summary_txt = ""
        losses = []
        if var_p1.get(): losses.append("NWG")
        if var_p2.get(): losses.append("RWG")
        if var_p3.get(): losses.append("SWG")
        summary_txt += f"Waveguide Losses ({entry_wave.get()} nm): {', '.join(losses) if losses else 'None selected'}\n"
        summary_txt += f"TLM Figures: {len(basket_tlm_items)} plot graphs selected.\n"
        summary_txt += f"Lasers: {len(basket_laser_items)} figures selected."
        lbl_global_summary.config(text=summary_txt)

    def start_processing(tapeout, fab_filter, filter_mode, wavelength, plot_choices, save_plots, screen_w, screen_h, display_plots):
        """Launches the core processing pipeline safely inside an independent worker daemon Thread."""
        def run():
            try:
                files = main_pipeline(
                    tapeout, fab_filter, filter_mode, wavelength, 
                    plot_choices, save_plots, screen_w, screen_h, yaml_path, root_data
                )
                root.after(0, lambda: finish_processing(files, display_plots, tapeout))
            except Exception as e:
                root.after(0, lambda ex=e: error_handler(ex))
        threading.Thread(target=run, daemon=True).start()

    def error_handler(error):
        """Fires and displays processing exceptions safely inside user-friendly message boxes."""
        progress.stop()
        progress.grid_forget()
        btn_run.config(state="normal")
        messagebox.showerror("Critical Error", f"An error occurred during calculation processing:\n{error}")

    def validate(scope="global"):
        """Validates all input constraints and kicks off the background calculation thread."""
        saving_file = entry_folder.get().strip()
        filter_mode = combobox_mode.get()
        
        tapeout = [listbox_tapeout.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_tapeout.curselection()]
        fab_filter = [listbox_fab.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_fab.curselection()]
        selected_w = [listbox_matched_wafers.get(i).replace("☐ ","").replace("☑ ","") for i in listbox_matched_wafers.curselection()]
        
        if not selected_w:
            messagebox.showerror("Error", "Please select at least one wafer from the list browser.")
            return
            
        wavelength = entry_wave.get().strip()
        display_plots = var_display.get()
        save_plots = var_save.get()
        
        if not display_plots and not save_plots:
            messagebox.showerror("Error", "At least one display image pipeline or file storage mechanism must be active.")
            return

        # Context evaluation depending on targeted execution scope
        if scope == "global" and not (var_p1.get() or var_p2.get() or var_p3.get() or basket_tlm_items or basket_laser_items):
            messagebox.showerror("Error", "No operations configured inside your active workspace basket layers.")
            return
        elif scope == "loss" and not (var_p1.get() or var_p2.get() or var_p3.get()):
            messagebox.showerror("Error", "No loss target parameters chosen for standalone parsing execution.")
            return
        elif scope == "tlm" and not basket_tlm_items:
            messagebox.showerror("Error", "The active TLM figure request bundle contains zero records.")
            return
        elif scope == "laser" and not basket_laser_items:
            messagebox.showerror("Error", "The specific laser rendering execution pipeline workspace holds no elements.")
            return

        def parse_v(val): return float(val.strip()) if val.strip() else None
        def parse_s(val):
            raw = val.strip()
            if not raw: return None
            return tuple(float(x) for x in raw.split(",")) if "," in raw else float(raw)

        try:
            loss_configs = {
                "NWG": {"spec": parse_s(entry_nwg_spec.get()), "ymin": parse_v(entry_nwg_ymin.get()), "ymax": parse_v(entry_nwg_ymax.get()), "cbmin": parse_v(entry_nwg_cbmin.get()), "cbmax": parse_v(entry_nwg_cbmax.get())},
                "RWG": {"spec": parse_s(entry_rwg_spec.get()), "ymin": parse_v(entry_rwg_ymin.get()), "ymax": parse_v(entry_rwg_ymax.get()), "cbmin": parse_v(entry_rwg_cbmin.get()), "cbmax": parse_v(entry_rwg_cbmax.get())},
                "SWG": {"spec": parse_s(entry_swg_spec.get()), "ymin": parse_v(entry_swg_ymin.get()), "ymax": parse_v(entry_swg_ymax.get()), "cbmin": parse_v(entry_swg_cbmin.get()), "cbmax": parse_v(entry_swg_cbmax.get())}
            }
        except ValueError:
            messagebox.showerror("Error", "Loss configuration constraints table cells must hold numerical expressions.")
            return

        plot_choices = {
            "nwg": var_p1.get() if scope in ["global", "loss"] else False,
            "rwg": var_p2.get() if scope in ["global", "loss"] else False,
            "swg": var_p3.get() if scope in ["global", "loss"] else False,
            "loss_configs": loss_configs,
            "dynamic_tlm": basket_tlm_items if scope in ["global", "tlm"] else [],
            "dynamic_laser_items": basket_laser_items if scope in ["global", "laser"] else [],
            "saving_path": saving_file,
            "selected_wafers": selected_w
        }

        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()

        btn_run.config(state="disabled")
        progress.grid(row=12, column=1, pady=3)
        progress.start()

        root.after(100, lambda: start_processing(
            tapeout, fab_filter, filter_mode, wavelength, 
            plot_choices, save_plots, screen_w, screen_h, display_plots
        ))

    def finish_processing(files, display_plots, tapeout):
        """Displays completion notification alerts and initiates image window previews."""
        progress.stop()
        progress.grid_forget()
        btn_run.config(state="normal")
        
        if not files:
            messagebox.showwarning("No Data Matched", "No sorted wafer records found or matching dataset contained no valid test metrics.")
            return
            
        messagebox.showinfo("Success", "Regrouped extraction plot figures built successfully!")
        if display_plots:
            for f in files: display_image(root, f)

    def setup_checkbox_listbox(lb, callback=None):
        """
        Custom helper that formats listbox widget selections into persistent 
        simulated checkbox structures (using '☑' and '☐' text prefixes).
        """
        lb.config(selectbackground=lb.cget('bg'), selectforeground=lb.cget('fg'), activestyle='none')
        
        def _on_select(event):
            y = lb.yview()
            selections = set(lb.curselection())
            
            lb.unbind("<<ListboxSelect>>")
            for i in range(lb.size()):
                txt = lb.get(i)
                clean = txt.replace("☐ ", "").replace("☑ ", "")
                expected = ("☑ " if i in selections else "☐ ") + clean
                    
                if txt != expected:
                    lb.unbind("<<ListboxSelect>>")
                    lb.delete(i)
                    lb.insert(i, expected)
                    if i in selections:
                        lb.selection_set(i)
                        
            lb.yview_moveto(y[0])
            lb.bind("<<ListboxSelect>>", _on_select)
            
            if callback:
                callback()
                
        lb.bind("<<ListboxSelect>>", _on_select)

    def toggle_listbox(lb, callback=None):
        """Selects or clears all elements inside a checkbox-style Listbox."""
        y = lb.yview()
        if lb.curselection():
            lb.selection_clear(0, tk.END)
        else:
            lb.selection_set(0, tk.END)
        
        selections = set(lb.curselection())
        items = []
        for i in range(lb.size()):
            txt = lb.get(i)
            clean = txt.replace("☐ ", "").replace("☑ ", "")
            items.append(clean)
        
        lb.delete(0, tk.END)
        for i, item in enumerate(items):
            prefix = "☑ " if i in selections else "☐ "
            lb.insert(tk.END, prefix + item)
        
        for i in selections:
            lb.selection_set(i)
            
        lb.yview_moveto(y[0])
        if callback:
            callback()

    # ---- MAIN APP DESIGN ASSEMBLY WINDOW (RESPONSIVE) ----
    root = tk.Tk()
    root.title("Characterization Plot Board - Scintil Photonics")
    root.geometry("1450x750") 
    root.configure(padx=12, pady=5)
    
    # Configure grid scaling weights
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(6, weight=1) 

    style = ttk.Style()
    style.theme_use('clam')

    desc_text = (
        "Application Description: Filters wafer lots from database config matching selected attributes. "
        "Aggregates metrics cleanly into aligned matrix subplots with independent scaling metrics parameters rules mapping."
    )
    lbl_desc = tk.Label(root, text=desc_text, justify="left", fg="#333333", bg="#f5f5f5", bd=1, relief="solid", padx=8, pady=4, font=("Arial", 9))
    lbl_desc.grid(row=0, column=0, columnspan=3, pady=(0, 4), sticky="ew")

    f_upper = tk.Frame(root)
    f_upper.grid(row=1, column=0, columnspan=3, sticky="w", pady=2)
    
    # Storage and filter directories inputs
    tk.Label(f_upper, text="Saving Folder:", font=("Arial", 9, "bold")).grid(row=0, column=0, padx=2, sticky="w")
    entry_folder = tk.Entry(f_upper, width=30, font=("Arial", 9))
    entry_folder.grid(row=0, column=1, padx=4)
    tk.Button(f_upper, text="Browse...", command=choose_folder, font=("Arial", 8)).grid(row=0, column=2, padx=2)

    tk.Label(f_upper, text="   Mode:", font=("Arial", 9, "bold")).grid(row=0, column=3, padx=2)
    combobox_mode = ttk.Combobox(f_upper, values=["Tapeout", "Fab_IIIV", "Both"], width=10, state="readonly", font=("Arial", 9))
    combobox_mode.set("Tapeout"); combobox_mode.grid(row=0, column=4, padx=2)

    tk.Label(f_upper, text="   Tapeout:", font=("Arial", 9, "bold")).grid(row=0, column=5, padx=2)
    listbox_tapeout = tk.Listbox(f_upper, width=12, height=6, selectmode="multiple", exportselection=False, font=("Arial", 9))
    for idx, t in enumerate(unique_tapeouts):
        prefix = "☑ " if idx == 5 else "☐ "
        listbox_tapeout.insert(tk.END, prefix + t)
    if unique_tapeouts:
        listbox_tapeout.select_set(5)
    listbox_tapeout.grid(row=0, column=6, padx=2, sticky="w")

    tk.Label(f_upper, text="   Fab:", font=("Arial", 9, "bold")).grid(row=0, column=7, padx=2)
    listbox_fab = tk.Listbox(f_upper, width=12, height=3, selectmode="multiple", exportselection=False, font=("Arial", 9))
    for idx, f in enumerate(unique_fabs):
        prefix = "☑ " if idx == 0 else "☐ "
        listbox_fab.insert(tk.END, prefix + f)
    if unique_fabs:
        listbox_fab.select_set(0)
    listbox_fab.grid(row=0, column=8, padx=2, sticky="w")

    lbl_wafer_count = tk.Label(f_upper, text="Wafers (0):", font=("Arial", 9, "bold"))
    lbl_wafer_count.grid(row=0, column=9, padx=(15, 2), sticky="w")
    
    f_matched_wafers = tk.Frame(f_upper)
    f_matched_wafers.grid(row=0, column=10, padx=2, sticky="w")
    sb_matched = tk.Scrollbar(f_matched_wafers, orient="vertical")
    
    listbox_matched_wafers = tk.Listbox(
        f_matched_wafers, width=45, height=8, selectmode="multiple", 
        yscrollcommand=sb_matched.set, font=("Arial", 9), fg="#2c3e50"
    )
    sb_matched.config(command=listbox_matched_wafers.yview)
    sb_matched.pack(side="right", fill="y")
    listbox_matched_wafers.pack(side="left", fill="both")

    btn_select_all = tk.Button(f_upper, text="All/None", font=("Arial", 8), command=lambda: toggle_listbox(listbox_matched_wafers, on_wafer_select))
    btn_select_all.grid(row=0, column=11, padx=2, sticky="w")

    notebook = ttk.Notebook(root)
    notebook.grid(row=6, column=0, columnspan=3, pady=6, sticky="nsew")

    tab_loss = ttk.Frame(notebook, padding=5)
    tab_tlm = ttk.Frame(notebook, padding=5)
    tab_laser = ttk.Frame(notebook, padding=5)

    notebook.add(tab_loss, text=" Waveguide Loss (NWG/RWG/SWG) ")
    notebook.add(tab_tlm, text=" TLM Measurements ")
    notebook.add(tab_laser, text=" Laser Configurations ")

    # ==========================================
    # TAB 1: WAVEGUIDE LOSS
    # ==========================================
    frame_wave_block = tk.Frame(tab_loss)
    frame_wave_block.pack(anchor="w", pady=2)
    tk.Label(frame_wave_block, text="Wavelength (nm):", font=("Arial", 9, "bold")).pack(side="left", padx=2)
    entry_wave = tk.Entry(frame_wave_block, width=12, font=("Arial", 9)); entry_wave.insert(0, "1310"); entry_wave.pack(side="left", padx=4)
    entry_wave.bind("<KeyRelease>", update_global_summary)

    frame_loss_tbl = tk.Frame(tab_loss, pady=2)
    frame_loss_tbl.pack(fill="x")

    var_p1, var_p2, var_p3 = tk.BooleanVar(value=False), tk.BooleanVar(value=False), tk.BooleanVar(value=False)
    headers_loss = ["Structure", "Analyze?", "Spec Limit", "Boxplot Y Min", "Boxplot Y Max", "Wafermap CB Min", "Wafermap CB Max"]
    for idx, h in enumerate(headers_loss):
        frame_loss_tbl.grid_columnconfigure(idx, weight=1)
        tk.Label(frame_loss_tbl, text=h, font=("Arial", 9, "bold")).grid(row=0, column=idx, padx=5, pady=2, sticky="w" if idx==0 else "")

    rows_loss = [("NWG Loss:", var_p1, "#1f77b4"), ("RWG Loss:", var_p2, "#ff7f0e"), ("SWG Loss:", var_p3, "#2ca02c")]
    entries_loss_refs = []
    for r_idx, (name, var, col) in enumerate(rows_loss, start=1):
        tk.Label(frame_loss_tbl, text=name, font=("Arial", 9, "bold"), fg=col).grid(row=r_idx, column=0, padx=5, pady=2, sticky="w")
        tk.Checkbutton(frame_loss_tbl, variable=var, command=update_global_summary).grid(row=r_idx, column=1, pady=2)
        e_spec = tk.Entry(frame_loss_tbl, width=10, font=("Arial", 9)); e_spec.grid(row=r_idx, column=2, padx=4, sticky="ew")
        e_ymin = tk.Entry(frame_loss_tbl, width=10, font=("Arial", 9)); e_ymin.grid(row=r_idx, column=3, padx=4, sticky="ew")
        e_ymax = tk.Entry(frame_loss_tbl, width=10, font=("Arial", 9)); e_ymax.grid(row=r_idx, column=4, padx=4, sticky="ew")
        e_cmin = tk.Entry(frame_loss_tbl, width=12, font=("Arial", 9)); e_cmin.grid(row=r_idx, column=5, padx=4, sticky="ew")
        e_cmax = tk.Entry(frame_loss_tbl, width=12, font=("Arial", 9)); e_cmax.grid(row=r_idx, column=6, padx=4, sticky="ew")
        entries_loss_refs.append((e_spec, e_ymin, e_ymax, e_cmin, e_cmax))
    
    entry_nwg_spec, entry_nwg_ymin, entry_nwg_ymax, entry_nwg_cbmin, entry_nwg_cbmax = entries_loss_refs[0]
    entry_rwg_spec, entry_rwg_ymin, entry_rwg_ymax, entry_rwg_cbmin, entry_rwg_cbmax = entries_loss_refs[1]
    entry_swg_spec, entry_swg_ymin, entry_swg_ymax, entry_swg_cbmin, entry_swg_cbmax = entries_loss_refs[2]

    tk.Label(tab_loss, text="* Spec Format: enter float (e.g. -7) or range (e.g. -10,-5)", font=("Arial", 8, "italic"), fg="gray").pack(anchor="w", padx=4)
    btn_run_loss = tk.Button(tab_loss, text="Run Waveguide Loss Only", bg="#34495e", fg="white", font=("Arial", 9, "bold"), command=lambda: validate("loss"))
    btn_run_loss.pack(anchor="e", pady=2)

    # ==========================================
    # TAB 2: TLM MEASUREMENTS
    # ==========================================
    frame_tlm_engine = tk.Frame(tab_tlm)
    frame_tlm_engine.pack(fill="both", expand=True)

    f_tlm_list = tk.LabelFrame(frame_tlm_engine, text=" Available Columns ", font=("Arial", 9, "bold"), padx=4, pady=2)
    f_tlm_list.pack(side="left", fill="both", expand=True, padx=2)
    sb_tlm = tk.Scrollbar(f_tlm_list, orient="vertical")
    listbox_tlm = tk.Listbox(f_tlm_list, selectmode="browse", exportselection=False, width=28, height=6, yscrollcommand=sb_tlm.set, font=("Arial", 9))
    sb_tlm.config(command=listbox_tlm.yview); sb_tlm.pack(side="right", fill="y"); listbox_tlm.pack(side="left", fill="both", expand=True)

    f_tlm_limits_inputs = tk.LabelFrame(frame_tlm_engine, text=" Limits Fixed Matrix for this Canvas ", font=("Arial", 9, "bold"), padx=6, pady=4)
    f_tlm_limits_inputs.pack(side="left", fill="y", padx=4)
    
    tk.Label(f_tlm_limits_inputs, text="Spec Limit:", font=("Arial", 8, "bold")).grid(row=0, column=0, sticky="w")
    entry_tlm_spec = tk.Entry(f_tlm_limits_inputs, width=12); entry_tlm_spec.grid(row=0, column=1, pady=2, padx=4)
    tk.Label(f_tlm_limits_inputs, text="* e.g. -7 or -10,-5", font=("Arial", 7, "italic"), fg="gray").grid(row=1, column=1, sticky="w")
    
    tk.Label(f_tlm_limits_inputs, text="Y Min / Max:", font=("Arial", 8, "bold")).grid(row=2, column=0, sticky="w")
    f_t_l_sub = tk.Frame(f_tlm_limits_inputs)
    f_t_l_sub.grid(row=2, column=1, pady=2)
    entry_tlm_ymin = tk.Entry(f_t_l_sub, width=6); entry_tlm_ymin.pack(side="left", padx=1)
    entry_tlm_ymax = tk.Entry(f_t_l_sub, width=6); entry_tlm_ymax.pack(side="left", padx=1)

    tk.Label(f_tlm_limits_inputs, text="CB Min / Max:", font=("Arial", 8, "bold")).grid(row=3, column=0, sticky="w")
    f_t_c_sub = tk.Frame(f_tlm_limits_inputs)
    f_t_c_sub.grid(row=3, column=1, pady=2)
    entry_tlm_cbmin = tk.Entry(f_t_c_sub, width=6); entry_tlm_cbmin.pack(side="left", padx=1)
    entry_tlm_cbmax = tk.Entry(f_t_c_sub, width=6); entry_tlm_cbmax.pack(side="left", padx=1)

    btn_add_tlm = tk.Button(f_tlm_limits_inputs, text="Add TLM\nConfig ➜", bg="#3498db", fg="white", font=("Arial", 8, "bold"), command=add_to_tlm_basket)
    btn_add_tlm.grid(row=4, column=0, columnspan=2, pady=4, sticky="ew")

    f_tlm_basket_view = tk.LabelFrame(frame_tlm_engine, text=" Registered TLM Figures ", font=("Arial", 9, "bold"), padx=4, pady=2)
    f_tlm_basket_view.pack(side="right", fill="both", expand=True, padx=2)
    sb_t_s = tk.Scrollbar(f_tlm_basket_view, orient="vertical")
    listbox_tlm_summary = tk.Listbox(
        f_tlm_basket_view, selectmode="extended", exportselection=False, 
        width=45, height=6, yscrollcommand=sb_t_s.set, font=("Arial", 9, "italic")
    )
    sb_t_s.config(command=listbox_tlm_summary.yview); sb_t_s.pack(side="right", fill="y"); listbox_tlm_summary.pack(side="left", fill="both", expand=True)
    tk.Button(f_tlm_basket_view, text="❌", bg="#c0392b", fg="white", font=("Arial", 8, "bold"), width=3, command=remove_from_tlm_basket).pack(side="right", padx=2)

    btn_run_tlm = tk.Button(tab_tlm, text="Run TLM Only", bg="#34495e", fg="white", font=("Arial", 9, "bold"), command=lambda: validate("tlm"))
    btn_run_tlm.pack(anchor="e", pady=2)

    # ==========================================
    # TAB 3: LASER CONFIGURATIONS
    # ==========================================
    tab_laser.grid_rowconfigure(0, weight=3) 
    tab_laser.grid_rowconfigure(1, weight=1) 
    tab_laser.grid_columnconfigure(0, weight=1)

    frame_laser_selection = tk.Frame(tab_laser)
    frame_laser_selection.grid(row=0, column=0, sticky="nsew", pady=1)
    for c_i in range(4): frame_laser_selection.grid_columnconfigure(c_i, weight=1)

    # Laser measure parameter columns browser
    f_las_cols = tk.Frame(frame_laser_selection)
    f_las_cols.grid(row=0, column=0, padx=2, sticky="nsew")
    tk.Label(f_las_cols, text="Measures", font=("Arial", 8, "bold")).pack()
    sb_las_cols = tk.Scrollbar(f_las_cols, orient="vertical")
    listbox_laser_cols = tk.Listbox(f_las_cols, selectmode="browse", exportselection=False, height=8, yscrollcommand=sb_las_cols.set, font=("Arial", 9))
    sb_las_cols.config(command=listbox_laser_cols.yview); sb_las_cols.pack(side="right", fill="y"); listbox_laser_cols.pack(side="left", fill="both", expand=True)

    # Laser structure layouts names
    f_las_names = tk.Frame(frame_laser_selection)
    f_las_names.grid(row=0, column=1, padx=2, sticky="nsew")
    tk.Label(f_las_names, text="Laser Names", font=("Arial", 8, "bold")).pack()
    btn_all_names = tk.Button(f_las_names, text="All/None", font=("Arial", 7), command=lambda: toggle_listbox(listbox_laser_names, on_laser_name_select))
    btn_all_names.pack(fill="x")
    sb_las_names = tk.Scrollbar(f_las_names, orient="vertical")
    listbox_laser_names = tk.Listbox(f_las_names, selectmode="multiple", exportselection=False, height=8, yscrollcommand=sb_las_names.set, font=("Arial", 9))
    sb_las_names.config(command=listbox_laser_names.yview); sb_las_names.pack(side="right", fill="y"); listbox_laser_names.pack(side="left", fill="both", expand=True)

    # Operational experimental temperatures
    f_las_temps = tk.Frame(frame_laser_selection)
    f_las_temps.grid(row=0, column=2, padx=2, sticky="nsew")
    tk.Label(f_las_temps, text="Temp (°C)", font=("Arial", 8, "bold")).pack()
    btn_all_temps = tk.Button(f_las_temps, text="All/None", font=("Arial", 7), command=lambda: toggle_listbox(listbox_laser_temps, on_laser_temp_select))
    btn_all_temps.pack(fill="x")
    sb_las_temps = tk.Scrollbar(f_las_temps, orient="vertical")
    listbox_laser_temps = tk.Listbox(f_las_temps, selectmode="multiple", exportselection=False, height=8, yscrollcommand=sb_las_temps.set, font=("Arial", 9))
    sb_las_temps.config(command=listbox_laser_temps.yview); sb_las_temps.pack(side="right", fill="y"); listbox_laser_temps.pack(side="left", fill="both", expand=True)

    # Biasing currents
    f_las_currs = tk.Frame(frame_laser_selection)
    f_las_currs.grid(row=0, column=3, padx=2, sticky="nsew")
    tk.Label(f_las_currs, text="Current (mA)", font=("Arial", 8, "bold")).pack()
    btn_all_currs = tk.Button(f_las_currs, text="All/None", font=("Arial", 7), command=lambda: toggle_listbox(listbox_laser_currents))
    btn_all_currs.pack(fill="x")
    sb_las_currs = tk.Scrollbar(f_las_currs, orient="vertical")
    listbox_laser_currents = tk.Listbox(f_las_currs, selectmode="multiple", exportselection=False, height=8, yscrollcommand=sb_las_currs.set, font=("Arial", 9))
    sb_las_currs.config(command=listbox_laser_currents.yview); sb_las_currs.pack(side="right", fill="y"); listbox_laser_currents.pack(side="left", fill="both", expand=True)

    f_las_inputs_panel = tk.LabelFrame(frame_laser_selection, text=" Limits Lock ", font=("Arial", 8, "bold"), padx=4)
    f_las_inputs_panel.grid(row=0, column=4, padx=5, sticky="nsew")
    
    tk.Label(f_las_inputs_panel, text="Spec Limit:", font=("Arial", 8)).grid(row=0, column=0, sticky="w")
    entry_laser_spec = tk.Entry(f_las_inputs_panel, width=12); entry_laser_spec.grid(row=0, column=1, pady=1)
    tk.Label(f_las_inputs_panel, text="* e.g. -7 or -10,-5", font=("Arial", 7, "italic"), fg="gray").grid(row=1, column=1, sticky="w")
    
    tk.Label(f_las_inputs_panel, text="Y Min/Max:", font=("Arial", 8)).grid(row=2, column=0, sticky="w")
    f_l_y_sub = tk.Frame(f_las_inputs_panel)
    f_l_y_sub.grid(row=2, column=1, pady=1)
    entry_laser_ymin = tk.Entry(f_l_y_sub, width=5); entry_laser_ymin.pack(side="left", padx=1)
    entry_laser_ymax = tk.Entry(f_l_y_sub, width=5); entry_laser_ymax.pack(side="left", padx=1)

    tk.Label(f_las_inputs_panel, text="CB Min/Max:", font=("Arial", 8)).grid(row=3, column=0, sticky="w")
    f_l_c_sub = tk.Frame(f_las_inputs_panel)
    f_l_c_sub.grid(row=3, column=1, pady=1)
    entry_laser_cbmin = tk.Entry(f_l_c_sub, width=5); entry_laser_cbmin.pack(side="left", padx=1)
    entry_laser_cbmax = tk.Entry(f_l_c_sub, width=5); entry_laser_cbmax.pack(side="left", padx=1)

    frame_placement = tk.LabelFrame(f_las_inputs_panel, text=" Placement ", font=("Arial", 8, "bold"), padx=4, pady=2)
    frame_placement.grid(row=4, column=0, columnspan=2, pady=4, sticky="ew")
    var_laser_fig_mode = tk.StringVar(value="new")
    tk.Radiobutton(frame_placement, text="New Canvas", variable=var_laser_fig_mode, value="new", font=("Arial", 8)).pack(anchor="w")
    tk.Radiobutton(frame_placement, text="Same Fig (Grouped)", variable=var_laser_fig_mode, value="same", font=("Arial", 8)).pack(anchor="w")

    btn_add_basket = tk.Button(f_las_inputs_panel, text="Add Laser\nConfig ➜", bg="#3498db", fg="white", font=("Arial", 8, "bold"), command=add_to_laser_basket)
    btn_add_basket.grid(row=5, column=0, columnspan=2, pady=4, sticky="ew")

    frame_summary_box = tk.LabelFrame(tab_laser, text=" Configured Laser Figure Buckets (Overview) ", font=("Arial", 9, "bold"), padx=4, pady=2)
    frame_summary_box.grid(row=1, column=0, sticky="nsew", pady=2)
    frame_summary_inner = tk.Frame(frame_summary_box)
    frame_summary_inner.pack(fill="both", expand=True)

    sb_summary = tk.Scrollbar(frame_summary_inner, orient="vertical")
    listbox_summary = tk.Listbox(
        frame_summary_inner, selectmode="extended", exportselection=False, 
        height=4, yscrollcommand=sb_summary.set, font=("Arial", 9, "italic"), fg="#2c3e50"
    )
    sb_summary.config(command=listbox_summary.yview); sb_summary.pack(side="right", fill="y"); listbox_summary.pack(side="left", fill="both", expand=True)
    tk.Button(frame_summary_inner, text="❌", bg="#c0392b", fg="white", font=("Arial", 9, "bold"), width=3, command=remove_from_laser_basket).pack(side="right", padx=4)
    tk.Button(frame_summary_inner, text="Clear All", bg="#e67e22", fg="white", font=("Arial", 9, "bold"), command=clear_laser_basket).pack(side="right", padx=4)
    btn_run_laser = tk.Button(tab_laser, text="Run Lasers Analysis Only", bg="#34495e", fg="white", font=("Arial", 9, "bold"), command=lambda: validate("laser"))
    btn_run_laser.grid(row=2, column=0, sticky="e", pady=1)

    # ==========================================
    # ALWAYS VISIBLE BOTTOM LAYOUT ENGINE
    # ==========================================
    lf_summary_panel = tk.LabelFrame(root, text=" Global Execution Selection Summary (Integrated Sync View) ", font=("Arial", 9, "bold"), padx=8, pady=4)
    lf_summary_panel.grid(row=7, column=0, columnspan=3, pady=2, sticky="ew")
    lbl_global_summary = tk.Label(lf_summary_panel, text="", justify="left", anchor="w", font=("Arial", 9, "italic"), fg="#2c3e50")
    lbl_global_summary.pack(fill="x")

    var_display, var_save = tk.BooleanVar(value=True), tk.BooleanVar(value=False)
    f_run_actions = tk.Frame(root)
    f_run_actions.grid(row=9, column=0, columnspan=3, pady=3, sticky="ew")
    
    chk_display = tk.Checkbutton(f_run_actions, text="Display plots on screen (Preview pop-up)", variable=var_display, font=("Arial", 9, "bold"), fg="#27ae60")
    chk_display.pack(side="left", padx=10)
    chk_save = tk.Checkbutton(f_run_actions, text="Save image files (.png) in folder", variable=var_save, font=("Arial", 9, "bold"), fg="#c0392b")
    chk_save.pack(side="left", padx=10)

    progress = ttk.Progressbar(root, mode="indeterminate", length=350)
    btn_run = tk.Button(
        root, text="Run Global Integrated Analysis (All Canvas Schedules)", bg="#2ecc71", fg="white",
        activebackground="#27ae60", activeforeground="white", font=("Arial", 10, "bold"), bd=2, relief="groove", command=lambda: validate("global")
    )
    btn_run.grid(row=11, column=0, columnspan=3, pady=4, sticky="ew")

    # Bind events
    combobox_mode.bind("<<ComboboxSelected>>", lambda e: [on_filter_mode_changed(), update_dynamic_choices()])

    # Apply checkbox decorators to multi-selection listboxes
    setup_checkbox_listbox(listbox_tapeout, update_dynamic_choices)
    setup_checkbox_listbox(listbox_fab, update_dynamic_choices)
    setup_checkbox_listbox(listbox_matched_wafers, on_wafer_select)
    setup_checkbox_listbox(listbox_laser_names, on_laser_name_select)
    setup_checkbox_listbox(listbox_laser_temps, on_laser_temp_select)
    setup_checkbox_listbox(listbox_laser_currents)
    
    # Classic simple select behavior for Measures column selection
    listbox_laser_cols.bind("<<ListboxSelect>>", on_laser_col_select)

    # Initialize view states
    on_filter_mode_changed()
    update_dynamic_choices()
    update_global_summary()
    
    root.mainloop()


if __name__ == "__main__":
    request_parameters()
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:50:33 2026

@author: kevin.froberger
Contact : kevin.froberger@scintil-photonics.com
All right reserved Scintil Photonics

Goal : 
Code that goes with the GUI to display boxplots of the different measures, with the possibility to add specs and to group by different parameters (wafer, tapeout, etc.)
"""

######################################
#   Packages
######################################
# To clear variable in Spyder :
import sys
from importlib.resources import path
from posixpath import sep
import re
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import yaml
import chardet
from pathlib import Path
import re
import textwrap


# Close all previous MPL figures


######################################
#   Functions
######################################


def load_wafer_files(filepaths, sep="\t"):
    """
    Charge plusieurs fichiers wafers et retourne un DataFrame concaténé.

    Parameters
    ----------
    filepaths : list of str
        Liste des chemins vers les fichiers.
    sep : str
        Séparateur des fichiers (par défaut tabulation).

    Returns
    -------
    pandas.DataFrame
    """
    

    dfs = []
    for path in filepaths:
        try:
            df = pd.read_csv(path, encoding="utf-8", sep=sep)
        except UnicodeDecodeError:
            df = pd.read_csv(path, encoding="cp1252", sep=sep)

        dfs.append(df)

    df_all = pd.concat(dfs, ignore_index=True)
    return df_all

def filter_measure_laser(
    df,
    measure_type,
    parameters,
    temperature=None,
    structure_name=None,
    wafer_name=None,
    die_name=None
):
    """
    Filtre les données selon une colonne de mesure et options supplémentaires.

    Parameters
    ----------
    df : pandas.DataFrame
    measure_type : str
        Nom de la colonne de mesure (ex: "Peak wavelength (nm)", "SMSR (dB)")
    temperature : float or int, optional
    structure_name : str, optional
    wafer_name : str, optional
    die_name : str, optional

    Returns
    -------
    pandas.DataFrame
    """

    if measure_type not in df.columns:
        raise ValueError(f"La colonne '{measure_type}' n'existe pas dans le DataFrame")

    
    
    
    mask = df.apply(
        lambda row: row.apply(lambda cell: any(p in str(cell) for p in parameters)).any(),
        axis=1
    )




    if temperature is not None:
        mask &= df["Temperature (°C)"] == temperature

    if structure_name is not None and "Structure name" in df.columns:
        mask &= df["Structure name"] == structure_name

    if wafer_name is not None:
        mask &= df["Wafer name"] == wafer_name

    if die_name is not None:
        mask &= df["Die name"] == die_name

    df_filt = df.loc[mask].copy()

    df_filt[measure_type] = pd.to_numeric(df_filt[measure_type], errors='coerce')

    return df_filt

def filter_measure(
    df,
    measure_type,
    temperature=None,
    structure_name=None
):
    """
    Filtre les données selon le type de mesure et options supplémentaires.

    Parameters
    ----------
    df : pandas.DataFrame
    measure_type : str
        Ex: "TLM, Rsheet, ohm.sq"
    temperature : float or int, optional
    structure_name : str, optional

    Returns
    -------
    pandas.DataFrame
    """
    mask = df["Type of result"] == measure_type

    if temperature is not None:
        mask &= df["Temperature (C)"] == temperature

    if structure_name is not None:
        mask &= df["Structure name"] == structure_name

    df_filt = df.loc[mask].copy()
    df_filt["Result"] = df_filt["Result"].astype(float)

    return df_filt



def prepare_boxplot_data(df, group_col="Wafer name", value_col="Result"):
    grouped = df.groupby(group_col, observed=True)

    data = []
    labels = []

    for name, group in grouped:
        values = pd.to_numeric(group[value_col], errors="coerce").dropna()

        if len(values) == 0:
            continue 

        data.append(values.values)
        labels.append(str(name))

    return data, labels




def plot_boxplot_with_points(
    data,
    labels,
    ylabel,
    title=None,
    jitter=0.08,
    logscale=False,
    spec=None,
    figsize=(8, 6),
    fontsize_labels=12,
    fontsize_ticks=10,
    fontsize_title=14,
    ymin=None,
    ymax=None
):
    """
    Trace un boxplot avec points individuels et specs optionnelles.

    spec formats:
    - None
    - float / int                  -> spec globale
    - (min, max)                   -> range global
    - dict {label: spec_value}     -> spec par wafer
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    positions = np.arange(1, len(data) + 1)

    # --- BOXPLOT ---
    bp = ax.boxplot(
        data,
        positions=positions,
        labels=labels,
        showfliers=False,
        patch_artist=True
    )

    for box in bp["boxes"]:
        box.set(facecolor="lightgray", alpha=0.7)

    # --- POINTS INDIVIDUELS ---
    for pos, values in zip(positions, data):
        x = np.random.normal(pos, jitter, size=len(values))
        ax.scatter(x, values, s=30, alpha=0.8)

    # --- SPECS ---
    if spec is not None:

        # ===== SPEC GLOBALE =====
        if isinstance(spec, (int, float)):
            ax.axhline(
                spec,
                color="red",
                linestyle="--",
                linewidth=2,
                label="Spec"
            )

        elif isinstance(spec, (tuple, list)) and len(spec) == 2:
            ax.axhspan(
                spec[0],
                spec[1],
                color="red",
                alpha=0.15,
                label="Spec range"
            )

        # ===== SPEC PAR WAFER =====
        elif isinstance(spec, dict):
            for pos, label in zip(positions, labels):

                if label not in spec:
                    continue

                wafer_spec = spec[label]

                # --- Valeur unique ---
                if isinstance(wafer_spec, (int, float)):
                    ax.hlines(
                        wafer_spec,
                        pos - 0.35,
                        pos + 0.35,
                        colors="red",
                        linestyles="--",
                        linewidth=2,
                        label='Spec'
                    )

                # --- Range ---
                elif isinstance(wafer_spec, (tuple, list)) and len(wafer_spec) == 2:
                    ax.fill_between(
                        [pos - 0.35, pos + 0.35],
                        wafer_spec[0],
                        wafer_spec[1],
                        color="red",
                        alpha=0.2,
                        label='Spec range'
                    )

                else:
                    raise ValueError(
                        f"Spec invalide pour le wafer {label}"
                    )

        else:
            raise ValueError(
                "spec doit être None, float, tuple(min,max) ou dict"
            )

    # --- AXES ---
    ax.set_ylabel(ylabel, fontsize=fontsize_labels)
    ax.tick_params(axis="x", labelsize=fontsize_ticks, rotation=45)
    ax.tick_params(axis="y", labelsize=fontsize_ticks)

    if spec:
        ax.legend(fontsize=fontsize_ticks)

    
    
    if title:
        wrapped_title = "\n".join(textwrap.wrap(title, width=50))
        ax.set_title(wrapped_title, fontsize=fontsize_title, pad=10)



    if logscale:
        ax.set_yscale("log")


    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.grid(axis="x", linestyle="--", alpha=0.5)
    
    if ymin is not None or ymax is not None:
        ax.set_ylim(
            bottom=ymin if ymin is not None else ax.get_ylim()[0],
            top=ymax if ymax is not None else ax.get_ylim()[1],
        )

    plt.tight_layout()


######################################




# extract_folder = r'C:/Users/pierre.cassagnettes/Documents/Temporary transfer to Pierre/Codes that already exists/Extracts'
# image_folder = r'C:/Users/pierre.cassagnettes/Documents/Temporary transfer to Pierre/Image_interface'


def get_resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)


def escape_matplotlib_text(text):
    if text is None:
        return text
    return str(text).replace("$", r"\$")

def main(parameters,measure,group,temp,folder,image_folder,y_min,y_max,wafer_list_yaml_path,spec_=None):
    #parameters = [parameter.strip() for parameter in parameters.strip("[]").split(",")]
    measure = str(measure)
    group = str(group)
    y_min = float(y_min) if y_min.lower() != "none" else None
    y_max = float(y_max) if y_max.lower() != "none" else None
    extract_folder = str(Path(folder))
    image_folder = str(Path(image_folder))


    measure_type = measure
    group_by = group
    temperature = None if temp.lower() == "none" else float(temp)


    if temperature is not None:
        fig_title = f'{escape_matplotlib_text(parameters)}, {escape_matplotlib_text(measure_type)}, {temperature}°C , grouped by {escape_matplotlib_text(group_by)}'
    else:
        fig_title = f'{escape_matplotlib_text(parameters)}, {escape_matplotlib_text(measure_type)}, grouped by {escape_matplotlib_text(group_by)}'
    y_label = escape_matplotlib_text(measure_type)
    image_filename = f'Boxplot_{escape_matplotlib_text(measure_type)}_{temperature}°C_{escape_matplotlib_text(group_by)}.png'


    ######################################
    #   YAML wafer list
    ######################################
    with open(wafer_list_yaml_path) as f:
        meta = yaml.safe_load(f)

    REQUIRED_FIELDS = {"tapeout", "wafer_scribe", "SiPho_lot", "SiPho_number", "Fab_IIIV", "IIIV_split", "epi"}

    # Checking for incorherence in the YMAL file
    if meta.get("version") != 1:
        raise ValueError(
            f"Unsupported metadata version: {meta.get('version')}"
        )
    for wafer_id, info in meta["wafers"].items():
        if not isinstance(info, dict):
            raise TypeError(f"Wafer {wafer_id} metadata is not a mapping")
        missing = REQUIRED_FIELDS - info.keys()
        if missing:
            raise ValueError(
                f"Wafer {wafer_id} missing fields: {missing}"
            )


    # Loading yaml data in a dataframe
    df_meta = (
        pd.DataFrame.from_dict(meta["wafers"], orient="index")
        .reset_index()
        .rename(columns={"index": "Wafer name"})
    )


    ######################################
    #   Full code itself
    ######################################
    files = [os.path.join(extract_folder, file) for file in os.listdir(extract_folder) if file.endswith(".txt")]
    structure_name = 'other'
    files_filtered = []
    for file in files:         
        with open(file, "rb") as f:
            raw = f.read(1000)  
            encoding = chardet.detect(raw)["encoding"]
        with open(file, "r", encoding=encoding) as f:
            first_line = f.readline().strip()
            
            columns = first_line.split("\t")  
            if any(measure_type in col for col in columns):
                structure_name = 'laser'
                files_filtered.append(file)
                
        
    if structure_name == 'other':
        for file in os.listdir(extract_folder):
            with open(os.path.join(extract_folder, file), "rb") as f:
                raw = f.read(1000)  
                encoding = chardet.detect(raw)["encoding"]
            with open(os.path.join(extract_folder, file), "r", encoding=encoding) as f:
                contenu_2 = f.read()
            if parameters[0] in contenu_2:
                files_filtered.append(os.path.join(extract_folder, file))

    files = files_filtered
    df_full = load_wafer_files(files)
    if structure_name == 'laser':
        df_filtered = filter_measure_laser(df_full, parameters=parameters, measure_type=measure_type,temperature=temperature)
    else :
        df_filtered = filter_measure(df_full, measure_type=measure_type, temperature=temperature)
        

    df_filtered["Wafer name"] = df_filtered["Wafer name"].astype(str).str.strip()
    df_meta["Wafer name"] = df_meta["Wafer name"].astype(str).str.strip()
    df_filtered = df_filtered.merge(df_meta, on="Wafer name", how="left", validate="many_to_one", indicator=True)

    if not (df_filtered["_merge"] == "both").all():
        raise ValueError("Some wafers are missing from YAML metadata")

    df_filtered.drop(columns="_merge", inplace=True)
    df_filtered["is_mpw"] = (df_filtered["tapeout"].astype(str).str.startswith("MPW"))
    df_filtered["tapeout_num"] = np.where(
        df_filtered["is_mpw"], np.nan,
        pd.to_numeric(df_filtered["tapeout"].astype(str).str.replace("TO", "", regex=False), errors="coerce"))
    df_filtered["tapeout_sort_group"] = np.where(df_filtered["is_mpw"], 0, 1)
    df_filtered["tapeout_sort_value"] = np.where(df_filtered["is_mpw"], df_filtered["tapeout"], df_filtered["tapeout_num"])
    df_filtered["wafer_label"] = np.where(df_filtered["is_mpw"], df_filtered["wafer_scribe"],   # MPW04
                                        (
        "TO" + df_filtered["tapeout_num"].map(lambda x: f"{x:g}")
        + "\nFab " + df_filtered["Fab_IIIV"]
        + "\n" + df_filtered["Wafer name"]
    )
    )
    label_order = (df_filtered.drop_duplicates("wafer_label").
                sort_values(["tapeout_sort_group", "tapeout_sort_value","Fab_IIIV","IIIV_split", "Wafer name"])["wafer_label"])
    df_filtered["wafer_label"] = pd.Categorical(df_filtered["wafer_label"], categories=label_order, ordered=True)

    # Preparing the plot
    if structure_name == 'laser':
        data, labels = prepare_boxplot_data(df_filtered, group_col=group_by, value_col=measure_type)
        
    else:
        data, labels = prepare_boxplot_data(df_filtered, group_col=group_by, value_col="Result")
        
    print(f"spec_ : {spec_}")
    if spec_ is not None:
        if isinstance(spec_, str):
            try:
                spec_ = float(spec_)
            except ValueError:
                pass
        spec_= tuple(map(float, spec_.strip("()").split(","))) if isinstance(spec_, str) and "," in spec_ else spec_
        if isinstance(spec_, dict):
            for key in spec_:
                try:
                    spec_[key] = float(spec_[key])
                except ValueError:
                    pass

    plot_boxplot_with_points(data, labels, ylabel=y_label, title=fig_title, jitter=0.08, logscale=False,ymin=y_min, ymax=y_max, spec=spec_)

    # Saving the figure
    os.makedirs(image_folder, exist_ok=True)
    image_filename = re.sub(r'[<>:"/\\|?*]', '_', image_filename)[:255]
    save_path = os.path.join(image_folder, image_filename)
    plt.savefig(save_path)
    
    return save_path



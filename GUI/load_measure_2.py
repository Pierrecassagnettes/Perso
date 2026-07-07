# -*- coding: utf-8 -*-
"""
load_measure_2.py

Refactored version:
- importable as a normal Python module
- still usable as a CLI script
- more robust with encodings and special characters (°, ², etc.)
"""

import sys
from pathlib import Path
import os
import chardet


# -----------------------------------------------------------------------------
# Console encoding (useful when launched as script / subprocess)
# -----------------------------------------------------------------------------
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
MEASURE_TYPES = [
    "Threshold (mA)",
    "Resistance @160mA (Ohm)",
    "r² Resistance",
    "Power CH1 @160mA (mW)",
    "Power CH2 @160mA (mW)",
    "LI slope (W/A)",
    "Roll-off current (mA)",
    "Total roll-off power (mW)",
    "R1 (ohm)",
    "R2 (ohm)",
    "R3 (ohm)",
    "R4 (ohm)",
    "Rsheet (ohm.sq)",
    "Resistivity (ohm.cm)",
    "Doping (cm-3)",
    "Rc (ohm)",
    "Lt (m)",
    "rho_c (ohm.cm2)",
    "r_sq linear regression",
    "Resistance @160mA, ohm",
    "SMSR @160mA, dB",
    "Threshold, mA",
    "Waveguide_total_power @160mA, mW",
    "TLM, Rsheet, ohm.sq",
    "TLM, Doping, cm-1",
    "TLM, rho_c, ohm.cm2",
    "dlambda/dPe (nm/W)",
    "dlambda/dT (nm/K)",
    "Thermal resistance (K/W)",
    "Current (mA)",
    "Peak wavelength (nm)",
    "SMSR (dB)",
    "Kappa (cm-1)",
    "Phase shift (°)",
]


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def normalize_text(text):
    """
    Normalize corrupted encodings and common textual variants.

    Goal:
    - keep display-friendly strings
    - make comparisons more robust
    """
    if text is None:
        return ""

    text = str(text)

    replacements = {
        "\ufeff": "",    # BOM
        "Â°": "°",
        "âˆ˜": "°",
        "â°": "°",
        "�": "°",        # replacement char (approximate recovery)
        "Â²": "²",
        "â²": "²",
        "cm²": "cm2",
        "cm⁻²": "cm-2",
        "cm⁻¹": "cm-1",
        "cm⁻³": "cm-3",
        "ohm.cm²": "ohm.cm2",
    }

    for bad, good in replacements.items():
        text = text.replace(bad, good)

    return text.strip()


def unique_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        key = normalize_text(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def parse_parameters(parameters):
    """
    Accepts:
    - a Python list
    - a Java-style string: [a, b, c]
    - a Python-style string: ['a', 'b', 'c']
    """
    if isinstance(parameters, list):
        return [str(p).strip().strip("'").strip('"') for p in parameters if str(p).strip()]

    parameters = str(parameters).strip()

    if not parameters:
        return []

    parameters = parameters.strip("[]")
    raw_parts = parameters.split(",")

    cleaned = [
        p.strip().strip("'").strip('"')
        for p in raw_parts
        if p.strip()
    ]
    return cleaned


def detect_file_encoding(file_path, n_bytes=2000):
    with open(file_path, "rb") as f:
        raw = f.read(n_bytes)

    detected = chardet.detect(raw)
    encoding = detected.get("encoding")

    if not encoding:
        encoding = "utf-8"

    return encoding


def read_text_file(file_path):
    """
    Robust text read with fallback encodings.
    """
    tried = []

    # Try chardet result first
    encodings_to_try = []
    detected = detect_file_encoding(file_path)
    if detected:
        encodings_to_try.append(detected)

    # Common fallbacks
    for enc in ["utf-8", "utf-8-sig", "cp1252", "latin-1"]:
        if enc not in encodings_to_try:
            encodings_to_try.append(enc)

    for enc in encodings_to_try:
        try:
            with open(file_path, "r", encoding=enc) as f:
                return normalize_text(f.read())
        except UnicodeDecodeError:
            tried.append(enc)
            continue

    # Last fallback
    with open(file_path, "r", encoding="latin-1", errors="replace") as f:
        return normalize_text(f.read())


def get_txt_files(folder):
    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    return [
        str(folder / file_name)
        for file_name in os.listdir(folder)
        if file_name.lower().endswith(".txt")
    ]


def text_contains_parameter(file_path, parameter):
    """
    True if the parameter is found in the filename or file content.
    """
    parameter_norm = normalize_text(parameter)
    filename_norm = normalize_text(os.path.basename(file_path))

    if parameter_norm in filename_norm:
        return True

    content = read_text_file(file_path)
    return parameter_norm in content


def find_candidate_files(parameters, files):
    """
    Return all files matching at least one parameter.
    """
    matched = []

    for file_path in files:
        for parameter in parameters:
            if text_contains_parameter(file_path, parameter):
                matched.append(file_path)
                break

    return unique_preserve_order(matched)


def extract_measures_from_files(files, measure_types=None):
    if measure_types is None:
        measure_types = MEASURE_TYPES

    result = []
    normalized_measure_types = [(m, normalize_text(m)) for m in measure_types]

    for file_path in files:
        content = read_text_file(file_path)

        for original_measure, normalized_measure in normalized_measure_types:
            if normalized_measure in content:
                result.append(original_measure)

    return unique_preserve_order(result)


# -----------------------------------------------------------------------------
# Public API for GUI import
# -----------------------------------------------------------------------------
def load_measures(parameters, folder):
    """
    Main function to be imported from the GUI.

    Parameters
    ----------
    parameters : list[str] | str
        Either a list of parameters or a string representation such as:
        "[param1, param2]"
    folder : str | Path
        Folder containing .txt extract files

    Returns
    -------
    list[str]
        List of detected measure types
    """
    parsed_parameters = parse_parameters(parameters)
    extract_folder = str(Path(folder))

    files = get_txt_files(extract_folder)
    files_parameter = find_candidate_files(parsed_parameters, files)
    result = extract_measures_from_files(files_parameter)

    return sorted(result)


# -----------------------------------------------------------------------------
# CLI entry point (backward compatibility)
# -----------------------------------------------------------------------------
def main():
    if len(sys.argv) < 3:
        raise ValueError("Usage: python load_measure_2.py \"[param1, param2]\" folder_path")

    parameters = sys.argv[1]
    folder = sys.argv[2]

    result = load_measures(parameters, folder)
    print(result)


if __name__ == "__main__":
    main()

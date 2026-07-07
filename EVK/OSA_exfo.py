# -*- coding: utf-8 -*-
"""
Created on June 30th 2026

@author: Kévin Froberger
Contact : kevin.froberger@scintil-photonics.com,
    jeremie.vigier@scintil-photonics.com
Part of this code is inspired from the PyMeasure package

Copyright (c) 2013-2023 PyMeasure Developers
Copyright (c) 2024 Scintil photonics

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Goal :
Object allowing to control the Exfo Variable Optical Attenuator
"""
import logging
import time

if __name__ == "__main__":
    from instrument import Instrument
    import matplotlib.pyplot as plt
else:
    from instrument import Instrument
import numpy as np
from typing import Union, Literal, Final  # Optional, List

# Setup logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class OSA_exfo(Instrument):
    """
    Creates the OSA object

    adapter : Should be an IP adress in the form : f"TCPIP0::{ip}::{port}::SOCKET"
    Example : TO BE FILLED

    Returns
    -------
    None.

    """

    def __init__(self, adapter, **kwargs):
        self.name = "OSA_exfo"
        super().__init__(adapter, self.name, **kwargs)
        
        self.clear_error_queue()
        self._initialize()
    def _initialize(self):
        """
        Function that initializes the powermeter

        Returns
        -------
        None

        """
        # Get the identity of the instrument
        print(self.id())

        # Check the instrument inside the LTK-1
        instru = self.ask("INST:CAT?")
        print(f'Instrument contains : {instru}')

        # Resetting the default configuration of the VOA
        self.reset_default()

        # Clear error queue
        self.clear_error_queue()
        print("OSA initialized")

    # ######################################################
    # Generic commands
    # ######################################################

    def close_connection(self):
        """
        Closes the ethernet connection to the instrument
        """
        self.close_adapter()

    def _check_operation_ended(self, op_type):
        """
        Checks if the operation is completed
        'LINStrument00:STATus:OPERation:BIT8:CONDition?' : p 133 => If attenuation is not set it returns 1,
        if it is set,, it returns 0

        s : Socket
        op_type : Type of operation

        Returns
        -------
        None.

        """
        operation_on_going = "1"
        counter = 0
        wait = 0.1
        while operation_on_going == "1":
            operation_on_going = self.ask("LINS00:STAT:OPER:BIT8:COND?")
            time.sleep(wait)  # Recommanded by Exfo engineers
            counter += 1

            # Adding a counter that raises an error if we wait too much
            if counter >= 100:
                raise Exception(
                    f"Waiting time limit reach while {op_type} : around {wait*counter}sec. Operation not working."
                )

    def reset_default(self):
        """
        Resets the instrument to its default setup
        p133 : ":RST" (high performance powermeter datasheet)

        """
        self.write(":RST")

    def clear_error_queue(self):
        """
        Clear the error queue
        """
        self.write("*CLS")

    def get_error_queue(self):
        """
        Query the error queue
        The response retrieved is of the form: error code, error name
        """
        response = self.ask(":SYST:ERR?")
        error = response.split(",")
        error_code = int(error[0])
        error_name = error[1]
        return error_code, error_name

    # ######################################################
    # Data management
    # ######################################################

    def get_spectrum_fast(self):
        """
        Récupère instantanément la trace active à l'écran.
        """
        self.write("LINS00:FORM:DATA ASC")
        trace_name = '"TRC1"'
        
        raw_y = self.ask(f"LINS00:TRAC:DATA? {trace_name}")
        
        if raw_y.startswith('#'):
            num_digits = int(raw_y[1])
            raw_y = raw_y[2 + num_digits:]
            
        powers = np.fromstring(raw_y, sep=',')
        
        start_w = float(self.ask("LINS00:SENS:WAV:STAR?"))
        stop_w = float(self.ask("LINS00:SENS:WAV:STOP?"))
        
        wavelengths = np.linspace(start_w, stop_w, len(powers))
        
        # CORRECTION : 1.55e-6 étant inférieur à 1.0, ce test à 1.0 est ultra-robuste
        # pour convertir les mètres en nanomètres (ex: 1550 nm)
        if len(wavelengths) > 0 and wavelengths[0] < 1.0:
            wavelengths *= 1e9
            
        return wavelengths, powers

    def analyze_peaks(self, wavelengths, powers, prominence: float = 3.0, distance: int = 10):
        """
        Détecte les pics du spectre, filtre pour ne garder que ceux > -30 dBm,
        et calcule l'espacement en fréquence (FSR) directement en THz.
        """
        from scipy.signal import find_peaks
        
        # 1. Détection initiale des pics
        peak_indices, _ = find_peaks(powers, prominence=prominence, distance=distance)
        
        # 2. MODIFICATION : Filtrage strict pour ne garder que les amplitudes > -30 dBm
        peak_indices = np.array([idx for idx in peak_indices if powers[idx] > -30.0])
        
        if len(peak_indices) == 0:
            log.warning("Aucun pic supérieur à -30 dBm n'a été détecté.")
            return [], np.array([])
            
        peak_wavs = wavelengths[peak_indices]
        peak_powers = powers[peak_indices]
        
        peaks = [{"wavelength_nm": w, "power_dbm": p} for w, p in zip(peak_wavs, peak_powers)]
        
        # 3. MODIFICATION : Calcul des fréquences absolues directement en THz (1e12)
        # nu (THz) = c / (lambda * 1e-9) / 1e12
        c = 299792458
        frequencies_thz = (c / (peak_wavs * 1e-9)) / 1e12
        
        # Calcul de la différence entre pics consécutifs en THz
        freq_spacings_thz = np.abs(np.diff(frequencies_thz))
        
        return peaks, freq_spacings_thz
def main():
    ip = "172.16.30.86"  
    port = 5025         
    
    OSA = OSA_exfo(
        f"TCPIP0::{ip}::{port}::SOCKET",
        write_termination="\r\n",
        read_termination="\r\n",
        timeout=5.0,
    )
    
    # Récupération rapide
    wavelengths, powers = OSA.get_spectrum_fast()
    
    # Analyse avec le nouveau filtrage à -30 dBm intégré
    peaks, spacings = OSA.analyze_peaks(wavelengths, powers, prominence=5.0)
    
    print("\n--- RÉSULTATS DE L'ANALYSE ---")
    print(f"Nombre de pics valides (> -30 dBm) trouvés : {len(peaks)}")
    for i, p in enumerate(peaks):
        print(f"Pic #{i+1}: {p['wavelength_nm']:.3f} nm | {p['power_dbm']:.2f} dBm")
        
    # Affichage des écarts en THz
    for i, space in enumerate(spacings):
        print(f"Espacement Fréquence Pic {i+1} -> Pic {i+2}: {space:.4f} THz")

    OSA.close_connection()

if __name__ == "__main__":
    main()
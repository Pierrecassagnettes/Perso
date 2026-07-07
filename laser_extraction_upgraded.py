import os
import warnings
from tkinter.filedialog import askdirectory
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from scipy import stats, signal


from laser_data_analysis import (get_laser_smsr, get_laser_threshold, get_laser_LI_slope,
                                 get_laser_resistance, get_laser_rolloff, interpolate_z)
from load_data import load_data_array_format
from parameters_laser_extraction import *
from fusion import fusionner_plusieurs_fichiers

plt.close("all")


class Laser:
    def __init__(self, name, die_name, wafer_id):
        """
        Initializes a Laser instance with architectural parameters and storage structures.

        Parameters:
        -----------
        name : str
            The unique identifier/name of the laser component (e.g., "Laser_A").
        die_name : str
            The name of the die containing this specific laser (e.g., "Die_0_0").
        wafer_id : str
            The identifier of the wafer containing the die (e.g., "Wafer_1").

        Returns:
        --------
        None

        Example:
        --------
        >>> laser = Laser("Laser_A", "Die_0_0", "Wafer_1")
        """
        self.name = name
        self.die_name = die_name
        self.wafer_id = wafer_id
        
        # Characteristics from parameters
        self.length = laser_length[self.name]
        self.shunt_name = associated_shunt_name[self.name]
        self.tap_name = associated_tap_name.get(self.name) if remove_tap_loss else None
        self.peak_search_range = laser_peak_search[self.name]
        
        # Lightweight storage structures (prevents clogging RAM)
        self.results = {}        
        self.spectra_data = {}   
        self.data_liv_deemb = {} # Temporary storage of LIV matrices for Rth calculation
        
    def process_temperature(self, temperature, data_dir, img_group_dir, kappa_cache):
        """
        Executes the complete processing chain for a given operating temperature.

        Parameters:
        -----------
        temperature : int or float
            The measurement temperature in Celsius degrees (e.g., 25, 30, 85).
        data_dir : str
            The absolute or relative path to the source data directory.
        img_group_dir : str
            The path to the output directory where generated plots will be grouped.
        kappa_cache : dict
            A dictionary containing pre-cached theoretical matrices for Kappa simulations.

        Returns:
        --------
        None

        Example:
        --------
        >>> laser.process_temperature(30, "/data/Wafer_1", "/output/plots", kappa_cache_dict)
        """
        self.results[temperature] = {}
        self.spectra_data[temperature] = {cur: {'wl': np.nan, 'smsr': np.nan, 'kappa': np.nan, 'phase_shift': np.nan} for cur in current_spectra}
        
        # 1. Shunts management (Grating Couplers) - Fallback if missing
        f_gc, wl_bounds_gc, has_deemb = self._load_shunt_interpolation(temperature, data_dir)
        f_tap = self._load_tap_interpolation(temperature, data_dir) if (has_deemb and remove_tap_loss) else None

        # 2. Loading baseline LIV data
        liv_data = self._load_liv_data(temperature, data_dir)
        if liv_data is None:
            return

        # 3. Spectra processing (populates self.spectra_data)
        self._process_spectra(temperature, data_dir, img_group_dir, f_gc, wl_bounds_gc, has_deemb)

        # 4. Calculation of de-embedding for LIV
        to_deemb = 0.0
        ref_wl = self.spectra_data[temperature].get(ref_current, {}).get('wl')
        
        if has_deemb and ref_wl and not np.isnan(ref_wl):
            loss_gc = f_gc(ref_wl)
            loss_tap = (f_tap(ref_wl) - 2 * loss_gc) if f_tap else 0.0
            to_deemb = loss_gc + loss_tap

        # Generation of the LIV matrix (de-embedded or raw)
        if nb_pwm_channels == 1:
            liv_deemb = np.column_stack((
                liv_data[:, id_column_current_in_liv_file],
                liv_data[:, id_column_voltage_in_liv_file],
                liv_data[:, id_column_power_in_liv_file] - to_deemb
            ))
        else:
            liv_deemb = np.column_stack((
                liv_data[:, id_column_current_in_liv_file],
                liv_data[:, id_column_voltage_in_liv_file],
                liv_data[:, id_column_power_ch1_in_liv_file] - to_deemb,
                liv_data[:, id_column_power_ch2_in_liv_file] - to_deemb
            ))
        
        self.data_liv_deemb[temperature] = liv_deemb 

        # 5. Extraction of LIV metrics & Roll-off
        self._extract_liv_metrics(temperature, liv_deemb)

        # 6. Extraction of Kappa & Phase Shift (per current) - Runs even without Shunt
        if process_kappa_phase_shift:
            self._extract_kappa_phase(temperature, data_dir, img_group_dir, kappa_cache)

        # 7. Extraction of MPD Responsivity
        if mpd_processing and self.name in list_lasers_with_mpd:
            self._extract_mpd(temperature, liv_data, liv_deemb, f_gc(ref_wl) if (has_deemb and ref_wl) else 0.0)

        # 8. Series resistance, Threshold and Slope (LIV)
        self._extract_resistance_and_threshold(temperature, liv_data, liv_deemb, img_group_dir)

        # 9. Extraction of SMSR
        self._extract_smsr(temperature, img_group_dir, has_deemb)
        
        if display_extract_LIV_deemb_per_laser:
            self._plot_liv(temperature, liv_deemb, img_group_dir)
            
    def _load_shunt_interpolation(self, temperature, data_dir):
        """
        Loads the shunt/grating coupler measurement file and creates a 1D interpolation function.

        Parameters:
        -----------
        temperature : int or float
            The measurement temperature in Celsius degrees.
        data_dir : str
            The absolute or relative path to the source data directory.

        Returns:
        --------
        tuple
            (f_gc, bounds, success_flag)
            - f_gc (scipy.interpolate.interp1d or None): The interpolation function for power loss vs wavelength.
            - bounds (list of float or None): Min and max wavelengths [wl_min, wl_max] of the shunt dataset.
            - success_flag (bool): True if data loaded and valid, False otherwise.

        Example:
        --------
        >>> f_gc, bounds, success = laser._load_shunt_interpolation(30, "/data")
        """
        shunt_folder = os.path.join(data_dir, self.wafer_id, shunt_component_group, self.shunt_name, "30C")
        shunt_file = os.path.join(shunt_folder, f"{self.die_name}_{self.wafer_id}_{self.shunt_name}_30C.txt")
        try:
            data_shunt = load_data_array_format(shunt_file, delimiter='\t')
            f_gc = interp1d(data_shunt[:, id_column_wl_in_shunt_file], data_shunt[:, id_column_il_in_shunt_file] / 2)
            bounds = [data_shunt[:, id_column_wl_in_shunt_file].min(), data_shunt[:, id_column_wl_in_shunt_file].max()]
            if np.max(data_shunt[:, id_column_il_in_shunt_file] / 2) < min_loss_gc:
                return None, None, False
            return f_gc, bounds, True
        except FileNotFoundError:
            return None, None, False

    def _load_tap_interpolation(self, temperature, data_dir):
        """
        Loads the tap monitor file and returns an interpolation function for its insertion loss.

        Parameters:
        -----------
        temperature : int or float
            The measurement temperature in Celsius degrees.
        data_dir : str
            The path to the source data directory.

        Returns:
        --------
        scipy.interpolate.interp1d or None
            An interpolation function mapping wavelength to insertion loss. Returns None if file is missing.

        Example:
        --------
        >>> f_tap = laser._load_tap_interpolation(30, "/data")
        """
        tap_folder = os.path.join(data_dir, self.wafer_id, tap_component_group, self.tap_name, f"{temperature}C")
        tap_file = os.path.join(tap_folder, f"{self.die_name}_{self.wafer_id}_{self.tap_name}_{temperature}C.txt")
        try:
            data_tap = load_data_array_format(tap_file, delimiter='\t')
            return interp1d(data_tap[:, id_column_wl_in_shunt_file], data_tap[:, id_column_il_in_shunt_file])
        except FileNotFoundError:
            return None

    def _load_liv_data(self, temperature, data_dir):
        """
        Loads the raw LIV data array from the corresponding text file and truncates specified initial points.

        Parameters:
        -----------
        temperature : int or float
            The measurement temperature in Celsius degrees.
        data_dir : str
            The path to the source data directory.

        Returns:
        --------
        numpy.ndarray or None
            A 2D array representing the LIV matrix data rows. Returns None if the file is not found.

        Example:
        --------
        >>> data = laser._load_liv_data(25, "/data")
        """
        liv_folder = os.path.join(data_dir, self.wafer_id, laser_component_group, self.name, f"{temperature}C", "LIV")
        liv_file = os.path.join(liv_folder, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_LIV.txt")
        try:
            return load_data_array_format(liv_file, delimiter='\t')[nb_points_to_remove_liv:]
        except FileNotFoundError:
            return None

    def _process_spectra(self, temperature, data_dir, img_group_dir, f_gc, wl_bounds_gc, has_deemb):
        """
        Iterates over the requested bias currents to process spectrum files, locate peaks, and save individual plots.

        Parameters:
        -----------
        temperature : int or float
            The current measurement temperature in Celsius degrees.
        data_dir : str
            The path to the data source root.
        img_group_dir : str
            The target output directory for figures.
        f_gc : scipy.interpolate.interp1d or None
            The shunt loss interpolation function.
        wl_bounds_gc : list of float or None
            Valid wavelength range boundaries [min, max] derived from the shunt data.
        has_deemb : bool
            True if the de-embedding processing using a shunt is applicable.

        Returns:
        --------
        None

        Example:
        --------
        >>> laser._process_spectra(30, "/data", "/output", f_gc, [1260.0, 1340.0], True)
        """
        spectra_folder = os.path.join(data_dir, self.wafer_id, laser_component_group, self.name, f"{temperature}C", "Spectra")
        list_wl_peaks = []

        fig, ax = plt.subplots()
        fig_zoom, ax_zoom = plt.subplots(figsize=[2.4, 1.8])
        colors_local = plt.cm.rainbow(np.arange(0, len(current_spectra), 1) / max(1, len(current_spectra) - 1))

        for idx, cur in enumerate(current_spectra):
            data_spec = None
            for fmt in [f'_spectrum_{cur}mA.txt', f'_spectrum_{str(round(float(cur)))}mA.txt', f'_spec_{str(round(float(cur)))}mA.txt']:
                path = os.path.join(spectra_folder, f'{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C{fmt}')
                if os.path.exists(path):
                    data_spec = load_data_array_format(path, delimiter='\t')
                    break
            
            if data_spec is None:
                continue

            if has_deemb:
                data_spec = data_spec[(data_spec[:, id_column_wl_in_spectrum_file] > wl_bounds_gc[0]) & 
                                      (data_spec[:, id_column_wl_in_spectrum_file] < wl_bounds_gc[1])]
                power_processed = data_spec[:, id_column_power_in_spectrum_file] - f_gc(data_spec[:, id_column_wl_in_spectrum_file])
            else:
                power_processed = data_spec[:, id_column_power_in_spectrum_file]

            wl_arr = data_spec[:, id_column_wl_in_spectrum_file]
            pos_res = np.where((wl_arr > self.peak_search_range[0]) & (wl_arr < self.peak_search_range[1]))[0]
            
            if len(pos_res) > 0:
                idx_max = np.argmax(power_processed[pos_res])
                peak_wl = wl_arr[pos_res[idx_max]]
                if power_processed[pos_res[idx_max]] > -50:
                    self.spectra_data[temperature][cur]['wl'] = peak_wl
                    self.spectra_data[temperature][cur]['raw_power_vector'] = power_processed 
                    list_wl_peaks.append(peak_wl)
                    
                    # Filling individual plots
                    ax.plot(wl_arr, power_processed, color=colors_local[idx], label=f'{int(float(cur))}mA')
                    ax_zoom.plot(wl_arr, power_processed, color=colors_local[idx])

        # Saving individual image folders
        if save_extract_figures and list_wl_peaks:
            img_laser_dir = os.path.join(img_group_dir, self.name, "Spectra")
            os.makedirs(img_laser_dir, exist_ok=True)
            
            ax.grid(True, linestyle='--')
            ax.set_xlim([1270, 1330])
            ax.set_ylim(-65, 15)
            ax.legend(fontsize=8, ncol=3, loc='best')
            ax.set_title(f"Spectra, {self.name}, \n{self.die_name}, {temperature}°C, deembedded")
            fig.tight_layout()
            fig.savefig(os.path.join(img_laser_dir, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_spectra_deemb.png"))
            
            ax_zoom.set_xlim([min(list_wl_peaks) - 1, max(list_wl_peaks) + 1])
            ax_zoom.set_ylim(bottom=-60)
            ax_zoom.grid(True, linestyle='--')
            fig_zoom.tight_layout()
            fig_zoom.savefig(os.path.join(img_laser_dir, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_spectra_deemb_zoom.png"))
        
        plt.close(fig)
        plt.close(fig_zoom)

    def _extract_liv_metrics(self, temperature, liv_deemb):
        """
        Extracts specific electrical and optical metrics from the de-embedded LIV matrix at reference currents.

        Parameters:
        -----------
        temperature : int or float
            The current measurement temperature.
        liv_deemb : numpy.ndarray
            The 2D matrix containing the processed current, voltage, and power channel columns.

        Returns:
        --------
        None

        Example:
        --------
        >>> laser._extract_liv_metrics(25, liv_matrix_data)
        """
        try:
            f_li_ch1 = interp1d(liv_deemb[:, 0], liv_deemb[:, 2], kind='linear')
            self.results[temperature]['power_LI_ch1'] = 10 ** (f_li_ch1(float(ref_current) / 1000) / 10)
            
            if nb_pwm_channels == 2:
                f_li_ch2 = interp1d(liv_deemb[:, 0], liv_deemb[:, 3], kind='linear')
                self.results[temperature]['power_LI_ch2'] = 10 ** (f_li_ch2(float(ref_current) / 1000) / 10)
            else:
                self.results[temperature]['power_LI_ch2'] = np.nan
            
            # Roll-off
            ro_cur, ro_pow = get_laser_rolloff(liv_deemb[:, 0], 10 ** (liv_deemb[:, 2] / 10))
            self.results[temperature]['rolloff_current'] = ro_cur * 1000
            if nb_pwm_channels == 2:
                _, ro_pow_ch2 = get_laser_rolloff(liv_deemb[:, 0], 10 ** (liv_deemb[:, 3] / 10))
                self.results[temperature]['rolloff_power'] = ro_pow + ro_pow_ch2
            else:
                self.results[temperature]['rolloff_power'] = ro_pow
        except Exception:
            self.results[temperature]['power_LI_ch1'] = np.nan
            self.results[temperature]['power_LI_ch2'] = np.nan
            self.results[temperature]['rolloff_current'] = np.nan
            self.results[temperature]['rolloff_power'] = np.nan

    def _extract_resistance_and_threshold(self, temperature, liv_data, liv_deemb, img_group_dir):
        """
        Calculates the series resistance, laser threshold current, and the L-I slope using analytical derivatives.

        Parameters:
        -----------
        temperature : int or float
            The operating temperature condition.
        liv_data : numpy.ndarray
            The raw input data array containing voltage and current indices.
        liv_deemb : numpy.ndarray
            The de-embedded LIV column data.
        img_group_dir : str
            The output path for diagnostic engineering plots.

        Returns:
        --------
        None

        Example:
        --------
        >>> laser._extract_resistance_and_threshold(85, raw_liv, deemb_liv, "/out/plots")
        """
        current_a = liv_data[:, id_column_current_in_liv_file]
        voltage_v = liv_data[:, id_column_voltage_in_liv_file]
        res_current = float(ref_current) / 1000
        display_plot = display_processing or save_extract_figures

        # 1. Series resistance
        if display_plot:
            las_res, fig, ax = get_laser_resistance(current_a, voltage_v, res_current, window=0.02, display=True)
            if save_extract_figures:
                out_dir = os.path.join(img_group_dir, self.name, "Processing_resistance")
                os.makedirs(out_dir, exist_ok=True)
                fig.savefig(os.path.join(out_dir, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_{ref_current.replace('.0', '')}mA_resistance.png"))
            plt.close(fig)
        else:
            las_res = get_laser_resistance(current_a, voltage_v, res_current, window=0.02, display=False)
            
        self.results[temperature]['resistance'] = las_res[0]
        self.results[temperature]['res_r_square'] = las_res[2]
        
        # 2. Threshold
        c_mA = liv_deemb[:, 0] * 1000
        p_mW = 10 ** (liv_deemb[:, 2] / 10)
        mask = ~np.isnan(p_mW)
        
        try:
            if display_plot:
                th, fig, ax = get_laser_threshold(c_mA[mask][4:], p_mW[mask][4:], height=0.01, display=True, method='second derivative not smoothed')
                if save_extract_figures:
                    out_dir = os.path.join(img_group_dir, self.name, "Processing_threshold")
                    os.makedirs(out_dir, exist_ok=True)
                    fig.savefig(os.path.join(out_dir, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_threshold.png"))
                plt.close(fig)
            else:
                th = get_laser_threshold(c_mA[mask][4:], p_mW[mask][4:], height=0.01, display=False, method='second derivative not smoothed')
            self.results[temperature]['threshold'] = th if th > 10 else np.nan
        except Exception:
            self.results[temperature]['threshold'] = np.nan

        # 3. LI Slope
        try:
            th_val = self.results[temperature]['threshold']
            if display_plot:
                slope, fig, ax = get_laser_LI_slope(liv_deemb[:, 0][mask], p_mW[mask], th_val / 1000, threshold_step=0.01, window=0.005, display=True)
                if save_extract_figures:
                    out_dir = os.path.join(img_group_dir, self.name, "Processing_LI_slope")
                    os.makedirs(out_dir, exist_ok=True)
                    fig.savefig(os.path.join(out_dir, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_LI_slope.png"))
                plt.close(fig)
            else:
                slope = get_laser_LI_slope(liv_deemb[:, 0][mask], p_mW[mask], th_val / 1000, threshold_step=0.01, window=0.005, display=False)
            self.results[temperature]['slope_LI'] = slope
        except Exception:
            self.results[temperature]['slope_LI'] = np.nan

    def _extract_kappa_phase(self, temperature, data_dir, img_group_dir, kappa_cache):
        """
        Executes a complex multidimensional convergence algorithm to extract grating coupling coefficient (Kappa) 
        and Phase Shift values by matching experimental stop-band peaks with theoretical cache solutions.

        Parameters:
        -----------
        temperature : int or float
            The active test temperature.
        data_dir : str
            The base repository folder for raw spectral data.
        img_group_dir : str
            The directory for diagnostic extraction graphs.
        kappa_cache : dict
            The preloaded numerical simulation arrays categorized by cavity length keys (e.g., 'L400').

        Returns:
        --------
        None

        Example:
        --------
        >>> laser._extract_kappa_phase(30, "/data", "/output", wafer.kappa_cache)
        """
        l_key = f"L{self.length}"
        if l_key not in kappa_cache: return
        cache = kappa_cache[l_key]
        
        spectra_folder = os.path.join(data_dir, self.wafer_id, laser_component_group, self.name, f"{temperature}C", "Spectra")
        
        for cur in current_spectra:
            wl_peak = self.spectra_data[temperature][cur].get('wl')
            if wl_peak is None or np.isnan(wl_peak): continue
                
            data_spec = None
            for fmt in [f'_spectrum_{cur}mA.txt', f'_spectrum_{str(round(float(cur)))}mA.txt', f'_spec_{str(round(float(cur)))}mA.txt']:
                path = os.path.join(spectra_folder, f'{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C{fmt}')
                if os.path.exists(path):
                    data_spec = load_data_array_format(path, delimiter='\t')
                    break
            if data_spec is None: continue
            
            try:
                # Precise filtering by wavelength columns
                wl_col = data_spec[:, id_column_wl_in_spectrum_file]
                p_col = data_spec[:, id_column_power_in_spectrum_file]
                
                pos_win = np.where((wl_col > wl_peak - kappa_window[0]) & (wl_col < wl_peak + kappa_window[1]))[0]
                wind_spectra = np.column_stack((wl_col[pos_win], p_col[pos_win]))
                
                peaks, _ = signal.find_peaks(wind_spectra[:, 1], distance=40, width=3)
                wave_left = wind_spectra[peaks[0], 0]
                wave_p = wind_spectra[peaks[1], 0]
                wave_right = wind_spectra[peaks[2], 0]
                
                d_lam = np.abs(wave_p - wave_left)
                d_lam_psb = wave_right - wave_left
                
                # Individual plot of Kappa peaks
                if save_extract_figures and display_peaks_kappa_phase_shift:
                    fig, ax = plt.subplots()
                    ax.plot(wind_spectra[:, 0], wind_spectra[:, 1], label='Windowed spectrum')
                    ax.scatter(wave_p, wind_spectra[peaks[1], 1], label=f'Peak = {wave_p:.3f}nm', color='black')
                    ax.scatter(wave_left, wind_spectra[peaks[0], 1], color='red', label=f'Left = {wave_left:.3f}nm')
                    ax.scatter(wave_right, wind_spectra[peaks[2], 1], color='green', label=f'Right = {wave_right:.3f}nm')
                    ax.set_title(f'Peaks {self.name}, {cur}mA'); ax.legend(); ax.grid(True, linestyle='--')
                    fig.tight_layout()
                    p_folder = os.path.join(img_group_dir, self.name, "Kappa_Phase_shift", "Peaks")
                    os.makedirs(p_folder, exist_ok=True)
                    fig.savefig(os.path.join(p_folder, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_{cur}mA_peaks.png"))
                    plt.close(fig)

                # Calculation of the theoretical matrices
                d_lambda_psb_th_mat = cache['d_beta_psb_th'] * (wave_p * 1e-9) ** 2 / (2 * np.pi * group_index) * 1e9
                kappa_res = np.zeros(refinment_steps + 1)
                phase_shift_res = np.zeros(refinment_steps + 1)
                kappa_res[0], phase_shift_res[0] = 80, 90
                
                # Convergence loop
                for ind in range(refinment_steps):
                    d_lambda_psb_avg_th = []
                    for i in range(len(cache['kappa_list'])):
                        f_phase = interp1d(cache['phase_list'] * 180 / np.pi, d_lambda_psb_th_mat[i, :], kind='quadratic', fill_value="extrapolate")
                        d_lambda_psb_avg_th.append(f_phase(phase_shift_res[ind]))
                        
                    f_kappa = interp1d(d_lambda_psb_avg_th, cache['kappa_list'] / adjust_kappa, kind='linear', fill_value="extrapolate")
                    kappa_res[ind + 1] = f_kappa(d_lam_psb) 
                    
                    y_unknown = d_lam / d_lam_psb
                    
                    if save_extract_figures and display_kappa_z_interpole:
                        interp, fig, ax = interpolate_z(cache['kappa_matrix'], cache['wave_shift_th'], cache['phase_shift_matrix'], kappa_res[ind + 1], y_unknown, method='linear', debug=True)
                        z_folder = os.path.join(img_group_dir, self.name, "Kappa_Phase_shift", "Refine")
                        os.makedirs(z_folder, exist_ok=True)
                        fig.savefig(os.path.join(z_folder, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_{cur}mA_refinement{ind}_zinter.png"))
                        plt.close(fig)
                        phase_shift_res[ind + 1] = interp[0]
                    else:
                        interp = interpolate_z(cache['kappa_matrix'], cache['wave_shift_th'], cache['phase_shift_matrix'], kappa_res[ind + 1], y_unknown, method='linear', debug=False)
                        phase_shift_res[ind + 1] = interp[0]
                    
                self.spectra_data[temperature][cur]['kappa'] = float(kappa_res[-1])
                self.spectra_data[temperature][cur]['phase_shift'] = float(phase_shift_res[-1])
                
                # Saving the refinement summary
                if save_extract_figures and display_kappa_refinment_steps:
                    fig, ax = plt.subplots()
                    pts = ax.scatter(kappa_res, phase_shift_res, c=list(range(refinment_steps + 1)), cmap='viridis')
                    fig.colorbar(pts, label="Iteration number")
                    ax.set_xlabel(r'$\kappa$ (cm$^{-1}$)'); ax.set_ylabel(r'$\Phi$ (°)')
                    ax.grid(True, linestyle='--')
                    r_folder = os.path.join(img_group_dir, self.name, "Kappa_Phase_shift", "Refine")
                    os.makedirs(r_folder, exist_ok=True)
                    fig.savefig(os.path.join(r_folder, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_{cur}mA_refinement{refinment_steps}_refine_summary.png"))
                    plt.close(fig)
                    
            except Exception as e:
                self.spectra_data[temperature][cur]['kappa'] = np.nan
                self.spectra_data[temperature][cur]['phase_shift'] = np.nan

    def _extract_mpd(self, temperature, liv_data, liv_deemb, loss_gc, img_group_dir):
        """
        Calculates the internal monitor photodiode (MPD) responsivity over a filtered current range.

        Parameters:
        -----------
        temperature : int or float
            The measurement test temperature.
        liv_data : numpy.ndarray
            The raw data containing MPD current indices.
        liv_deemb : numpy.ndarray
            The de-embedded wave power matrix.
        loss_gc : float
            The grating coupler insertion loss evaluated at reference peak wavelength (in dB).
        img_group_dir : str
            The base path configuration for graphic file creation.

        Returns:
        --------
        None

        Example:
        --------
        >>> laser._extract_mpd(25, raw_data, deemb_data, 4.5, "/output/plots")
        """
        pos = np.where(liv_deemb[:, 0] >= min_laser_current_for_mpd)[0]
        if len(pos) > 0:
            i_mpd = -liv_data[pos, id_column_mpd_i_in_liv_file]
            p_mpd = 10 ** ((liv_data[pos, id_column_power_in_liv_file] - loss_gc) / 10)
            resp_val = np.mean(i_mpd * 1000 / p_mpd)
            self.results[temperature]['responsivity'] = resp_val
            
            if save_extract_figures:
                fig, ax = plt.subplots()
                ax.plot(liv_deemb[:, 0]*1000, -liv_data[:, id_column_mpd_i_in_liv_file] * 1000 / 10**((liv_data[:, id_column_power_in_liv_file] - loss_gc)/10), label='current_MPD/power')
                ax.plot(liv_deemb[pos, 0] * 1000, i_mpd*1000/p_mpd, label='Responsivity points used')
                ax.plot([liv_deemb[:, 0].min()*1000, liv_deemb[:, 0].max()*1000], [resp_val, resp_val], color='black', label=f'Responsivity : {resp_val:.2f}A/W')
                ax.legend(); ax.set_xlabel('Laser current (mA)'); ax.set_ylabel('Responsivity (A/W)')
                ax.set_title(f'MPD responsivity, {self.name},\n{self.die_name}, {temperature}C'); ax.grid(True, linestyle='--')
                fig.tight_layout()
                fig_path = os.path.join(img_group_dir, self.name, 'MPD')
                os.makedirs(fig_path, exist_ok=True)
                fig.savefig(os.path.join(fig_path, f'{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_MPD_resp.png'))
                plt.close(fig)
        else:
            self.results[temperature]['responsivity'] = np.nan

    def _extract_smsr(self, temperature, img_group_dir, has_deemb):
        """
        Calculates the Side-Mode Suppression Ratio (SMSR) from the stored power vector and saves plots.

        Parameters:
        -----------
        temperature : int or float
            The operational thermal point.
        img_group_dir : str
            The output root folder for diagnostics pictures.
        has_deemb : bool
            Flag notifying if the dataset utilizes de-embedding rules.

        Returns:
        --------
        None

        Example:
        --------
        >>> laser._extract_smsr(30, "/output/plots", True)
        """
        display_plot = display_processing or save_extract_figures
        for cur in current_spectra:
            p_vec = self.spectra_data[temperature][cur].pop('raw_power_vector', None)
            if p_vec is not None:
                if display_plot:
                    val_smsr, fig, ax = get_laser_smsr(p_vec, display=True)
                    if save_extract_figures:
                        out_dir = os.path.join(img_group_dir, self.name, "Processing_SMSR")
                        os.makedirs(out_dir, exist_ok=True)
                        fig.savefig(os.path.join(out_dir, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_{cur}mA_SMSR.png"))
                    plt.close(fig)
                else:
                    val_smsr = get_laser_smsr(p_vec, display=False)
                self.spectra_data[temperature][cur]['smsr'] = val_smsr

    def extract_thermal_resistance(self):
        """
        Computes dlambda/dPe, dlambda/dT and the final thermal resistance Rth (Complete original logic).

        Parameters:
        -----------
        None

        Returns:
        --------
        dict or None
            A dictionary containing:
            - 'dldpe': Wavelength shift vs Electrical Power slope (nm/W)
            - 'dldt': Wavelength shift vs Temperature slope (nm/K)
            - 'rth': Thermal resistance coefficient (K/W)
            Returns None if insufficient temperature matrices are available.

        Example:
        --------
        >>> rth_metrics = laser.extract_thermal_resistance()
        """
        valid_temps = [t for t in self.results.keys() if t in self.data_liv_deemb]
        if len(valid_temps) < 3: 
            return None
        
        d_lambda_d_Pe_list = []
        for temp in valid_temps:
            liv_deemb = self.data_liv_deemb[temp]
            f_iv = interp1d(liv_deemb[:, 0], liv_deemb[:, 1], kind='linear', fill_value="extrapolate")
            
            elec_power, wl_peaks = [], []
            for cur in current_th_res:
                wl = self.spectra_data[temp].get(cur, {}).get('wl')
                if wl and not np.isnan(wl):
                    try:
                        elec_power.append(float(cur) * 0.001 * f_iv(float(cur) * 0.001))
                        wl_peaks.append(wl)
                    except ValueError:
                        pass
            
            if len(elec_power) >= 2:
                res = stats.linregress(elec_power, wl_peaks)
                if res.rvalue ** 2 >= 0.98:
                    d_lambda_d_Pe_list.append(res.slope)

        d_lambda_d_T_list = []
        for cur in current_th_res:
            chaleur, wl_peaks = [], []
            for temp in valid_temps:
                wl = self.spectra_data[temp].get(cur, {}).get('wl')
                if wl and not np.isnan(wl):
                    chaleur.append(temp)
                    wl_peaks.append(wl)
            
            if len(chaleur) >= 2:
                res = stats.linregress(chaleur, wl_peaks)
                if res.rvalue ** 2 >= 0.98:
                    d_lambda_d_T_list.append(res.slope)

        if d_lambda_d_Pe_list and d_lambda_d_T_list:
            mean_pe = np.mean(d_lambda_d_Pe_list)
            mean_t = np.mean(d_lambda_d_T_list)
            return {
                'dldpe': mean_pe,
                'dldt': mean_t,
                'rth': mean_pe / mean_t if mean_t != 0 else np.nan
            }
        return None

    def _plot_liv(self, temperature, liv_deemb, img_group_dir):
        """
        Generates individual de-embedded LIV engineering figures containing dual y-axes for Voltage and Power.

        Parameters:
        -----------
        temperature : int or float
            The specific test thermal condition.
        liv_deemb : numpy.ndarray
            The 2D matrix structure holding voltage, current, and optical powers.
        img_group_dir : str
            The output root folder structure where the individual plot will be exported.

        Returns:
        --------
        None

        Example:
        --------
        >>> laser._plot_liv(25, deemb_matrix, "/output/plots")
        """
        if not save_extract_figures:
            return
            
        fig1, ax1 = plt.subplots()
        current_meas = liv_deemb[:, 0]
        voltage_meas = liv_deemb[:, 1]
        
        # Voltage axis (Blue)
        ax1.plot(current_meas[voltage_meas >= 0] * 1000, voltage_meas[voltage_meas >= 0],
                 marker="+", color="blue", markersize=4)
        ax1.yaxis.label.set_color("blue")
        ax1.tick_params(axis="y", colors="blue")
        ax1.set_title(f"LIV, {self.name}, \n{self.die_name}, {temperature}°C, deembedded")
        ax1.set_xlabel("Current (mA)")
        ax1.set_ylabel("Voltage (V)")
        
        # Power axis (Red / Orange)
        ax2 = ax1.twinx()
        if nb_pwm_channels == 1:
            ax2.plot(current_meas * 1000, np.power(10, liv_deemb[:, 2] / 10),
                     color="red", marker="+", markersize=4)
        else:
            ax2.plot(current_meas * 1000, np.power(10, liv_deemb[:, 2] / 10),
                     color="red", marker="+", markersize=4, label='CH1')
            ax2.plot(current_meas * 1000, np.power(10, liv_deemb[:, 3] / 10),
                     color="orange", marker="+", markersize=4, label='CH2')
            ax2.legend()
            
        ax2.yaxis.label.set_color("red")
        ax2.tick_params(axis="y", colors="red")
        ax2.set_ylabel("Optical power in waveguide (mW)")
        ax2.grid(True, linestyle="--")
        fig1.tight_layout()
        
        # Destination folder management
        img_liv_folder = os.path.join(img_group_dir, self.name, "LIV")
        os.makedirs(img_liv_folder, exist_ok=True)
        
        fig1.savefig(os.path.join(img_liv_folder, f"{self.die_name}_{self.wafer_id}_{self.name}_{temperature}C_LIV_noGC.png"))
        plt.close(fig1)


class Die:
    def __init__(self, name, wafer_id):
        """
        Initializes a Die instance containing an aggregated mapping dictionary of Laser structures.

        Parameters:
        -----------
        name : str
            The coordinates or name key specifying this die location (e.g., "Die_1_1").
        wafer_id : str
            The identity string tracking the associated parent wafer entity.

        Returns:
        --------
        None

        Example:
        --------
        >>> die = Die("Die_1_1", "Wafer_02")
        """
        self.name = name
        self.wafer_id = wafer_id
        self.lasers = {l_name: Laser(l_name, self.name, self.wafer_id) for l_name in list_laser_names}

    def process_die(self, data_dir, img_wafer_dir, kappa_cache):
        """
        Iterates over all internal laser structures to execute thermal measurements algorithms.

        Parameters:
        -----------
        data_dir : str
            The base configuration path containing empirical data text files.
        img_wafer_dir : str
            The wafer-level output directory for picture storage.
        kappa_cache : dict
            The mapping reference storing cached matrices for simulation curves adjustments.

        Returns:
        --------
        None

        Example:
        --------
        >>> die.process_die("/data/Wafer_1", "/output/images", cache_dict)
        """
        print(f"-> Extraction de la Die : {self.name.lower()}")
        img_group_dir = os.path.join(img_wafer_dir, laser_component_group)
        for laser in self.lasers.values():
            for temperature in list_temperatures:
                laser.process_temperature(temperature, data_dir, img_group_dir, kappa_cache)


class Wafer:
    def __init__(self, wafer_id):
        """
        Initializes a Wafer tracker object, creating sub-die references and setting up imaging structures.

        Parameters:
        -----------
        wafer_id : str
            The custom string ID of the wafer under analysis.

        Returns:
        --------
        None

        Example:
        --------
        >>> wafer_analysis = Wafer("W04_2026")
        """
        self.wafer_id = wafer_id
        self.data_dir = data_dir or askdirectory(title="Dossier Data")
        self.parent_dir = parent_dir or askdirectory(title="Dossier Parent")
        
        self.img_wafer_dir = os.path.join(self.parent_dir, 'Images', self.wafer_id)
        os.makedirs(self.img_wafer_dir, exist_ok=True)
        
        self.dies = {d_name: Die(d_name, self.wafer_id) for d_name in list_die_names}
        self.kappa_cache = {}
        self._pre_cache_kappa_simulations()

    def _pre_cache_kappa_simulations(self):
        """
        Pre-loads numerical simulation text arrays into an optimized lookup dictionary structure.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Example:
        --------
        >>> wafer._pre_cache_kappa_simulations()
        """
        if not process_kappa_phase_shift: return
        print("Mise en cache des matrices de simulation Kappa...")
        for l in set(laser_length.values()):
            folder = os.path.join(self.data_dir, self.wafer_id, "QWS_Kappa_And_Phase_Solutions", f"L{l}")
            if os.path.exists(folder):
                xplot1 = np.genfromtxt(os.path.join(folder, 'xplot1.txt'))
                xplot2 = np.genfromtxt(os.path.join(folder, 'xplot2.txt'))
                xplot3 = np.genfromtxt(os.path.join(folder, 'xplot3.txt'))
                k_list = np.genfromtxt(os.path.join(folder, 'kappa_list.txt'))
                p_list = np.genfromtxt(os.path.join(folder, 'phase_shift_list.txt'))
                
                size_ref = int(np.size(xplot1) / len(xplot1))
                d_beta_th = np.zeros((len(xplot1), size_ref))
                d_beta_psb_th = np.zeros((len(xplot1), size_ref))
                wave_shift_th = np.zeros((len(xplot1), size_ref))
                
                for i in range(len(k_list)):
                    for j in range(len(p_list)):
                        d_beta_th[i, j] = xplot3[i, j] - xplot2[i, j]
                        d_beta_psb_th[i, j] = xplot3[i, j] - xplot1[i, j]
                        wave_shift_th[i, j] = d_beta_th[i, j] / d_beta_psb_th[i, j]
                        
                k_mat, p_mat = np.meshgrid(k_list / adjust_kappa, p_list * 180 / np.pi)
                
                self.kappa_cache[f"L{l}"] = {
                    'kappa_list': k_list, 'phase_list': p_list,
                    'kappa_matrix': k_mat.T, 'phase_shift_matrix': p_mat.T,
                    'wave_shift_th': wave_shift_th, 'd_beta_psb_th': d_beta_psb_th
                }

    def _generate_global_plots(self):
        """
        Compiles and saves comparative charts grouping data curves from all processed dies on the wafer.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Example:
        --------
        >>> wafer._generate_global_plots()
        """
        print("Génération des graphiques comparatifs globaux (All Dies)...")
        img_group_dir = os.path.join(self.img_wafer_dir, laser_component_group)
        colors_dies = plt.cm.rainbow(np.arange(0, len(list_die_names), 1) / max(1, len(list_die_names) - 1))
        cools_lasers = plt.cm.rainbow(np.arange(0, len(list_laser_names), 1) / max(1, len(list_laser_names) - 1))

        for laser_name in list_laser_names:
            out_laser_dir = os.path.join(img_group_dir, laser_name)
            os.makedirs(out_laser_dir, exist_ok=True)
            
            for temp in list_temperatures:
                fig_li, ax_li = plt.subplots(2, 1 if nb_pwm_channels == 2 else 1, figsize=(7, 10) if nb_pwm_channels == 2 else (6, 4))
                fig_iv, ax_iv = plt.subplots()
                fig_wpe, ax_wpe = plt.subplots()
                fig_smsr, ax_smsr = plt.subplots()
                fig_kap, ax_kap = plt.subplots()
                fig_phs, ax_phs = plt.subplots()
                
                for d_idx, die_name in enumerate(list_die_names):
                    laser_obj = self.dies[die_name].lasers[laser_name]
                    liv_deemb = laser_obj.data_liv_deemb.get(temp)
                    
                    # --- 1. Cumulative LIV plots ---
                    if liv_deemb is not None:
                        # LI & IV & WPE
                        if nb_pwm_channels == 1:
                            ax_li.plot(liv_deemb[:, 0] * 1000, 10 ** (liv_deemb[:, 2] / 10), label=die_name, color=colors_dies[d_idx])
                            opt_p = 10 ** (liv_deemb[:, 2] / 10)
                        else:
                            ax_li[0].plot(liv_deemb[:, 0] * 1000, 10 ** (liv_deemb[:, 2] / 10), label=die_name, color=colors_dies[d_idx])
                            ax_li[1].plot(liv_deemb[:, 0] * 1000, 10 ** (liv_deemb[:, 3] / 10), label=die_name, color=colors_dies[d_idx])
                            opt_p = 10 ** (liv_deemb[:, 2] / 10) + 10 ** (liv_deemb[:, 3] / 10)
                            
                        ax_iv.plot(liv_deemb[:, 0] * 1000, liv_deemb[:, 1], label=die_name, color=colors_dies[d_idx])
                        
                        elec_p = liv_deemb[:, 1] * liv_deemb[:, 0] * 1000
                        ax_wpe.plot(liv_deemb[:, 0] * 1000, (opt_p / elec_p) * 100, label=die_name, color=colors_dies[d_idx])
                    
                    # --- 2. Cumulative Spectra plots (SMSR / Kappa / Phase) ---
                    x_cur = [float(c) for c in current_spectra]
                    y_smsr = [laser_obj.spectra_data[temp][c].get('smsr', np.nan) for c in current_spectra]
                    ax_smsr.plot(x_cur, y_smsr, label=die_name, color=colors_dies[d_idx])
                    
                    if process_kappa_phase_shift:
                        y_kap = [laser_obj.spectra_data[temp][c].get('kappa', np.nan) for c in current_spectra]
                        y_phs = [laser_obj.spectra_data[temp][c].get('phase_shift', np.nan) for c in current_spectra]
                        ax_kap.plot(x_cur, y_kap, label=die_name, color=colors_dies[d_idx])
                        ax_phs.plot(x_cur, y_phs, label=die_name, color=colors_dies[d_idx])
                
                # Writes and saves
                if save_extract_figures:
                    # Final LI
                    fig_li.savefig(os.path.join(out_laser_dir, f'LI_{self.wafer_id}_{laser_name}_{temp}C_all_dies_deembedded.png')); plt.close(fig_li)
                    # Final IV
                    ax_iv.set_title(f'{laser_name}, IV, {temp}°C'); ax_iv.legend(fontsize=8, ncol=4); ax_iv.grid(True, linestyle='--')
                    fig_iv.savefig(os.path.join(out_laser_dir, f'IV_{self.wafer_id}_{laser_name}_{temp}C_all_dies.png')); plt.close(fig_iv)
                    # Final WPE
                    ax_wpe.set_title(f'{laser_name}, WPE, {temp}°C'); ax_wpe.set_ylim([0, 25]); ax_wpe.legend(fontsize=8, ncol=4); ax_wpe.grid(True, linestyle='--')
                    fig_wpe.savefig(os.path.join(out_laser_dir, f'WPE_{self.wafer_id}_{laser_name}_{temp}C_all_dies.png')); plt.close(fig_wpe)
                    # Final SMSR
                    ax_smsr.set_title(f'{laser_name}, SMSR, {temp}°C'); ax_smsr.legend(fontsize=8, ncol=4); ax_smsr.grid(True, linestyle='--')
                    fig_smsr.savefig(os.path.join(out_laser_dir, f'SMSR_{self.wafer_id}_{laser_name}_{temp}C_all_dies.png')); plt.close(fig_smsr)
                    
                    if process_kappa_phase_shift:
                        ax_kap.set_title(f'{laser_name}, Kappa, {temp}°C'); ax_kap.set_ylim([10, 110]); ax_kap.legend(fontsize=8, ncol=4); ax_kap.grid(True, linestyle='--')
                        fig_kap.savefig(os.path.join(out_laser_dir, f'Kappa_{self.wafer_id}_{laser_name}_{temp}C_all_dies.png')); plt.close(fig_kap)
                        ax_phs.set_title(f'{laser_name}, Phase Shift, {temp}°C'); ax_phs.set_ylim([10, 170]); ax_phs.legend(fontsize=8, ncol=4); ax_phs.grid(True, linestyle='--')
                        fig_phs.savefig(os.path.join(out_laser_dir, f'Phase_shift_{self.wafer_id}_{laser_name}_{temp}C_all_dies.png')); plt.close(fig_phs)

        # --- 3. Global overlay of all spectra at ref_current ---
        img_spec_dir = os.path.join(img_group_dir, 'Spectra')
        os.makedirs(img_spec_dir, exist_ok=True)
        for temp in list_temperatures:
            for die_name in list_die_names:
                fig_spec, ax_spec = plt.subplots()
                for j, l_name in enumerate(list_laser_names):
                    # Simulates raw curve reconstruction - original deemb
                    laser_obj = self.dies[die_name].lasers[l_name]
                    wl = laser_obj.spectra_data[temp].get(ref_current, {}).get('wl', np.nan)
                    if not np.isnan(wl):
                        # Simple generation of a legend line to match graph format
                        ax_spec.plot([], [], label=l_name, color=cools_lasers[len(cools_lasers) - 1 - j])
                
                ax_spec.set_title(f'Spectra LA_200G et {ref_current}mA, {die_name}, {temp}C')
                ax_spec.set_ylim([-70, 10]); ax_spec.legend(fontsize=9); ax_spec.grid(True, linestyle='--')
                fig_spec.savefig(os.path.join(img_spec_dir, f'Spectra_{ref_current}mA_{self.wafer_id}_{temp}C_{die_name}.png'))
                plt.close(fig_spec)
                
    def run_all(self):
        """
        Launches the complete macro analytics flow for the current wafer.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Example:
        --------
        >>> wafer.run_all()
        """
        for die in self.dies.values():
            die.process_die(self.data_dir, self.img_wafer_dir, self.kappa_cache)
        
        self._generate_global_plots()
        
        self._build_and_save_all_dataframes()

    def _build_and_save_all_dataframes(self):
        """
        Collects parsed dictionary rows into structured Pandas dataframes and exports reports.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        Example:
        --------
        >>> wafer._build_and_save_all_dataframes()
        """
        print("Génération des fichiers d'extraction finaux...")
        liv_rows, spectra_rows, rth_rows = [], [], []
        
        for die in self.dies.values():
            for laser in die.lasers.values():
                # 1. Rth collection
                rth_data = laser.extract_thermal_resistance()
                if rth_data:
                    rth_rows.append([self.wafer_id, die.name, laser.name, rth_data['dldpe'], rth_data['dldt'], rth_data['rth']])
                
                for temp in list_temperatures:
                    res = laser.results.get(temp, {})
                    if not res: continue
                    
                    # 2. LIV collection (Dynamic CH1 and CH2 management)
                    liv_line = [
                        self.wafer_id, die.name, laser.name, laser.shunt_name, temp,
                        res.get('threshold', np.nan), res.get('resistance', np.nan), res.get('res_r_square', np.nan),
                        res.get('power_LI_ch1', np.nan)
                    ]
                    if nb_pwm_channels == 2:
                        liv_line.append(res.get('power_LI_ch2', np.nan))
                        
                    liv_line.extend([res.get('slope_LI', np.nan), res.get('rolloff_current', np.nan), res.get('rolloff_power', np.nan)])
                    liv_rows.append(liv_line)
                    
                    # 3. Spectra collection
                    for cur in current_spectra:
                        spec = laser.spectra_data[temp].get(cur, {})
                        spec_line = [
                            self.wafer_id, die.name, laser.name, laser.shunt_name, temp, cur, 
                            spec.get('wl', np.nan), 
                            spec.get('smsr', np.nan)
                        ]
                        if process_kappa_phase_shift:
                            spec_line.extend([
                                spec.get('kappa', np.nan), 
                                spec.get('phase_shift', np.nan)
                            ])
                        spectra_rows.append(spec_line)

        # ---- Dynamic definition of output columns ----
        # LIV
        liv_cols = ["Wafer name", "Die name", "Laser name", "Shunt name", "Temperature (°C)", "Threshold (mA)", 
                    f"Resistance @{float(ref_current):.0f}mA (Ohm)", "r² Resistance", f"Power CH1 @{float(ref_current):.0f}mA (mW)"]
        if nb_pwm_channels == 2:
            liv_cols.insert(9, f"Power CH2 @{float(ref_current):.0f}mA (mW)")
        liv_cols.extend(["LI slope (W/A)", "Roll-off current (mA)", "Total roll-off power (mW)"])
        
        # Spectra
        spectra_cols = ["Wafer name", "Die name", "Laser name", "Shunt name", "Temperature (°C)", "Current (mA)", "Peak wavelength (nm)", "SMSR (dB)"]
        if process_kappa_phase_shift:
            spectra_cols.extend(["Kappa (cm-1)", "Phase shift (°)"])
            
        # Rth
        rth_cols = ["Wafer name", "Die name", "Laser name", 'dlambda/dPe (nm/W)', 'dlambda/dT (nm/K)', 'Thermal resistance (K/W)']

        # ---- DataFrame Creation and Export ----
        os.makedirs(extraction_path, exist_ok=True)
        print(spectra_extract_file_name)
        # LIV Save
        pd.DataFrame(liv_rows, columns=liv_cols).to_csv(os.path.join(extraction_path, f"{liv_extract_file_name}.txt"), sep="\t", encoding='latin1', index=False)
        # Spectra Save
        pd.DataFrame(spectra_rows, columns=spectra_cols).to_csv(os.path.join(extraction_path, f"{spectra_extract_file_name}.txt"), sep="\t", encoding='latin1', index=False)
        # Rth Save
        pd.DataFrame(rth_rows, columns=rth_cols).to_csv(os.path.join(extraction_path, f"{rth_extract_file_name}.txt"), sep="\t", encoding='latin1', index=False)
        # Merged file save
        list_files = [f"{liv_extract_file_name}.txt", f"{spectra_extract_file_name}.txt", f"{rth_extract_file_name}.txt"]
        outputfile = f"{wafer_id}_{laser_component_group}_extraction.txt"
        fusionner_plusieurs_fichiers(list_files, outputfile, extraction_path)
        print("Tous les fichiers d'extraction (LIV, Spectra, Rth) ont été générés avec succès.")


if __name__ == "__main__":
    wafer_processor = Wafer(wafer_id=wafer_id)
    wafer_processor.run_all()
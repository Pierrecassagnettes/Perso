import warnings
import numpy as np
import matplotlib.pyplot as plt

from lib_test import smooth_signal
from scipy.interpolate import interp1d, griddata
from scipy.signal import find_peaks
from scipy.stats import linregress
import pandas as pd


def load_data_file(data_file_path, column_names):
    """
    load a data file as a pandas dataframe
    :param data_file_path: string
        path of the data file to read
    :param column_names: list of strings
        name of the data columns
    :return:
    """
    data = pd.read_csv(data_file_path, sep='\t', comment='#',
                       names=column_names, encoding='latin1')
    return data


def interpolate_z(x_matrix, y_matrix, z_matrix, x_query, y_query, method='linear', debug=True):
    """
    Interpolate Z values for given query points using known X, Y, Z data.

    Parameters:
        x_matrix (matrix-like): Known X coordinates.
        y_matrix (matrix-like): Known Y coordinates.
        z_matrix (matrix-like): Known Z values corresponding to (x_known, y_known).
        x_query (array-like): X coordinates of query points.
        y_query (array-like): Y coordinates of query points.
        method (str): Interpolation method ('linear', 'nearest', 'cubic').

    Returns:
        np.ndarray: Interpolated Z values. Can be Nan if the x and y queried are out of range
    """

    x_known = x_matrix.ravel()  # Convertir en 1D
    y_known = y_matrix.ravel()  # Convertir en 1D
    z_known = z_matrix.ravel()  # Convertir en 1D

    # Known points
    points = np.column_stack((x_known, y_known))

    # Query points
    query_points = np.column_stack((x_query, y_query))

    # Interpolation
    z_interpolated = griddata(points, z_known, query_points, method=method)

    # Check for NaN values (points outside the convex hull)
    if np.any(np.isnan(z_interpolated)):
        print("Warning: Some query points are outside the convex hull of the known data.")

    # Initialisation de la figure et des axes
    if debug is True:
        fig, ax = plt.subplots()
        vmin, vmax = z_matrix.min(), z_matrix.max()
        scatter_known = ax.scatter(x_matrix, y_matrix, c=z_matrix,
                                   s=10, cmap='viridis', vmin=vmin, vmax=vmax)
        ax.scatter(query_points[:, 0], query_points[:, 1], c=z_interpolated, s=10, edgecolor='k',
                   cmap='viridis',  vmin=vmin, vmax=vmax,
                   label=f'X = {query_points[0, 0]:.1f}, Y = {query_points[0, 1]:.3f}')
        # Cosmetics
        fig.colorbar(scatter_known, ax=ax, label=r"$\Phi$ (°)")
        ax.set_xlabel(r"$\kappa$ (cm$^{-1}$)", fontsize=12)
        ax.set_ylabel(r'$\Delta$$\beta$/$\Delta$$\beta_{PSB}$', fontsize=12)
        ax.set_title('Interpolation using griddata', fontsize=14)
        ax.legend()
        ax.set_ylim([0.2, 0.8])
        ax.set_xlim([10, 110])
        ax.set_xticks(np.arange(10, 111, 10))
        ax.grid(True, linestyle='--')
        return z_interpolated, fig, ax
    else:
        return z_interpolated


def get_laser_threshold(current, power, height=0.13, method='second derivative', display=False,
                        min_first_derivative=0.0015):
    """

    Parameters
    ----------

    current : numpy array
        array containing the current of the LI curve in mA
    power : numpy array
        array containing the power of the LI curve of the lasers. It has to be in mW
    height :
    method : string giving the methode to extract the threshold, default : "second derivative"
        "second derivative" : Using the second derivative to compute
    display : boolean
        If True, will display a figure showing how the process is done
    min_first_derivative:
        minimum value of the first derivative 1mA above the thershold current to validate the peak extraction
        when using the 'second derivative refined' method.
    Returns
    ------
    Returns the theshold current. The accuracy is equal to the current step.

    """

    if method == 'second derivative':
        # Calculating the derivatives
        der = np.gradient(smooth_signal(power, window=21))
        der2 = np.gradient(der)
        der2 = der2 / np.max(der2)

        # Searching for the first peak of the second derivative in the LI curve
        peaks, _ = find_peaks(der2, height=height)
        arg_thresh = peaks[0]
        thresh = current[arg_thresh]

        # Checking if it does everything we want if display is True
        if display:
            fig, ax = plt.subplots()
            ax.plot(current, der2 / np.max(der2), label='Second derivative')
            ax.plot(current, power / np.max(power), label='LI')
            ax.scatter(thresh, power[arg_thresh] / np.max(power),
                       color='black', label='Threshold point')
            ax.scatter(current[peaks], der2[peaks] / np.max(der2), label='Peaks')
            ax.legend()

            return thresh, fig, ax
        else:
            return thresh

    elif method == 'second derivative not smoothed':
        # Calculating the derivatives
        der = np.gradient(power)
        der2 = np.gradient(der)
        der2 = der2 / np.max(der2)

        # Searching for the first peak of the second derivative in the LI curve
        peaks, _ = find_peaks(der2, height=height)
        arg_thresh = peaks[0]
        thresh = current[arg_thresh]

        # Checking if it does everything we want if display is True
        if display:
            fig, ax = plt.subplots()
            ax.plot(current, der2 / np.max(der2), label='Second derivative')
            ax.plot(current, power / np.max(power), label='LI')
            ax.scatter(thresh, power[arg_thresh] / np.max(power),
                       color='black', label='Threshold point')
            ax.scatter(current[peaks], der2[peaks] / np.max(der2), label='Peaks')
            ax.legend()
            return thresh, fig, ax
        else:
            return thresh

    elif method == "second derivative refined":
        # Calculating the derivatives
        der = np.gradient(smooth_signal(power, window=21))
        der2 = np.gradient(der)
        der2 = der2 / np.max(der2)

        # Searching for the first peak of the second derivative in the LI curve.
        # A second criteria checks that 1mA above the threshold, the first derivative is above a minimal value
        thresh, arg_thresh = None, None
        peaks, _ = find_peaks(der2, height=height)
        step_current = current[1] - current[0]
        nb_steps_1ma = max(round(1 / step_current), 1)
        for i in range(len(peaks)):
            arg_thresh = peaks[i]
            thresh = current[arg_thresh]
            # check that the optical power after a few points is indeed above a minimal level
            if len(power) >= arg_thresh + nb_steps_1ma:
                if power[arg_thresh + nb_steps_1ma] > min_first_derivative:
                    arg_thresh = peaks[i]
                    break
            else:
                warnings.warn("Unable to detect a threshold current.")

        # Checking if it does everything we want if display is True
        if display:
            fig, ax = plt.subplots()
            ax.plot(current, der2 / np.max(der2), label='Second derivative')
            ax.plot(current, power / np.max(power), label='LI')
            ax.scatter(thresh, power[arg_thresh] / np.max(power),
                       color='black', label='Threshold point')
            ax.scatter(current[peaks], der2[peaks] / np.max(der2), label='Peaks')
            ax.legend()
            return thresh, fig, ax
        else:
            return thresh

    else:
        raise Exception('Method not yet coded')


def get_laser_rolloff(current, power, ignore_ratio=1):
    """
    ----------
    Parameters
    current : numpy array containing the current of the LI curve in mA
    power : numpy array containing the power of the LI curve of the lasers. It has to be in mW
    ignore_ratio : if the rolloff current is higher than the max current applied multiplied by this ratio,
     consider the rolloff extraction not reliable and return nan values
    -------
    Returns the roll off current and power

    """
    current = current[~np.isnan(power)]
    power = power[~np.isnan(power)]
    id_max_power = np.argmax(power)
    if id_max_power + 1 > ignore_ratio * len(current):
        return np.nan, np.nan
    else:
        return current[id_max_power], power[id_max_power]


def get_operational_currents(current, power, min_power):
    """
    ----------
    Parameters
    current : numpy array containing the current of the LI curve in mA
    power : numpy array containing the power of the LI curve of the lasers. It has to be in mW
    min_power : minimum operational power in mW
    -------
    Returns the minimal and maximal currents for wich the optical power is higher than the minimal operational power
        a None value means that no current value lead to a high enough power
        a numpy.nan value means that the maximum / minimum value of the current array still lead to a high enough power,
            making the precise extraction not possible
    """
    if len(current) != len(power):
        raise Exception("ERROR: current and power arrays must have the same length")
    else:
        id_rolloff = np.argmax(power)
        if power[id_rolloff] < min_power:
            max_op_current = None
            min_op_current = None
        else:
            max_op_current = np.nan
            min_op_current = np.nan
            for id_above_rolloff in range(np.argmax(power), len(current)):
                if (power[id_above_rolloff] < min_power) and (power[id_above_rolloff - 1] >= min_power):
                    max_op_current = current[id_above_rolloff - 1]
                    break
            for id_under_rolloff in range(np.argmax(power), -1, -1):
                if (power[id_under_rolloff] < min_power) and (power[id_under_rolloff + 1] >= min_power):
                    min_op_current = current[id_under_rolloff + 1]
                    break

        return min_op_current, max_op_current


def get_laser_resistance(current, voltage, chosen_current, window=0.02, display=False):
    """

    Parameters
    ----------
    current : numpy array
        array containing the current of the IV curve in A
    voltage : numpy array
        array containing the voltage of the IV curve in V
    chosen_current : float
        Current at which we want the resistance of the laser, in A
    window : float
        Window of current where we do the linear regression (+-window)
    display : boolean
        If True, will display a figure showing how the process is done

    -------
    Returns :
        - 2 floats if the method is 'linear fit' :
            - the resistance of the laser at resistance_chosen_current in Ohm
            - the square of the rvalue of the fit
        - 1 float if the method is 'derivative' :
            - the resistance of the laser at resistance_chosen_current in Ohm

    """

    # Getting the range of index where to do the linear fit (+-0.02 A around the point of interest)
    pos = np.where(np.logical_and(current >= chosen_current -
                                  window, current <= chosen_current + window))[0]
    try:
        res = linregress(current[pos], voltage[pos])
        # Getting the resistance
        resistance = res.slope
        r_square = res.rvalue ** 2
        inter = res.intercept
        # Getting the voltage at the chosen current
        f_iv = interp1d(current, voltage)
        volt = f_iv(chosen_current)
    except ValueError as e:
        print(f"error while doing the linear regression of the resistance: {e}")
        resistance = np.nan
        volt = np.nan
        r_square = np.nan
        inter = np.nan
    # Checking if it does everything we want if display is True
    if display:
        fig, ax = plt.subplots()
        ax.scatter(current, voltage, label='Data')
        ax.scatter(current[pos], voltage[pos],
                   label='Data for the fit', color='red')
        ax.plot([chosen_current, chosen_current], [min(voltage),
                                                   max(voltage)], label='Current of wanted resistance', color='green')
        ax.plot(current, current * resistance + inter,
                label=f'Fit : R = {resistance:.1f}' + r'$\Omega$' + f', r² = {r_square:.3f}', color='black')
        ax.set_title(
            f'Linear fit done at {chosen_current * 1000:.0f}mA,\nVoltage : {volt:.2f}V')
        ax.legend()
        ax.grid(True, linestyle='--')
        ax.set_xlabel('Current (A)')
        ax.set_ylabel('Voltage (V)')

        return [resistance, volt, r_square], fig, ax

    return [resistance, volt, r_square]


def get_laser_LI_slope(current,
                       power,
                       threshold,
                       threshold_step=0.01,
                       window=0.005,
                       display=False):
    """

    Parameters
    ----------
    current : numpy array
        array containing the current of the IV curve in A
    power : numpy array
        array containing the power in mW
    threshold : float
        Threshold current of the laser
    threshold_step : float
        Step of current above which we do the center of the linear regression
    window : float
        Window of current where we do the linear regression (+-window)
    display : boolean
        If True, will display a figure showing how the process is done

    -------
    Returns
        1 float which is the slope of the LI curve close to the threshold

    """

    # Getting the range of index where to do the linear fit (+-0.005 A around the point of interest)
    # The point of interest is by default 10mA above the threshold current
    chosen_current = threshold + threshold_step
    pos = np.where(np.logical_and(current >= chosen_current -
                                  window, current <= chosen_current + window))[0]
    res = linregress(current[pos], power[pos])
    # Getting the slope of the LI curve
    slope_LI = res.slope/1000
    r_square = res.rvalue ** 2

    # Checking if it does everything we want if display is True
    if display:
        fig, ax = plt.subplots()
        ax.scatter(current, power, label='Data')
        ax.scatter(current[pos], power[pos],
                   label='Data for the fit', color='red')
        ax.plot([chosen_current, chosen_current], [min(power),
                                                   max(power)], label='Current of wanted resistance', color='green')
        ax.plot(current, current * res.slope + res.intercept,
                label=f'Fit : dL/dI = {slope_LI:.2f} W/A, r² = {r_square:.3f}', color='black')
        ax.set_title(
            f'Linear fit done at {chosen_current * 1000:.0f}mA')
        ax.legend()
        ax.grid(True, linestyle='--')
        ax.set_xlabel('Current (A)')
        ax.set_ylabel('Power (mW)')

        if r_square < 0.98:
            slope_LI = np.nan
        return slope_LI, fig, ax
    else:
        if r_square < 0.98:
            slope_LI = np.nan
        return slope_LI


def get_frequency_peak(wavelength, power):
    """
    extracts the frequency peak of the spectra. Does node detect multimodes.
    :param wavelength: array of the wavelengths
    :param power: array of the measured power, either in mW or dB
    :return:
        freq_max_spectrum: the frequency in Hz corresponding to the main peak
        power_max_spectrum: the power (in the same unit as the "power" parameter) corresponding to the peak
    """
    id_max_spectrum = np.argmax(power)
    power_max_spectrum = power[id_max_spectrum]
    c = 299792458  # vitesse de la lumière dans le vide, en m/s
    freq_max_spectrum = c / wavelength[id_max_spectrum]
    return freq_max_spectrum, power_max_spectrum


def get_laser_smsr(spectra, display=False):
    """
    extract the side-mode suppression ratio (SMSR) from a spectrum data of a laser.
    Parameters
    ----------
    spectra : numpy array
        Contains the data of the spectra in dBm
    display : boolean
        If True, will display a figure showing how the process is done
    Returns
    -------
    The SMSR of the laser

    """

    peaks, properties = find_peaks(spectra, height=-80, distance=15)
    pos = np.argsort(properties['peak_heights'])
    les_max = np.sort(properties['peak_heights'])
    if len(les_max) <= 1:
        print("Less than 2 peaks detected : unable to extract the SMSR.")
        smsr = None
        if display:
            fig, ax = plt.subplots()
            ax.plot(spectra)
            ax.scatter(peaks, spectra[peaks])
            ax.set_title(f'Less than 2 peaks detected : unable to extract the SMSR.')
            ax.legend()
            ax.grid(True, linestyle='--')
            ax.set_xlabel('Sample number')
            ax.set_ylabel('Power on OSA (dB)')
            ax.set_ylim(bottom=-75)
            fig.tight_layout()
            return smsr, fig, ax
        else:
            return smsr
    else:
        first_max_pow = les_max[-1]
        second_max_pow = les_max[-2]
        smsr = first_max_pow - second_max_pow

        if display:
            fig, ax = plt.subplots()
            ax.plot(spectra)
            ax.scatter(peaks, spectra[peaks])
            ax.scatter(peaks[pos[-1]], first_max_pow,
                       label=f'Peak at {first_max_pow:.2f}dB', color='black')
            ax.scatter(peaks[pos[-2]], second_max_pow,
                       label=f'Peak at {second_max_pow:.2f}dB', color='red')
            ax.set_title(f'SMSR computed : {smsr:.2f}dB')
            ax.legend()
            ax.grid(True, linestyle='--')
            ax.set_xlabel('Sample number')
            ax.set_ylabel('Power on OSA (dB)')
            ax.set_ylim(bottom=-75)
            fig.tight_layout()
            return smsr, fig, ax
        else:
            return smsr


def create_interpolate_fn_gc(coupler_data_file_path):
    # Getting the GC data
    data_gc = np.genfromtxt(coupler_data_file_path, delimiter="\t")
    # Creating the interpolation function
    f_gc = interp1d(data_gc[:, 0], data_gc[:, 1] / 2, kind="linear")
    return f_gc

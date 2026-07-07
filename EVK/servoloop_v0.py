from ScintilAPI import *
 
import argparse
import logging
import matplotlib.pyplot as plt
import math
import os
import time

logging.getLogger().setLevel(logging.INFO)

LASER_BUFFER_SIZE = 512
LASER_SAMPLE_RATE = 312500 #312.5 KHz
FFT_SIZE = 2048
FFT_FS = 625000

class RingBuffer:
    """ Class that implements a not-yet-full buffer. """
    def __init__(self, bufsize):
        self.bufsize = bufsize
        self.data = []

    class __Full:
        """ Class that implements a full buffer. """
        def add(self, x):
            """ Add an element overwriting the oldest one. """
            self.data[self.currpos] = x
            self.currpos = (self.currpos+1) % self.bufsize
        def get(self):
            """ Return list of elements in correct order. """
            return self.data[self.currpos:]+self.data[:self.currpos]

    def add(self,x):
        """ Add an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.bufsize:
            # Initializing current position attribute
            self.currpos = 0
            # Permanently change self's class from not-yet-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data

def convert_frequency_to_nbr_periods(frequency):
    return round(frequency * LASER_BUFFER_SIZE / LASER_SAMPLE_RATE)

##@cond
def getDefaultServer():
    if "SDK___TEMPLATE_HTTP_SERVER" in os.environ:
        return os.environ["SDK___TEMPLATE_HTTP_SERVER"]
    return "127.0.0.1"

def getDefaultPort():
    if "SDK___TEMPLATE_HTTP_PORT" in os.environ:
        return os.environ["SDK___TEMPLATE_HTTP_PORT"]
    return 80
##@endcond

def servoloop_enable_lasers(api: ScintilHAL, module: scintil_hal_module_t, lasers_init: dict) -> ScintilError:
    logging.info("Setting lasers initial currents...")
    logging.info("Lasers initial currents: " + str(lasers_init))
    for laser in scintil_hal_laser_t:
        if laser != scintil_hal_laser_t.SCINTIL_HAL_LASER_ALL:
            ret = api.scintil_hal_laser_set_current(module, laser, lasers_init[laser.name])
            if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
                return ret["errcode"]
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE

def servoloop_enable_muxes(api: ScintilHAL, module: scintil_hal_module_t, muxheaters_init: dict) -> ScintilError:
    logging.info("Setting mux heaters initial voltages...")
    logging.info("Mux heaters initial voltages: " + str(muxheaters_init))

    for mux in scintil_hal_mux_heater_t:
        if mux == scintil_hal_mux_heater_t.SCINTIL_HAL_MUX_HEATER_LAST:
            break
        ret = api.scintil_hal_mux_heater_set_voltage(module, mux, muxheaters_init[mux.name])
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE

def servoloop_wait_for_temperature_stability(api: ScintilHAL, module: scintil_hal_module_t, temp_stability_channel: str, temp_diff: float, timeout: int) -> ScintilError:
    circular_buffer = RingBuffer(20)
    
    logging.info("Waiting for temperature stability...")
    logging.info("Used channel is {}".format(temp_stability_channel))
    logging.info("Temperature difference threshold: " + str(temp_diff) + " °C")
    logging.info("Timeout: " + str(timeout) + "s")

    while timeout > 0:
        if temp_stability_channel == "TEC":
            ret = api.scintil_hal_tec_get_object_temp(module)
        else:
            ret = api.scintil_hal_temperature_module_get_val(module)
        
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        
        circular_buffer.add(ret["temperature"])
        
        print(f"\rCurrent temperature :{ret["temperature"]}°C", end="", flush=True)

        if len(circular_buffer.get()) == 20:
            # Buffer is full, we can check stability
            min_temp = min(circular_buffer.get())
            max_temp = max(circular_buffer.get())

            if max_temp - min_temp < temp_diff:
                return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
        time.sleep(1)
        timeout -= 1
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API

def servoloop_tune_mux(api: ScintilHAL, module: scintil_hal_module_t, mux: scintil_hal_mux_heater_t, v_start: float, v_stop: float, n_steps: int, mpd_response_delay = 0.1) -> ScintilError:
    error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
    
    logging.info("Start Tuning MUX: " + mux.name)
    logging.info("Starting voltage: " + str(v_start) + " V")
    logging.info("Stopping voltage: " + str(v_stop) + " V")
    logging.info("Nbs steps: " + str(n_steps))
    
    mpd_mux = []
    heater_sweep_data = []
    
    # Create array of values using quadratic spacing for this sweep
    for i in range(n_steps):
    
        t = i / (n_steps - 1)
        val = v_start*v_start + t * (v_stop*v_stop - v_start*v_start)
        heater_sweep_data.append(math.sqrt(val))
    
    logging.info("Heater sweep data: " + str(heater_sweep_data))

    for i in range(n_steps):
        # Use quadractic stepping
        v = heater_sweep_data[i]
        print("\rSetting voltage :{:.2f} V".format(v), end="", flush=True)
        ret = api.scintil_hal_mux_heater_set_voltage(module, mux, v)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            logging.error("Error while setting MUX heater voltage: " + str(ret["errcode"]))
            return ret["errcode"]
        
        # Wait mpd_response_delay ms
        time.sleep(mpd_response_delay)
        
        ret = api.scintil_hal_mux_heater_get_mpd_stage_voltage(module, mux)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            logging.error("Error while getting MUX MPD stage voltage: " + str(ret["errcode"]))
            return ret["errcode"]
        mpd_mux.append(ret["voltage"])
    
    # Find the voltage that gives the best MPD response (max voltage)
    max_mpd = max(mpd_mux)
    max_index = mpd_mux.index(max_mpd)
    best_v = heater_sweep_data[max_index]
    ret = api.scintil_hal_mux_heater_set_voltage(module, mux, best_v)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while setting MUX heater voltage: " + str(ret["errcode"]))
        return ret["errcode"]

    plt.plot(heater_sweep_data, mpd_mux)
    plt.xlabel("Heater Voltage (V)")
    plt.ylabel("MPD Stage Voltage (V)")
    plt.title(f"MUX Heater {mux.name} Tuning")
    plt.show()

    logging.info(f"Best Heater voltage for MUX {mux.name} is: {best_v:.2f} V with MPD response: {max_mpd:.3f} V")

    return error

def servoloop_tune_muxes(api: ScintilHAL, module: scintil_hal_module_t, v_start: float, v_stop: float, n_steps: int, mpd_response_delay = 0) -> ScintilError:
    error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
    start_time = time.time()
    for mux in reversed(scintil_hal_mux_heater_t):
        if mux.value < scintil_hal_mux_heater_t.SCINTIL_HAL_MUX_HEATER_LAST.value:
            error = servoloop_tune_mux(api, module, mux, v_start, v_stop, n_steps, mpd_response_delay)
            if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
                return error
    end_time = time.time()
    logging.info("Tuning of all Muxes tooks {}s".format(end_time - start_time))
    return error

def servoloop_tune_ring_coarse(api: ScintilHAL, module: scintil_hal_module_t, v_start: float, v_stop: float, n_steps: int, fft_bin: int, mpd_response_delay = 0.1) -> ScintilError:

    logging.info("Start Tuning RING")
    logging.info("Starting voltage: " + str(v_start) + " V")
    logging.info("Stopping voltage: " + str(v_stop) + " V")
    logging.info("Nbs steps: " + str(n_steps))
    
    fft_powers = []
    
    heater_sweep_data = []
    
    # Create array of values using quadratic spacing for this sweep
    for i in range(n_steps):
    
        t = i / (n_steps - 1)
        val = v_start*v_start + t * (v_stop*v_stop - v_start*v_start)
        heater_sweep_data.append(math.sqrt(val))
    
    logging.info("Heater sweep data: " + str(heater_sweep_data))
    
    for i in range(n_steps):
        # Use quadractic stepping
        v = heater_sweep_data[i]
        print("\rSetting voltage :{:.2f} V".format(v), end="", flush=True)
        ret = api.scintil_hal_ring_heater_set_voltage(module, v)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            logging.error("Error while setting RING heater voltage: " + str(ret["errcode"]))
            return ret["errcode"]
        
        # Wait mpd_response_delay ms
        time.sleep(mpd_response_delay)
        
        # Get FFT Fundamental Power
        ret = api.scintil_hal_fft_fpga_sample(module, fft_bin + 1) # FFT FPGA bins are shifted by 1 bin
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        fft_powers.append(ret["data"])
        
    max_power = max(fft_powers)
    max_index = fft_powers.index(max_power)
    best_v = heater_sweep_data[max_index]
    ret = api.scintil_hal_ring_heater_set_voltage(module, best_v)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while setting RING heater voltage: " + str(ret["errcode"]))
        return ret["errcode"]
    
    plt.plot(heater_sweep_data, fft_powers)
    plt.xlabel("Heater Voltage (V)")
    plt.ylabel("FFT magnitude")
    plt.title(f"RING Heater Coarse Tuning")
    plt.show()

    logging.info(f"Best Heater voltage for RING is: {best_v:.2f} V with fft magnitude: {max_power:.3f} V")
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
    
def servoloop_tune_ring_fine(api: ScintilHAL, module: scintil_hal_module_t, ring_conf: dict) -> ScintilError:
     
    v_step = ring_conf["Fine_Vstep"]
    cpt = 0
    
    # Get current phase
    ret = api.scintil_hal_fft_get_laser_phase(module, scintil_hal_laser_t.SCINTIL_HAL_LASER_0)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    current_phase_sign = 1 if ret["phase"] >= 0 else -1
    
    # Get current v_ring
    ret = api.scintil_hal_ring_heater_get_voltage(module)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    current_v = ret["val"]
    
    while v_step > ring_conf["RING_STEP_THRESHOLD"] and cpt < ring_conf["RING_FINE_TUNING_MAX_TRIES"]:
        # Try increasing v_ring
        current_v += v_step * current_phase_sign
        ret = api.scintil_hal_ring_heater_set_voltage(module, current_v)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        
        # Wait 2ms
        # No need in python since API takes time to send and receive response
        
        # Get new phase
        ret = api.scintil_hal_fft_get_laser_phase(module, scintil_hal_laser_t.SCINTIL_HAL_LASER_0)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        new_phase_sign = 1 if ret["phase"] >= 0 else -1
        
        if new_phase_sign != current_phase_sign:
            # If the sign is different, we are going in the wrong direction, we need to decrease v_step and change direction
            v_step = v_step/2
            current_phase_sign = new_phase_sign
        
        cpt += 1
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE

def servoloop_laser_enable_dithering(api: ScintilHAL, module: scintil_hal_module_t, laser: scintil_hal_laser_t, frequency: float, amplitude: float):
    
    logging.info("Enable dithering on Laser {} with frequency {} Hz and amplitude {} A".format(laser.name, frequency, amplitude))
    period = convert_frequency_to_nbr_periods(frequency)
    ret = api.scintil_hal_laser_configure_AWG_from_period(module, laser, period, amplitude, 0)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error enabling dithering")
        return ret["errcode"]

    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
    
def servoloop_tune_ring(api: ScintilHAL, module: scintil_hal_module_t, laser: scintil_hal_laser_t, ring_conf: dict, frequency: float, amplitude: float) -> ScintilError:
    error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
    
    # Enable dithering on laser
    error = servoloop_laser_enable_dithering(api, module, laser, frequency, amplitude)
    
    # Tune Ring Coarse
    error = servoloop_tune_ring_coarse(api, module, ring_conf)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return error

    # Wait 2ms
    # No need in python since API takes time to send and receive response
    
    # Tune Ring Fine
    error = servoloop_tune_ring_fine(api, module, ring_conf)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return error
    
    # Disable dithering on laser
    ret = api.scintil_hal_laser_set_dither_state(module, laser, False)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    
    return error

def servoloop_tune_laser_coarse(api: ScintilHAL, module: scintil_hal_module_t, laser: scintil_hal_laser_t, laser_conf: dict) -> ScintilError:
    # Enable dithering on laser
    period = convert_frequency_to_nbr_periods(laser_conf["d_frequency"])
    amplitude = laser_conf["d_amplitude"]
    ret = api.scintil_hal_laser_configure_AWG_from_period(module, laser, period, amplitude, 0)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    
    i_start = laser_conf["I_Start"]
    i_stop = laser_conf["I_Stop"]
    i_step = laser_conf["I_Step"]
    
    fft_powers = []
    
    while i_start <= i_stop:
        ret = api.scintil_hal_laser_set_current(module, laser, i_start)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        
        # Wait 2ms
        # No need in python since API takes time to send and receive response
        
        # Get FFT Fundamental Power
        ret = api.scintil_hal_fft_get_laser_magnitude(module, laser)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        fft_powers.append(ret["magnitude"])
        
        i_start += i_step
    
    # Set laser to current corresponding to max power
    max_power = max(fft_powers)
    max_index = fft_powers.index(max_power)
    best_i = laser_conf["I_Start"] + max_index * laser_conf["I_Step"]
    ret = api.scintil_hal_laser_set_current(module, laser, best_i)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    
    # Disable dithering on laser
    ret = api.scintil_hal_laser_set_dither_state(module, laser, False)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
    
def servoloop_tune_laser_fine(api: ScintilHAL, module: scintil_hal_module_t, laser: scintil_hal_laser_t, laser_conf: dict, laser_fine_tuning_max_tries: int) -> ScintilError:
    
    i_current = api.scintil_hal_laser_get_applied_current(module, laser)
    i_step = laser_conf["Fine_Istep"]
    # Enable dithering on laser
    period = convert_frequency_to_nbr_periods(laser_conf["d_frequency"])
    amplitude = laser_conf["d_amplitude"]
    ret = api.scintil_hal_laser_configure_AWG_from_period(module, laser, period, amplitude, 0)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    
    cpt = 0
    
    while cpt < laser_fine_tuning_max_tries:
        # Get FFT Phase
        ret = api.scintil_hal_fft_get_laser_phase(module, scintil_hal_laser_t.SCINTIL_HAL_LASER_0)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        phase = ret["phase"]
        
        if phase > 90:
            i_current -= i_step
        else:
            i_current += i_step
        
        # Set laser current
        ret = api.scintil_hal_laser_set_current(module, laser, i_current)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        
        # Check convergance
        # TO DO
        
        cpt += 1
    
    # Disable dithering on laser
    ret = api.scintil_hal_laser_set_dither_state(module, laser, False)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
        
def servoloop_tune_lasers_and_ring(api: ScintilHAL, module: scintil_hal_module_t, lasers_conf: dict, ring_conf: dict, laser_fine_tuning_max_tries: int) -> ScintilError:
    ref_laser = scintil_hal_laser_t.SCINTIL_HAL_LASER_0
    
    error = servoloop_tune_ring(api, module, ref_laser, ring_conf, lasers_conf[ref_laser.name])
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return error
    
    # Tune ring for each laser
    ring_final_values = []
    for laser in lasers_conf:
        if laser == scintil_hal_laser_t.SCINTIL_HAL_LASER_ALL:
            continue
        error = servoloop_tune_ring(api, module, laser, ring_conf, lasers_conf[laser.name])
        if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return error
        
        # Get ring final value
        ret = api.scintil_hal_ring_heater_get_voltage(module)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return ret["errcode"]
        ring_final_values.append(ret["val"])
    
    # Search for minimum and maximum ring final values
    min_ring = min(ring_final_values)
    max_ring = max(ring_final_values)
    mid_ring = (min_ring + max_ring) / 2
    
    # Set ring to the middle value
    ret = api.scintil_hal_ring_heater_set_voltage(module, mid_ring)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]
    
    # Tune coarse lasers
    for laser in scintil_hal_laser_t:
        error = servoloop_tune_laser_coarse(api, module, laser, lasers_conf[laser.name])
        if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return error
    
    # Tune fine lasers
    for laser in scintil_hal_laser_t:
        error = servoloop_tune_laser_fine(api, module, laser, lasers_conf[laser.name], laser_fine_tuning_max_tries)
        if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            return error
    
    # Check all lasers converged
    # TO DO
    
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE

def servoloop_configuration(
        api: ScintilHAL, 
        module: scintil_hal_module_t, 
        lasers_init: dict, 
        muxheaters_init: dict, 
        ring_heater_init: float,
        vpolar_las_init: float,
        vpolar_ring_init: float,
        tec_setpoint: float,
        temp_stability_channel: str,
        temp_stability_diff: float,
        temp_stability_timeout: int,
    ) -> ScintilError:
    
    logging.info("Starting servoloop configuration...")
    start_time = time.time()
    
    # Power VLaser and lasers
    ret = api.scintil_hal_sys_enable(True)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while enabling sys: " + str(ret["errcode"]))
        return ret["errcode"]  

    # Configure TEC
    logging.info("Configuring TEC to {}°C".format(tec_setpoint))
    ret = api.scintil_hal_tec_set_target_object_temp(module, tec_setpoint)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while configuring TEC Temperature: " + str(ret["errcode"]))
        return error 

    # Power on lasers
    error = servoloop_enable_lasers(api, module, lasers_init)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while enabling lasers: " + str(error))
        return error 
    
    # Power on Muxes
    error = servoloop_enable_muxes(api, module, muxheaters_init)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while enabling MUXes: " + str(error))
        return error

    # Power on Ring
    logging.info("Setting ring heater initial voltage with value: " + str(ring_heater_init) + " V")
    ret = api.scintil_hal_ring_heater_set_voltage(module, ring_heater_init)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while setting ring heater voltage: " + str(ret["errcode"]))
        return ret["errcode"]  
    
    # Power on VPolar for MPD
    logging.info("Setting MUX laser vpolar initial voltage with value: " + str(vpolar_las_init) + " V")
    ret = api.scintil_hal_vpolar_set_out_val(scintil_hal_vpolar_out_t.SCINTIL_HAL_VPOLAR_OUT_LAS, vpolar_las_init)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while setting MUX laser vpolar voltage: " + str(ret["errcode"]))
        return ret["errcode"] 
    
    logging.info("Setting MUX ring vpolar initial voltage with value: " + str(vpolar_ring_init) + " V")
    ret = api.scintil_hal_vpolar_set_out_val(scintil_hal_vpolar_out_t.SCINTIL_HAL_VPOLAR_OUT_RING, vpolar_ring_init)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while setting MUX ring vpolar voltage: " + str(ret["errcode"]))
        return ret["errcode"] 
    
    # Check temperature stability
    error = servoloop_wait_for_temperature_stability(api, module, temp_stability_channel, temp_stability_diff, temp_stability_timeout)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        logging.error("Error while waiting for temperature stability: " + str(error))
        return error 
    
    logging.info("Servoloop configuration completed successfully.")
    
    end_time = time.time()
    logging.info("Configuration and temperature stability of {} tooks {}s".format(module.name, end_time - start_time))
    
    return error

def servoloop_init(
        api: ScintilHAL, 
        module: scintil_hal_module_t, 
        lasers_conf: dict, 
        muxes_conf: dict, 
        ring_conf: dict,
        vpolar_las_init : float,
        vpolar_ring_init : float,
        temp_stability_diff : float,
        temp_stability_timeout : int,
        laser_fine_tuning_max_tries : int
    ) -> ScintilError:
    
    error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE

    error = servoloop_configuration(api, module, lasers_conf, muxes_conf, ring_conf, vpolar_las_init, vpolar_ring_init, temp_stability_diff, temp_stability_timeout)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return error

    # Wait 10ms
    # No need in python since API takes time to send and receive response

    # Tune MUXs
    error = servoloop_tune_muxes(api, module, muxes_conf)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return error
    
    # Tune Lasers and Ring
    error = servoloop_tune_lasers_and_ring(api, module, lasers_conf, ring_conf, laser_fine_tuning_max_tries)
    if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return error
    
    # Power off Ring
    ret = api.scintil_hal_ring_heater_set_voltage(module, 0)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"]  
    
    return error

def servoloop_mux_one_step(
    api: ScintilHAL, 
    module: scintil_hal_module_t, 
    mux: scintil_hal_mux_heater_t, 
    mux_conf: dict, 
    correction_sign: int) -> tuple [ScintilError, int]:
    
    # Get Mux Heater current voltage
    ret = api.scintil_hal_mux_heater_get_voltage(module, mux)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"], correction_sign
    start_voltage = ret["voltage"]
    
    v_step = mux_conf["Servoloop_Vstep"]
    
    # Measure AC signal of MPD Mux
    ret = api.scintil_hal_mux_heater_get_mpd_stage_voltage(module, mux)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"], correction_sign
    tab_acq_0 = ret["voltage"]
    
    # Set Mux Heater with new voltage
    api.scintil_hal_mux_heater_set_voltage(module, mux, start_voltage + correction_sign * v_step)
    
    # Sleep 400us
    # No need in python since API takes time to send and receive response
    
    # Measure New AC signal of MPD Mux
    ret = api.scintil_hal_mux_heater_get_mpd_stage_voltage(module, mux)
    if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
        return ret["errcode"], correction_sign
    tab_acq_1 = ret["voltage"]
    
    if tab_acq_1 < tab_acq_0:
        # Reverse correction sign
        correction_sign *= -1
        
        # Set Mux Heater with old voltage
        api.scintil_hal_mux_heater_set_voltage(module, mux, start_voltage)
        
    return scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE, correction_sign

def servoloop_muxes(api: ScintilHAL, module: scintil_hal_module_t, muxes_conf: dict) -> ScintilError:
    correction_signs = {}
    mpd_mux_buffers = {}
    mux_lock = {}
    
    while True:
        for mux in scintil_hal_mux_heater_t:
            if mux < scintil_hal_mux_heater_t.SCINTIL_HAL_MUX_HEATER_LAST:
                mux_name = mux.name
                if mux_name not in correction_signs:
                    correction_signs[mux_name] = 1
                
                error, correction_signs[mux_name] = servoloop_mux_one_step(api, module, mux, muxes_conf[mux_name], correction_signs[mux_name])
                if error != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
                    return error
                
                # Store MPD Mux value
                if mux_name not in mpd_mux_buffers:
                    mpd_mux_buffers[mux_name] = RingBuffer(20)
                
                ret = api.scintil_hal_mux_heater_get_mpd_stage_voltage(module, mux)
                if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
                    return ret["errcode"]
                mpd_mux_buffers[mux_name].add(ret["voltage"])
                
                # Check convergance
                if len(mpd_mux_buffers[mux_name].get() == 20):
                    # Buffer is full, we can check stability
                    min_mpd_val = min(mpd_mux_buffers[mux_name].get())
                    max_mpd_val = max(mpd_mux_buffers[mux_name].get())

                    if max_mpd_val - min_mpd_val < muxes_conf[mux_name]["tab_crit_lock_mux"]:
                        mux_lock[mux_name] = True
                    else:
                        mux_lock[mux_name] = False

def connect_to_server(server: str, port: int) -> ScintilHAL:
    logging.info(f"Connecting to Scintil HTTP Server {server}:{port}")
    api = ScintilHAL(server, port, strictcutversion=False)
    return api          
        

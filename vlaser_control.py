from ScintilAPI import *
 
import argparse
import logging
import os
import sys
import time

import numpy as np

def generate_periodic_sine_array(amplitude=1.0, frequency=1.0, sampling_rate=1000, phase=0):
    # Number of samples per period
    samples_per_period = int(sampling_rate / frequency)
    
    t = np.linspace(0, 1, samples_per_period, endpoint=False)
    
    # Generate the sine wave
    y = amplitude * np.sin(2 * np.pi * t + phase)
    return y

 
##@cond
def getDefaultServer():
    if "SDK___TEMPLATE_HTTP_SERVER" in os.environ:
        return os.environ["SDK___TEMPLATE_HTTP_SERVER"]
    return "127.0.0.1"

def getDefaultLockToken():
    if "SDK___TEMPLATE_HTTP_LOCK_TOKEN" in os.environ:
        return os.environ["SDK___TEMPLATE_HTTP_LOCK_TOKEN"]
    return ""

def getDefaultPort():
    if "SDK___TEMPLATE_HTTP_PORT" in os.environ:
        return os.environ["SDK___TEMPLATE_HTTP_PORT"]
    return 80
##@endcond
 
def main():
 
    logging.getLogger().setLevel(logging.INFO)
 
    parser = argparse.ArgumentParser()
 
    parser.add_argument("--server", help="Scintil HTTP server address or name",  default=getDefaultServer())
    parser.add_argument("--port", help="Scintil HTTP server port",  default=getDefaultPort())
    parser.add_argument("--token", help="Scintil HTTP lock token", default=getDefaultLockToken())
    args = parser.parse_args()
 
    logging.info(f"Connecting to Scintil HTTP Server {args.server}:{args.port}")
 
    # Instantiate API
    api = ScintilHAL(args.server, args.port, strictcutversion=False)
 
    if args.token:
        api.setToken(args.token)
    
    module = scintil_hal_module_t.MODULE_1
    channel = scintil_hal_laser_t.SCINTIL_HAL_LASER_0
    amplitude = 0.02
    
    sine_values = generate_periodic_sine_array(amplitude=amplitude, frequency=1, sampling_rate=512)
    sine_values = [round((sine_value + amplitude).item(), 3) for sine_value in sine_values]
    
    api.scintil_hal_vlaser_enable(True)
    api.scintil_hal_laser_configure_AWG(module, channel, sine_values)
 
 
main()
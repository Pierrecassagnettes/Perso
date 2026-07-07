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
 
    error_none = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
 
    # Instantiate API
    api = ScintilHAL(args.server, args.port, strictcutversion=False)
 
    if args.token:
        api.setToken(args.token)
    
    print(api.scintil_hal_temperature_get_val(scintil_hal_temp_t.SCINTIL_HAL_TEMPERATURE_INTERPOSER_2))

    
 
 
main()
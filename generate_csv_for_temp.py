from ScintilAPI import *
 
import argparse
import csv
import logging
import os
import sys
import time

import numpy as np
 
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

def get_api_function_return_value(api:ScintilHAL, function_name:str, return_attribute:str, *args):
    func = getattr(api, function_name)
    if not func:
        logging.error(f"Function {function_name} not found in API")
        return None
    try:
        ret = func(*args)
        if ret["errcode"] != scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE:
            logging.error(f"Error calling function {function_name}: {ret['errcode']}")
            return None
        return ret[return_attribute]
    except Exception as e:
        logging.error(f"Error calling function {function_name}: {e}")
        return None


def generate_csv_temp(api:ScintilHAL, module: scintil_hal_module_t, laser: scintil_hal_laser_t, duration: int, refresh_rate: int = 1):
    # Time origin
    origin_time = time.time()
    
    data = {
        
    }
    
    # Create CSV file with specific columns "Applied Current", "Mainboard Temperature"
    for column in ["Applied Current", "Mainboard Temperature (°C)", "Interposer Temperature (°C)", "TEC Cold Temperature (°C)", "TEC Target (°C)"]:
        data[column] = {
            "time": [],
            "value": []
        }
    
    while time.time() - origin_time < duration:
        start_time = time.time()
        
        # Get applied Current
        applied_current = get_api_function_return_value(api, "scintil_hal_laser_get_applied_current", "current", module, laser)
        if applied_current is not None:
            data["Applied Current"]["time"].append(time.time() - origin_time)
            data["Applied Current"]["value"].append(applied_current)
        
        # Get mainboard temperature
        mainboard_temp = get_api_function_return_value(api, "scintil_hal_temperature_get_val", "temperature", scintil_hal_temp_t.SCINTIL_HAL_TEMPERATURE_MAINBOARD)
        if mainboard_temp is not None:
            data["Mainboard Temperature (°C)"]["time"].append(time.time() - origin_time)
            data["Mainboard Temperature (°C)"]["value"].append(mainboard_temp)
        
        # Get interposer temperature
        interposer_temp = get_api_function_return_value(api, "scintil_hal_temperature_module_get_val", "temperature", module)
        if interposer_temp is not None:
            data["Interposer Temperature (°C)"]["time"].append(time.time() - origin_time)
            data["Interposer Temperature (°C)"]["value"].append(interposer_temp)
        
        # Get TEC cold temperature
        tec_cold_temp = get_api_function_return_value(api, "scintil_hal_tec_get_object_temp", "temperature", module)
        if tec_cold_temp is not None:
            data["TEC Cold Temperature (°C)"]["time"].append(time.time() - origin_time)
            data["TEC Cold Temperature (°C)"]["value"].append(tec_cold_temp)
        
        # Get TEC target temperature
        tec_target_temp = get_api_function_return_value(api, "scintil_hal_tec_get_target_object_temp", "temperature", module)
        if tec_target_temp is not None:
            data["TEC Target (°C)"]["time"].append(time.time() - origin_time)
            data["TEC Target (°C)"]["value"].append(tec_target_temp)
        
        # Sleep until next refresh
        elapsed_time = time.time() - start_time
        if elapsed_time < refresh_rate:
            time.sleep(refresh_rate - elapsed_time)
    
    # Save data to CSV file
    with open("temperature_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        # Build header with alternating "Time (s)" and column names
        header = []
        for column_name in data.keys():
            header.append("Time (s)")
            header.append(column_name)
        writer.writerow(header)
        
        # Find maximum number of rows
        max_rows = max(len(data[col]["time"]) for col in data.keys())
        
        # Build and write data rows
        for row_idx in range(max_rows):
            row = []
            for column_name in data.keys():
                # Write time value
                if row_idx < len(data[column_name]["time"]):
                    row.append(f"{data[column_name]['time'][row_idx]:.3f}")
                else:
                    row.append("")  # Empty if no data for this row
                
                # Write value
                if row_idx < len(data[column_name]["value"]):
                    row.append(data[column_name]["value"][row_idx])
                else:
                    row.append("")  # Empty if no data for this row
            
            writer.writerow(row) 
 
def main():
 
    logging.getLogger().setLevel(logging.INFO)
 
    parser = argparse.ArgumentParser()
 
    parser.add_argument("--server", help="Scintil HTTP server address or name",  default=getDefaultServer())
    parser.add_argument("--port", help="Scintil HTTP server port",  default=getDefaultPort())
    parser.add_argument("--module", help="Module idx", type=int, default=1)
    parser.add_argument("--laser", help="Laser idx", type=int, default=0)
    parser.add_argument("--duration", help="Duration in seconds", type=int, default=10)
    parser.add_argument("--refresh-rate", help="Refresh rate in seconds", type=int, default=1)
    args = parser.parse_args()
 
    logging.info(f"Connecting to Scintil HTTP Server {args.server}:{args.port}")
 
    error_none = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_NONE
 
    # Instantiate API
    api = ScintilHAL(args.server, args.port, strictcutversion=False)
 
    generate_csv_temp(api, scintil_hal_module_t(args.module - 1), scintil_hal_laser_t(args.laser), duration=args.duration, refresh_rate=args.refresh_rate)

 
main()
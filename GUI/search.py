import os 
import pandas as pd

folder = r"W:\50-DEVELOPMENT\TEST\Temporary data database\Data\D24S0697_21\LeafLight\50C\LA1\raw_data"
files = os.listdir(folder)

for file in files :
    if file.endswith(".txt"):
        print("wsh")
        filepath = os.path.join(folder, file)
        df_txt = pd.read_csv(filepath, sep="\t")
        values = pd.to_numeric(df_txt["Power__dBm"])
        for value in values :
            if float(value)== -14.11 :
                print(file)
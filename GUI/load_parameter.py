

import os
from numpy import sort
import pandas as pd



def lire_dossier(chemin_dossier):
    noms_fichiers = []
    laser_names = set()  

    for fichier in os.listdir(chemin_dossier):
        if fichier.endswith(".txt"):
            chemin_fichier = os.path.join(chemin_dossier, fichier)
            noms_fichiers.append(fichier)

            try:
                df = pd.read_csv(chemin_fichier, sep="\t")  

                if "Laser name" in df.columns:
                    laser_names.update(df["Laser name"].dropna().unique())
                elif "TLM name" in df.columns:
                    laser_names.update(df["TLM name"].dropna().unique())
                elif "Structure name" in df.columns:
                    laser_names.update(df["Structure name"].dropna().unique())
            except UnicodeDecodeError:
                df = pd.read_csv(chemin_fichier, encoding="cp1252", sep="\t")
                if "Laser name" in df.columns:
                    laser_names.update(df["Laser name"].dropna().unique())
                elif "TLM name" in df.columns:
                    laser_names.update(df["TLM name"].dropna().unique())
                elif "Structure name" in df.columns:
                    laser_names.update(df["Structure name"].dropna().unique())
            except Exception as e:
                print(f"Erreur avec {fichier} : {e}")

    return sorted(list(laser_names))




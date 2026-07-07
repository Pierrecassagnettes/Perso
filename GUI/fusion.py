import os


def fusionner_plusieurs_fichiers(liste_fichiers, fichier_sortie, path):
    if not liste_fichiers:
        return

    os.chdir(path)

    # --- ETAPE 1 : Lister toutes les colonnes uniques globales ---
    colonnes_globales = []
    for nom_fichier in liste_fichiers:
        try:
            # Détection rapide de l'encodage juste pour l'en-tête
            try:
                with open(nom_fichier, "r", encoding="utf-8-sig") as f:
                    premiere_ligne = f.readline()
            except UnicodeDecodeError:
                with open(nom_fichier, "r", encoding="cp1252") as f:
                    premiere_ligne = f.readline()

            if not premiere_ligne:
                continue

            # Découpage et nettoyage des colonnes de ce fichier
            colonnes = [col.strip() for col in premiere_ligne.split("\t")]
            for col in colonnes:
                if "Temperature" in col:
                    col = "Temperature (C)"
                elif "Resistance" in col and "@" not in col:
                    col = "R2 Resistance"

                # On garde la colonne si elle n'est pas vide et pas déjà enregistrée
                if col and col not in colonnes_globales:
                    colonnes_globales.append(col)
        except Exception:
            continue

    if not colonnes_globales:
        print("Aucune colonne trouvée.")
        return

    # --- ETAPE 2 : Aligner et écrire les lignes les unes après les autres ---
    with open(fichier_sortie, "w", encoding="utf-8") as f_out:
        # On écrit l'en-tête global tout en haut du fichier final
        f_out.write("\t".join(colonnes_globales) + "\n")

        for nom_fichier in liste_fichiers:
            try:
                # Choix dynamique de l'encodage pour le fichier en cours
                encodage = "utf-8-sig"
                try:
                    with open(nom_fichier, "r", encoding=encodage) as f:
                        f.readline()
                except UnicodeDecodeError:
                    encodage = "cp1252"

                # Lecture de toutes les lignes du fichier
                with open(nom_fichier, "r", encoding=encodage) as f:
                    lignes = f.readlines()

                if len(lignes) <= 1:
                    continue  # Fichier vide ou juste un en-tête

                # Extraction et nettoyage de l'en-tête spécifique à ce fichier
                entete_origine = [col.strip() for col in lignes[0].split("\t")]
                entete_nettoye = []
                for col in entete_origine:
                    if "Temperature" in col:
                        col = "Temperature (C)"
                    elif "Resistance" in col and "@" not in col:
                        col = "R2 Resistance"
                    entete_nettoye.append(col)

                # Traitement des lignes de données (on saute la ligne 0)
                for ligne in lignes[1:]:
                    # Sécurité : on ignore les vraies lignes complètement vides du fichier
                    if not ligne.strip():
                        continue

                    valeurs = [val.strip() for val in ligne.split("\t")]

                    # On crée un dictionnaire de correspondance : Colonne -> Valeur pour CETTE ligne
                    dict_ligne = {}
                    for i, val in enumerate(valeurs):
                        if i < len(entete_nettoye):
                            dict_ligne[entete_nettoye[i]] = val

                    # On reconstruit la ligne en suivant SCRICTEMENT l'ordre des colonnes globales
                    ligne_ordonnee = []
                    for col_globale in colonnes_globales:
                        # Si la colonne existe pour cette ligne, on met sa valeur, sinon on laisse vide
                        ligne_ordonnee.append(dict_ligne.get(col_globale, ""))

                    # Écriture brute de la ligne alignée
                    f_out.write("\t".join(ligne_ordonnee) + "\n")

            except Exception as e:
                print(f"Erreur lors du traitement du fichier {nom_fichier} : {e}")


# --- Ton script de parcours de dossiers reste identique ---
root_data = r"W:\50-DEVELOPMENT\TEST\Temporary data database\Data"

for folder in os.listdir(root_data):
    folder_path = os.path.join(root_data, folder)
    if os.path.isdir(folder_path) and folder.startswith("D2"):
        wafer_name = folder
        path = os.path.join(root_data, wafer_name, "Processing_results")

        if not os.path.exists(path):
            continue

        files = []
        for file in os.listdir(path):
            if file.endswith(".txt") and "DOE_laser" not in file and "lasers_DOE" in file:
                if "LIV" in file or "Rth" in file or "Spectra" in file:
                    files.append(file)

        file_out = os.path.join(path, f"{wafer_name}_DOE_laser_extraction.txt")
        fusionner_plusieurs_fichiers(files, file_out, path)
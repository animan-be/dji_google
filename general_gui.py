import os
import re
from tkinter import Tk, filedialog, messagebox

# Expression régulière pour détecter les coordonnées
coord_pattern = re.compile(r"\[latitude:\s*(-?\d+\.\d+)\]\s*\[longitude:\s*(-?\d+\.\d+)\]")

# Fonction pour écrire le fichier KML
def ecrire_fichier_kml(nom_fichier_kml, points):
    print(f"Écriture dans le fichier KML : {nom_fichier_kml}")
    with open(nom_fichier_kml, "w") as fichier_kml:
        fichier_kml.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        fichier_kml.write("<kml xmlns='http://www.opengis.net/kml/2.2'>\n")
        fichier_kml.write("  <Document>\n")
        fichier_kml.write(f"    <name>{os.path.basename(nom_fichier_kml)}</name>\n")
        
        for nom_fichier_srt, latitude, longitude in points:
            fichier_kml.write("    <Placemark>\n")
            fichier_kml.write(f"      <name>{nom_fichier_srt}</name>\n")
            fichier_kml.write(f"      <Point>\n")
            fichier_kml.write(f"        <coordinates>{longitude},{latitude},0</coordinates>\n")
            fichier_kml.write("      </Point>\n")
            fichier_kml.write("    </Placemark>\n")
        
        fichier_kml.write("  </Document>\n")
        fichier_kml.write("</kml>\n")

# Fonction pour vérifier si les coordonnées sont valides
def coordonnees_valides(latitude, longitude):
    return latitude != "0.000000" and longitude != "0.000000"

# Fonction principale
def generer_kml():
    print("Début du programme")
    Tk().withdraw()  # Cacher la fenêtre principale Tkinter
    
    # Demander le dossier à scanner
    print("Ouverture du sélecteur de dossier...")
    dossier = filedialog.askdirectory(title="Sélectionnez le dossier à scanner")
    if not dossier:
        print("Aucun dossier sélectionné.")
        messagebox.showwarning("Aucun dossier sélectionné", "Vous devez sélectionner un dossier.")
        return
    print(f"Dossier sélectionné : {dossier}")
    
    # Demander où enregistrer le fichier KML
    print("Ouverture du sélecteur pour enregistrer le fichier...")
    fichier_kml = filedialog.asksaveasfilename(
        title="Enregistrer le fichier KML",
        defaultextension=".kml",
        filetypes=[("Fichier KML", "*.kml")]
    )
    if not fichier_kml:
        print("Aucun fichier sélectionné pour enregistrer le KML.")
        messagebox.showwarning("Aucun fichier sélectionné", "Vous devez choisir où enregistrer le fichier KML.")
        return
    print(f"Fichier KML sélectionné : {fichier_kml}")
    
    # Liste pour stocker les premiers points valides
    premiers_points_valides = []
    
    # Scanner le dossier pour trouver des fichiers .srt
    print("Début du scan des fichiers...")
    for racine, _, fichiers in os.walk(dossier):
        for nom_fichier in fichiers:
            if nom_fichier.lower().endswith(".srt"):  # Ignorer la casse
                chemin_fichier = os.path.join(racine, nom_fichier)
                print(f"Lecture du fichier : {chemin_fichier}")
                try:
                    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
                        contenu = fichier.read()
                        coordonnees = coord_pattern.findall(contenu)
                        
                        if coordonnees:
                            # Chercher le premier point valide
                            for latitude, longitude in coordonnees:
                                if coordonnees_valides(latitude, longitude):
                                    print(f"Point valide trouvé : {latitude}, {longitude}")
                                    premiers_points_valides.append((nom_fichier, latitude, longitude))
                                    break  # Trouver seulement le premier point valide
                except Exception as e:
                    print(f"Erreur en lisant {chemin_fichier}: {e}")
    
    # Créer le fichier KML si des points valides ont été trouvés
    if premiers_points_valides:
        print("Écriture des points dans le fichier KML...")
        ecrire_fichier_kml(fichier_kml, premiers_points_valides)
        print("Fichier KML généré avec succès.")
        messagebox.showinfo("Succès", f"Fichier KML généré avec succès :\n{fichier_kml}")
    else:
        print("Aucun point valide trouvé.")
        messagebox.showwarning("Aucun point valide trouvé", "Aucun fichier SRT valide n'a été trouvé dans le dossier sélectionné.")

# Appeler la fonction principale
if __name__ == "__main__":
    generer_kml()

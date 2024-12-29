# README - Programme "General GUI"

//** Description **//

Le programme ""General GUI"" est un outil pratique créé pour afficher les premiers points GPS valides à partir des fichiers SRT générés par un drone (uniquement tester sur le DJI Mini 3 Pro). Ces points GPS sont ensuite enregistrés dans un fichier KML, qui peut être visualisé dans Google Earth ou tout autre outil compatible KML. Cela permet de faciliter la recherche de la bonne vidéo sur une carte.
__________________________

//** Formats valides **//

Le programme recherche des coordonnées GPS dans les fichiers SRT sous le format suivant :
Latitude et Longitude : un nombre décimal pouvant être positif ou négatif, au format: 12.345678 (six décimales ou moins après le point sont attendues).
Conditions supplémentaires :
Les coordonnées doivent apparaître sur une seule ligne dans le fichier SRT, avec le mot-clé latitude: suivi de longitude:.
Les valeurs latitude et longitude: 0.000000 sont ignorées, car elles ne représentent pas de position valide.
Si vos fichiers SRT contiennent des valeurs dans un format différent, le programme ne les détectera pas comme valides. Assurez vous que vos fichiers respectent ces critères.
--------
Exemples de formats acceptés :
latitude: 45.123456 longitude: -73.987654
latitude: -12.456789 longitude: 140.123456
latitude: 0.100000 longitude: -0.200000 (valeurs non nulles et valides).
--------
______________________________________

//** Fonctionnalités principales **//

1. **Sélection de dossier** :
   - Une fenêtre s'ouvre pour permettre à l'utilisateur de choisir le dossier à scanner (y compris les sous-dossiers).
   
2. **Extraction de coordonnées GPS** :
   - Le programme recherche les fichiers SRT dans le dossier sélectionné.
   - Il extrait les premières coordonnées valides (latitude et longitude) de chaque fichier SRT.
   - Les coordonnées où latitude et longitude sont « 0.000000 » sont ignorées.

3. **Enregistrement au format KML** :
   - Une fenêtre s'ouvre pour permettre à l'utilisateur de choisir où enregistrer le fichier KML.
   - Chaque point KML contient le nom du fichier SRT d'origine et ses coordonnées GPS.

_____________________________________

//** Instructions d'utilisation **//

1. Ouvrez une console (Terminal ou PowerShell).
2. Exécutez le fichier Python avec la commande suivante:
	python general_gui.py
3. Suivez les étapes suivantes :
   - Une première fenêtre s'ouvre pour sélectionner le dossier contenant les fichiers SRT.
   - Une seconde fenêtre s'ouvre pour choisir l'emplacement et le nom du fichier KML à générer.
4. Une fois le processus terminé :
   - Si des points valides ont été trouvés, un message de succès s'affiche.
   - Si aucun point valide n'a été trouvé, un message d'avertissement apparaît.

__________________________

## Structure des fichiers
- **general_gui.py** : Le script principal du programme.
- **Fichier KML généré** : prêts à être visualisés dans Google Earth.

__________

## Limitations
- Le programme ne traite que les fichiers SRT.
- Seules les premières coordonnées valides de chaque fichier sont extraites.

__________

## Aide et support
Pour toute question ou problème, n'hésitez pas à demander de l'aide 

__________

www.Animan.be

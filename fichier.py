import os
import sys

# Utilisation : python3 fichier.py fichier.pdf

# Bibliothèque a utiliser : pip install pypdf2

# Sous dossier contenant les fichier PDF à analyser
sous_dossier = sys.argv[1]
# Tableau des noms des fichiers à analyser
tableau_des_PDF = os.listdir(sous_dossier)
print(tableau_des_PDF)                              # Afficher les tableaux

# Concertir d'abord les fichiers PDF en txt via pdftotext
for x in tableau_des_PDF:
    os.exec("")

    # Traiter le fait que le sous-dossier existe déjà
try:
    os.mkdir("Apres_Analyse")
except:
    os.rmdir("")

    # for (x in tableau_des_PDF):

    # f = open('')
    # f.write()
    # f.close()

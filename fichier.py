import os
import sys

# Utilisation : python3 fichier.py dossier_contenant_les_fichiers txt

# Sous dossier contenant les fichier TXT à analyser
sous_dossier = sys.argv[1]




                # ETAPE 1 : RECUPERER LE NOM DES FICHIERS DU DOSSIER CONTENANT LES FICHIERS EN .TXT

tableau_des_TXT = os.listdir(sous_dossier)                          # Tableau contenant les nom des fichiers avec le .txt du sous_dossier
tableau_des_TXT_sans_le_txt = [""] * len(tableau_des_TXT)           # Déclaration et initialisation d'un autre tableau (voir )
# print(tableau_des_TXT)

for i in range(len(tableau_des_TXT)) :
    tableau_des_TXT_sans_le_txt[i] = tableau_des_TXT[i][:-4]

# A partir de maintenant, chaque element du tableau "tableau_des_TXT_sans_le_txt" ne contient plus le ".txt"
# print(" ")
# print(tableau_des_TXT_sans_le_txt)




                # ETAPE 2 : ECRIRE LES FICHIERS DANS UN DOSSIER


    # Traiter le fait que le sous-dossier existe déjà
# try:
#     os.mkdir("Apres_Analyse")
# except:
#     os.rmdir("")

    # for (x in tableau_des_PDF):

    # f = open('')
    # f.write()
    # f.close()

import os
import sys

# Utilisation : python3 fichier.py dossier_contenant_les_fichiers txt

# Sous dossier contenant les fichier TXT à analyser
# sous_dossier = sys.argv[1]


# Récupérer le nom des fichiers du dossier contenant les fichiers en .txt
def RecupNamesOfThePdfFiles(path):
    print("Récupération des titres des PDF dans un tableau")
    tableau_des_TXT = os.listdir(path)                                  # Tableau contenant les nom des fichiers du sous_dossier AVEC le ".txt"
    return tableau_des_TXT

def DeleteDotTxtFromAStringTable(table):
    tableau_des_TXT_sans_le_txt = [""] * len(table)                     # Tableau contenant les nom des fichiers du sous_dossier SANS le ".txt" 
    for i in range(len(table)) :
        tableau_des_TXT_sans_le_txt[i] = table[i][:-4]
    return tableau_des_TXT_sans_le_txt

# Supprimer le dossier Apres_Analyse s'il existe, le créer après vérification
def CreateAfterDeleteDirectory():
    if os.path.exists("Apres_Analyse"):
        os.remove("Apres_Analyse")
        print("'Apres_Analyse' directory deleted")
    # Création du dossier "Apres_Analyse"
    os.mkdir("Apres_Analyse")
    print("'Apres_Analyse' directory created")

# Supprimer les espaces des String d'un tableau de String
def SuppSpacesFromStringTables(stringTable):
    print("Suppression des espaces des String d'un tableau de String")
    for i in range(len(stringTable)):
        stringTable[i] = SuppSpacesFromString(stringTable[i])
    return stringTable

# Supprimer les espaces d'un String
def SuppSpacesFromString(name: str):
    print("Suppression des espaces d'un String")
    name.replace(" ", "_")
    return name

# Créer tous les fichiers d'un tableau ayant le même nom sans les espaces
def CreateFiles(tableauDesTxtSansLeTxt):
    print("Création des fichiers")
    for i in range(len(tableauDesTxtSansLeTxt)):
        nom = tableauDesTxtSansLeTxt[i]+".txt"
        f = open("Apres_Analyse/"+nom, "x")         # Création du fichier dans le dossier "Apres_Analyse"

# Récupérer le titre d'un fichier txt
def RecupTitle(fichier):
    print("Récupération du titre d'un fichier")

# Récupérer l'abstract d'un fichier
def RecupAbstract(fichier):
    keyword = ["Introduction", "INTRODUCTION", "introduction", "Keyword", "keyword", "Keywords", "keywords", "PACS", "pacs"]
    print("Récupération des résumés de l'auteur")
    word = "Abstract"
    nb_abstract_line = 0
    
    # Chercher la ligne où se situe le mot Abstract
    file = open(fichier, "r")
    for line in file:
        nb_abstract_line += 1
        if word in line:
            print("ABSTRACT found ! Line : ")
            print(nb_abstract_line)
            break
    file.close()
    
    # Chercher la ligne où se situe le mot KeyWord
    nb_keyword_line = 0
    file = open(fichier, "r")
    found = False

    for line in file:
        if found == True:
            break
        nb_keyword_line += 1
        for i in range(len(keyword)):
            if found == True:
                break
            if keyword[i] in line:
                print("KEYWORD found ! Line : ")
                print(nb_keyword_line)
                found = True

    with open(fichier, "r") as f:
        lines = f.readlines()[nb_abstract_line:nb_keyword_line-2]
        for line in lines:
            print(line, end="")
    # nb_abstract_line est maintenant la ligne où le asbtract se situe
    file.close()

    
def RecupTitlesInATable(path):
    print("Récupération des titres des fichiers txt du dossier "+path+" insérés dans un tableau")
    tableauDesFichiers = os.listdir(path)
    for i in range(len(tableauDesFichiers)) :
        print("Récupération des titres")




# On parcourt chaque fichier du dossier "Pdftotext"
# i = 0                               # Pour parcourir le tableau tableau_des_TXT_sans_le_txt en même temps que le tableau tableau_des_TXT
# for x in tableau_des_TXT:
    
#     f = open(x)
    
#     f.write()


# for x in tableau_des_PDF:
#     f = open('')
#     f.write()
#     f.close()

RecupAbstract("test.txt")
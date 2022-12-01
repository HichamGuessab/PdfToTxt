import os
import sys
import shutil
import re
# Récupérer le nom des fichiers du dossier contenant les fichiers en .txt
def recupNamesOfTheTxtFiles(path):
    #print("Récupération des titres des PDF dans un tableau")
    tableau_des_TXT = os.listdir(path)                                  # Tableau contenant les nom des fichiers du sous_dossier AVEC le ".txt"
    return tableau_des_TXT

def deleteDotTxtFromAStringTable(table):
    tableau_des_TXT_sans_le_txt = [""] * len(table)                     # Tableau contenant les nom des fichiers du sous_dossier SANS le ".txt" 
    for i in range(len(table)) :
        tableau_des_TXT_sans_le_txt[i] = table[i][:-4]
    return tableau_des_TXT_sans_le_txt

# Supprimer le dossier Apres_Analyse s'il existe, le créer après vérification
def createAfterDeleteDirectory(folderName: str):
    if os.path.exists(folderName):
        shutil.rmtree(folderName)
        print(folderName+" directory deleted")
    # Création du dossier folderName
    os.mkdir(folderName)
    print(folderName+" directory created")

# Supprimer les espaces des String d'un tableau de String
def suppSpacesFromStringTables(stringTable):
    # print("Suppression des espaces des String d'un tableau de String")
    for i in range(len(stringTable)):
        stringTable[i] = suppSpacesFromString(stringTable[i])
    return stringTable

# Supprimer les espaces d'un String
def suppSpacesFromString(name: str):
    # print("Suppression des espaces d'un String")
    name.replace(" ", "_")
    return name

# Créer tous les fichiers d'un tableau ayant le même nom sans les espaces
def createFileInAFolder(fileName: str, folderName: str):
    print("Création du fichier : "+fileName + "dans le directory :" + folderName)
    # for i in range(len(tableauDesTxtSansLeTxt)):
    nom = fileName+".txt"
    f = open(folderName+"/"+nom, "x")         # Création du fichier dans le dossier "Apres_Analyse"
    f.close()

def recupIntroduction(fichier):
    characters = ["Introduction", "INTRODUCTION", "I NTRODUCTION"]
    finalCharacters = ["2.", "2", "II.", "II"]
    introductionLine = 1
    file = open(fichier, 'r', encoding="ascii", errors='ignore')
    for line in file :
        if any(x in line for x in characters):
            break
        introductionLine += 1
    endOfIntroduction = introductionLine
    for line in file:
        endOfIntroduction += 1
        if(len(line) > 3):
            if any(x in line[0] for x in finalCharacters):
                if(not line[1].isdigit()):
                    break
            elif any(x in line[1] for x in finalCharacters):
                if(not line[2].isdigit()):
                    break
            elif line[0] == "I":
                line = line.split()
                if any(x in line[0] for x in finalCharacters):
                    break
    file.close()
    print(endOfIntroduction)
    file = open(fichier, 'r', encoding="ascii", errors='ignore')
    intro = file.readlines()[introductionLine:endOfIntroduction-1]
    file.close()
    return intro

def recupReferences(fichier):
    characters = ["References", "REFERENCES"]
    referenceLine = 1
    file = open(fichier, 'r', encoding="ascii", errors='ignore')
    numLine = 1
    for line in file :
        if any(x in line for x in characters):
            referenceLine = numLine
        numLine += 1
    file.close()
    file = open(fichier, 'r', encoding="ascii", errors='ignore')
    references = file.readlines()[referenceLine:numLine-1]
    file.close()
    print(references)
    return references


path = "Pdftotext/"
tab = recupNamesOfTheTxtFiles(path)
for file in tab:
    print(file)
    recupReferences("Pdftotext/"+file)

#lines = file.readlines()[introductionLine:endOfIntroduction-1]

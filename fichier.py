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
    keyword = ["Introduction", "INTRODUCTION","I NTRODUCTION", "introduction", "Keyword", "keyword", "Keywords", "keywords", "PACS", "pacs"]
    # print("Récupération des résumés de l'auteur")
    word1 = "Abstract"
    word2 = "ABSTRACT"
    nb_abstract_line = 0
    
    # Chercher la ligne où se situe le mot "Abstract"
    abstractFound = False
    j = 0
    file = open(fichier, "r")
    for line in file:
        nb_abstract_line += 1
        if word1 in line or word2 in line:
            # print("ABSTRACT found ! Line : ")
            # print(nb_abstract_line)
            abstractFound = True
            break
    file.close()
    
    # Chercher la ligne où se situe le KeyWord
    nb_keyword_line = 0
    file = open(fichier, "r")
    keywordFound = False

    for line in file:
        if keywordFound == True:
            break
        nb_keyword_line += 1
        for i in range(len(keyword)):
            if keywordFound == True:
                break
            if keyword[i] in line:
                # print("KEYWORD keywordFound ! Line : ")
                # print(nb_keyword_line)
                keywordFound = True

# nb_abstract_line est maintenant la ligne où le asbtract se situe
# nb_keyword_line est maintenant la ligne où le keyword se situe
    # On doit traiter le cas où le mot "Abstract" n'est pas présent
    # if(abstractFound == True):
    with open(fichier, "r") as f:
        lines = f.readlines()[nb_abstract_line-1:nb_keyword_line-2]
        tableau_base = [""] * len(lines)
        i = 0
        # stocker toutes les lignes dans un tableau
        for line in lines:
            tableau_base[i] = line
            i+=1
    # else:
    #     with open(fichier, "r") as f:
    #         lines = f.readlines()[nb_keyword_line-2:nb_abstract_line-1]
    #         tableau_base = [""] * len(lines)
    #         i = 0
    #         # stocker toutes les lignes dans un tableau
    #         for line in lines:
    #             tableau_base[i] = line
    #             i+=1
    # file.close()

    # Localisation des index des lignes où il n'y a rien au début (tableau de booleans)
    x = 0
    tableau_index = [0] * len(tableau_base)
    for i in range(len(tableau_base)):
        if(tableau_base[i][0:15]=="               "):
            # print("hey")
            x+=1
            tableau_index[i] = 1                 # ranger les index qui ne sont pas bon dans un tableau
    
    # Suppression des lignes où il y a des espaces au début
    d = 0
    for v in range(len(tableau_index)):
        if(tableau_index[v]==1):
            tableau_base.pop(d)
        else:
            d += 1
    # print("AVANT suppression des lignes")
    # for i in range(len(tableau_base)):
    #     print(tableau_base[i])
    
    # Suppression des espaces au début de toutes les lignes    
    # print("Tableau sans espaces au début")
    for i in range(len(tableau_base)):
        tableau_base[i] = tableau_base[i].lstrip()
    # Suppression de la fin des lignes à partir de là où il y a 5 espaces
    # Trouver l'index 
    num_line_tab = 0                        # le numéro de la ligne (dans le tableau)
    i = 0
    for i in range(len(tableau_base)):
        num_line_tab+=1
        index = tableau_base[i].find("         ")
        # print("Ligne : ", num_line_tab)
        # print("Espaces trouvées index :", index)
        tableau_base[i] = tableau_base[i][:index]
        
    # print("APRES suppression des lignes d'après")
    for i in range(len(tableau_base)):
        print(tableau_base[i])

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

x = os.listdir("Pdftotext")
for i in x:
    print("--------------------------------------------------------")
    print(i)
    print("--------------------------------------------------------")
    RecupAbstract("Pdftotext/"+i)
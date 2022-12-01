import os
import sys
import shutil
import re
# from xml_file import *

# Récupérer le nom des fichiers du dossier contenant les fichiers en .txt
def RecupNamesOfTheTxtFiles(path):
    print("Récupération des titres des PDF dans un tableau")
    tableau_des_TXT = os.listdir(path)                                  # Tableau contenant les nom des fichiers du sous_dossier AVEC le ".txt"
    return tableau_des_TXT

def DeleteDotTxtFromAStringTable(table):
    tableau_des_TXT_sans_le_txt = [""] * len(table)                     # Tableau contenant les nom des fichiers du sous_dossier SANS le ".txt" 
    for i in range(len(table)) :
        tableau_des_TXT_sans_le_txt[i] = table[i][:-4]
    return tableau_des_TXT_sans_le_txt

# Supprimer le dossier Apres_Analyse s'il existe, le créer après vérification
def CreateAfterDeleteDirectory(folderName: str):
    if os.path.exists(folderName):
        shutil.rmtree(folderName)
        print(folderName+" directory deleted")
    # Création du dossier folderName
    os.mkdir(folderName)
    print(folderName+" directory created")

# Supprimer les espaces des String d'un tableau de String
def SuppSpacesFromStringTables(stringTable):
    # print("Suppression des espaces des String d'un tableau de String")
    for i in range(len(stringTable)):
        stringTable[i] = SuppSpacesFromString(stringTable[i])
    return stringTable

# Supprimer les espaces d'un String
def SuppSpacesFromString(name: str):
    # print("Suppression des espaces d'un String")
    name.replace(" ", "_")
    return name

# Créer tous les fichiers d'un tableau ayant le même nom sans les espaces
def CreateFileInAFolder(fileName: str, folderName: str):
    print("Création du fichier : "+fileName + "dans le directory :" + folderName)
    # for i in range(len(tableauDesTxtSansLeTxt)):
    nom = fileName+".txt"
    f = open(folderName+"/"+nom, "x")         # Création du fichier dans le dossier "Apres_Analyse"
    f.close()
    
def supp_start_spaces_from_lines_(table):
    # Suppression des espaces au début de toutes les lignes    
    # print("Tableau sans espaces au début")
    for i in range(len(table)):
        table[i] = table[i].lstrip() 
    return table

def supp_void_lines_from_table(table):
    # Trouver l'index 
    num_line_tab = 0                        # le numéro de la ligne (dans le tableau)
    i = 0
    for i in range(len(table)):
        num_line_tab+=1
        index = table[i].find("                                   ")
        # print("Ligne : ", num_line_tab)
        # print("Espaces trouvées index :", index)
        table[i] = table[i][:index]
    return table

# NE SERT PLUS A RIEN
# Avant nous servait à supprimer les lignes qui n'avaient rien à voir avoir notre texte (option -layout)
def supp_lines_from_tables_if_x_spaces_at_start(table):
    # Localisation des index des lignes où il n'y a rien au début (tableau de booleans)
    x = 0
    tableau_index = [0] * len(table)
    for i in range(len(table)):
        if(table[i][0:15]=="               "):
            # print("hey")
            x+=1
            tableau_index[i] = 1                 # ranger les index qui ne sont pas bon dans un tableau
    
    # Suppression des lignes où il y a des espaces au début
    d = 0
    for v in range(len(tableau_index)):
        if(tableau_index[v]==1):
            table.pop(d)
        else:
            d += 1
    return table
    
# Fonction qui ne sert plus à rien : On la garde au cas où
def supp_lines_from_table_after_5_spaces(table):
    # Suppression de la fin des lignes à partir de là où il y a 5 espaces
    # Trouver l'index 
    num_line_tab = 0                        # le numéro de la ligne (dans le tableau)
    i = 0
    for i in range(len(table)):
        num_line_tab+=1
        index = table[i].find("         ")
        # print("Ligne : ", num_line_tab)
        # print("Espaces trouvées index :", index)
        table[i] = table[i][:index]
    return table

# Recupérer le titre d'un fichier (!= nom d'un fichier)
def RecupTitle(fichier):
    connectors = ["with", "without", "of", "for", "An ", "OF"] # Mots de liaisons
    skipCharacters = ["From", "Journal", "Submitted"] # Mot qui ne font pas parti du titre
    file1 = open(fichier, 'r')
    titre = ""
    global nb_title_line
    nb_title_line = 0

    ligne = file1.readline()
    ligne_v = ligne
    nb_title_line += 1
    liste = list(ligne.split(" ")) # Récupérer la ligne sous forme de liste pour comparer les mots
    taille = len(liste)
            
    # Tant que je trouve un mot pas bon je passe à la prochaine ligne
    # Si la prochaine est un saut de ligne, je passe à la prochaine ligne
    diffWord = False
    while(diffWord == False):
        if any(x in liste[0] for x in skipCharacters): # Si on rencontre un caractère qui ne fait pas parti du titre
            ligne = file1.readline() # Passer à la ligne suivante
            liste = list(ligne.split(" "))
            nb_title_line += 1

            while(not ligne.strip()): # Tant qu'on rencontre des lignes vides, on passe aux suivantes
                ligne = file1.readline()
                liste = list(ligne.split(" "))
                nb_title_line += 1
        else:
            diffWord = True

    titre += ligne # Ajout de la première ligne de titre
    liste = list(ligne.split(" "))
    taille = len(liste)
    if any(x in liste[taille-1] for x in connectors): # Si on rencontre un connecteur à la fin de la première ligne
        ligne = file1.readline() # On passe à la ligne suivante
        titre+=ligne # On ajoute la ligne suivante au titre (suite du titre)
        nb_title_line += 1
    else :
        ligne = file1.readline() # Sinon on passe à la ligne suivante 
        if any(x in ligne for x in connectors): # Si on rencontre un connecteur dans la deuxième ligne
            titre+=ligne # On ajoute la ligne suivante au titre (suite du titre)
            nb_title_line += 1
    file1.close()
    
    finalTitre = ""
    for t in titre.split(): # On ajoute les éléments du tableau contenant tout les mots du titre dans notre titre final
        finalTitre+=t
        finalTitre+=" "
    # print(finalTitre)
    return finalTitre

# Récupérer l'abstract d'un fichier
def RecupAbstract(fichier):
    keyword = ["Introduction", "INTRODUCTION","I NTRODUCTION", "introduction"]
    # print("Récupération des résumés de l'auteur")
    word1 = "Abstract"
    word2 = "ABSTRACT"
    global nb_abstract_line 
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
    global nb_keyword_line
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
    if(abstractFound == True):
        with open(fichier, "r") as f:
            lines = f.readlines()[nb_abstract_line-1:nb_keyword_line-2]
            tableau_base = [""] * len(lines)
            i = 0
            # stocker toutes les lignes dans un tableau
            for line in lines:
                tableau_base[i] = line
                i+=1
    else:
        with open(fichier, "r") as f:
            # On a notre ligne Introduction (nb_keyword_line) mais pas notre mot clé "Abstract"
            # Faut maintenant stocker dans une liste en remontant le keyword 
            lines = f.readlines()[0:nb_keyword_line-1]
            tableau_base = [""] * len(lines)
            i = 0
            # stocker toutes les lignes dans un tableau
            for line in lines:
                tableau_base[i] = line
                i+=1
    file.close()

    # Traitement du cas où le mot clé "abstract" n'a pas été trouvé
    if(abstractFound == False):
        # print("Abstract non trouvé")
        # print(nb_keyword_line)
        j = 0
        for i in range(len(tableau_base)):
            if(tableau_base[i]=="\n"):
            #     j+=1
            #     if (tableau_base[i+1]=="\n"):
            #         j+=1
            #     else:
            #         j=0
            # if(j == 2):
                nb_abstract_line = i+1
                # print("oula", i)
                for x in range(i+1):
                    tableau_base.pop(0)
                break
        # for i in range(len(tableau_base)):
        #     print(tableau_base[i])
    tableau_base = supp_void_lines_from_table(tableau_base)
    return tableau_base
    
def RecupAuteurs(fichier):
    f = open(fichier, "r")
    lines = f.readlines()[nb_title_line:nb_abstract_line-1]
    tableau_base = [""] * len(lines)
    i = 0
    # stocker toutes les lignes dans un tableau
    for line in lines:
        tableau_base[i] = line
        # print(tableau_base[i])
        i+=1
    
    
    # Pour torres.txt
    # Si le tableau fait plus de 25 lignes
    if (len(tableau_base) > 20):
        # print("plus de 20")
        # On check si les 10 dernières lignes sont vides
        for i in reversed(range(len(tableau_base)-10, len(tableau_base))):
            # Si c'est le cas, on les supprime
            if (tableau_base[i] == "\n"):
                # print("aha")
                tableau_base.pop(i)
        # tableau_base.pop(len(tableau_base)-1)
        for i in reversed(tableau_base):
            if (i != "\n"):
                tableau_base.pop(tableau_base.index(i))
            else:
                break
    
    # Suppresion des sauts de ligne
    for i in tableau_base:
        if (i=="\n"):
            tableau_base.pop(tableau_base.index(i))
    return tableau_base


def RecupReferences(fichier):
    keywordReferences = ["References", "REFERENCES"]
    nb_reference_line = 0
    
    # Récupération du nombre de ligne du fichier
    file = open(fichier, "r")
    nb_lines = 0
    for line in (open(fichier).readlines()):
        nb_lines += 1

    # On récupère la ligne où apparait le premier référence à partir du bas
    length = 0              # Nombre de lignes où les REFERENCES apparaissent
    for line in reversed(open(fichier).readlines()):
        if any(x in line for x in keywordReferences):
            # print("REFERENCES found ! Line : ")
            # print(nb_lines - length)
            break
        length += 1
    file.close()
    
    nb_reference_line = nb_lines - length
    with open(fichier, "r") as f:
        lines = f.readlines()[nb_reference_line-1:]
        i = 0
        tableau_base = [""] * len(lines)
        # stocker toutes les lignes dans un tableau
        for line in lines:
            tableau_base[i] = line
            i+=1
    file.close()
    
    return tableau_base
    
    # for line in reversed(open(fichier).readlines()):
    #     print (line.rstrip())
    
    # En lisant le fichier à partir de la fin
    # Tant qu'on a pas le mot "References"
    # On ajoute au tableau


# def ConvertToTxt():
path = "Pdftotext/"
TableOfNamesOfTxtFilesWithDotTxt = RecupNamesOfTheTxtFiles(path)
TableOfNamesOfTxtFilesWithTxtAndSpacesDeleted = SuppSpacesFromStringTables(TableOfNamesOfTxtFilesWithDotTxt)
TableOfNamesOfTxtFilesWithoutDotTxt = DeleteDotTxtFromAStringTable(TableOfNamesOfTxtFilesWithDotTxt)

folderName = "Apres_Analyse"
CreateAfterDeleteDirectory(folderName)

i = 0
for x in TableOfNamesOfTxtFilesWithTxtAndSpacesDeleted:
    # PathFile = fichier d'où l'on va récupérer les informations
    pathFile = path + x
    # Créer le fichier "x"
    CreateFileInAFolder(TableOfNamesOfTxtFilesWithoutDotTxt[i], folderName)
    # Ecrire dans le fichier "x"
    with open(folderName+"/"+ x, "a") as f:
        # Ecrire le nom de fichier sans espace
        f.write(TableOfNamesOfTxtFilesWithTxtAndSpacesDeleted[i]+"\n")
        f.write("\n")
        f.write("______________________________")
        f.write("\n")

        # Ecrire le nom du titre
        f.write(RecupTitle(pathFile)+"\n")
        f.write("\n")
        f.write("______________________________")
        f.write("\n")

        # Ecrire l'abstract
        tableOfStrings = RecupAbstract(pathFile)
        for v in range(len(tableOfStrings)):
            f.write(tableOfStrings[v]+"\n")
        f.write("\n")
        f.write("______________________________")
        f.write("\n")
        
        AuteursTableStrings = RecupAuteurs(pathFile)
        for v in range(len(AuteursTableStrings)):
            f.write(AuteursTableStrings[v])
        f.write("\n")
        f.write("______________________________")
        f.write("\n")

        ReferencesTableStrings = RecupReferences(pathFile)
        for v in range(len(ReferencesTableStrings)):
            f.write(ReferencesTableStrings[v])
        f.write("\n")
        f.write("______________________________")
        f.write("\n")
        
        #test pour le xml 
    i += 1

# def ConvertToXml():
#     Tab = RecupNamesOfTheTxtFiles("Apres_Analyse")
#     for file in Tab :
#         print("Apres_Analyse/"+file)
#         sortie = open_file("Apres_Analyse/"+file)
#         sortie = split_file(sortie)
#         generate_xml(sortie)


# RecupReferences("test.txt")


# if len(sys.argv) == 2:
#     if(sys.argv[1] == "-t"):
#         ConvertToTxt()
#     elif(sys.argv[1] == "-x"):
#         ConvertToTxt()
#         ConvertToXml()
#     else :
#         print("Mauvais argument entré !")
# else :
#     print("Entrez le type de sortie ! (-x) ou (-t)")


# Test pour récupérer les titres

# Tab = RecupNamesOfThePdfFiles(sous_dossier)
# for i in range(0,10):
#     RecupTitle(sous_dossier+"/"+Tab[i])

# Juste pour retenir les fonctions
# for x in tableau_des_PDF:
#     f = open('')
#     f.write()
#     f.close()


# Utilisation : python3 fichier.py dossier_contenant_les_fichiers txt

# Sous dossier contenant les fichier TXT à analyser
# sous_dossier = sys.argv[1]

# for i in TableOfNamesOfTxtFilesWithDotTxt :
#     print("--------------------------------------------------------")
#     print(i)
#     print("--------------------------------------------------------")
#     RecupAbstract(path+i)
#     RecupTitle(path+i)

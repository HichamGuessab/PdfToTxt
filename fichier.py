import os
import sys
import shutil
import re
import subprocess

# Utilisation : python3 fichier.py dossier_contenant_les_fichiers txt

# Dossier contenant les pdf à analyser (et les txts) = sys.argv[1]
# Type de sortie = sys.argv[2]
# utiliser ou non le parseur = sys.argv[3]

# Recuperer le nom des fichiers du dossier contenant les fichiers en .pdf
def recupNamesOfThePdfFiles(path):
    tableau_des_pdf = os.listdir(path)
    maxi = len(tableau_des_pdf)
    i=0
    while i < maxi :
        if re.search("\.pdf$", tableau_des_pdf[i]) == None:
            tableau_des_pdf.remove(tableau_des_pdf[i])
            i-=1
            maxi-=1
        i+=1
    return tableau_des_pdf

# Recuperer le nom des fichiers du dossier contenant les fichiers en .txt
def recupNamesOfTheTxtFiles(path):
    tableau_des_txt = os.listdir(path)
    maxi = len(tableau_des_txt)
    i=0
    while i < maxi :
        if re.search("\.txt$", tableau_des_txt[i]) == None:
            tableau_des_txt.remove(tableau_des_txt[i])
            i-=1
            maxi-=1
        i+=1
    # print(tableau_des_txt)
    return tableau_des_txt

def deleteDotTxtFromAStringTable(table):
    tableau_des_TXT_sans_le_txt = [""] * len(table)                     # Tableau contenant les nom des fichiers du sous_dossier SANS le ".txt" 
    for i in range(len(table)) :
        tableau_des_TXT_sans_le_txt[i] = table[i][:-4]
    return tableau_des_TXT_sans_le_txt

# Supprimer le dossier Apres_Analyse s'il existe, le creer après verification
def createAfterDeleteDirectory(folderName: str):
    if os.path.exists(folderName):
        shutil.rmtree(folderName)
        print(folderName+" directory deleted")
    # Creation du dossier folderName
    os.mkdir(folderName)
    print(folderName+" directory created")

# Supprime le dossier s'il existe
def deleteDirectory(folderName: str):
    if os.path.exists(folderName):
        shutil.rmtree(folderName)

# Supprimer les espaces des String d'un tableau de String
def suppSpacesFromStringTables(stringTable):
    # print("Suppression des espaces des String d'un tableau de String")
    for i in range(len(stringTable)):
        stringTable[i] = suppSpacesFromString(stringTable[i])
    return stringTable

# Supprimer les espaces d'un String
def suppSpacesFromString(name: str):
    # print("Suppression des espaces d'un String")
    x = name.replace(" ", "_")
    return x

def supp_start_spaces_from_lines_(table):
    # Suppression des espaces au debut de toutes les lignes    
    # print("Tableau sans espaces au debut")
    for i in range(len(table)):
        table[i] = table[i].lstrip() 
    return table

def supp_void_lines_from_table(table):
    # Trouver l'index 
    num_line_tab = 0                        # le numero de la ligne (dans le tableau)
    i = 0
    for i in range(len(table)):
        num_line_tab+=1
        index = table[i].find("                                   ")
        # print("Ligne : ", num_line_tab)
        # print("Espaces trouvees index :", index)
        table[i] = table[i][:index]
    return table

# Creer tous les fichiers d'un tableau ayant le même nom sans les espaces
def createFileInAFolder(fileName: str, folderName: str):
    print("Creation du fichier "+fileName + " dans le directory " + folderName)
    # for i in range(len(tableauDesTxtSansLeTxt)):
    nom = fileName+".txt"
    f = open(folderName+"/"+nom, "x")         # Creation du fichier dans le dossier "Apres_Analyse"
    f.close()

# Fonction qui ne sert plus à rien : On la garde au cas où
def supp_lines_from_table_after_5_spaces(table):
    # Suppression de la fin des lignes à partir de là où il y a 5 espaces
    # Trouver l'index 
    num_line_tab = 0                        # le numero de la ligne (dans le tableau)
    i = 0
    for i in range(len(table)):
        num_line_tab+=1
        index = table[i].find("         ")
        # print("Ligne : ", num_line_tab)
        # print("Espaces trouvees index :", index)
        table[i] = table[i][:index]
    return table

# Recuperer le titre d'un fichier (!= nom d'un fichier)
def RecupTitle(fichier):
    connectors = ["with", "without", "of", "for", "An ", "OF"] # Mots de liaisons
    skipCharacters = ["From", "Journal", "Submitted"] # Mot qui ne font pas parti du titre
    file1 = open(fichier, 'r', encoding="ascii", errors='ignore')
    titre = ""
    global nb_title_line
    nb_title_line = 0

    ligne = file1.readline()
    ligne_v = ligne
    nb_title_line += 1
    liste = list(ligne.split(" ")) # Recuperer la ligne sous forme de liste pour comparer les mots
    taille = len(liste)
            
    # Tant que je trouve un mot pas bon je passe à la prochaine ligne
    # Si la prochaine est un saut de ligne, je passe à la prochaine ligne
    diffWord = False
    while(diffWord == False):
        if any(x in liste[0] for x in skipCharacters) or re.search(r'\d', ligne) or len(ligne.split()) == 1: # Si on rencontre un caractère qui ne fait pas parti du titre
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
        if any(x in ligne[0] for x in connectors): # Si on rencontre un connecteur dans la deuxième ligne
            titre+=ligne # On ajoute la ligne suivante au titre (suite du titre)
            nb_title_line += 1
    file1.close()
    
    finalTitre = ""
    for t in titre.split(): # On ajoute les elements du tableau contenant tout les mots du titre dans notre titre final
        finalTitre+=t
        finalTitre+=" "
    # print(finalTitre)
    return finalTitre

# Recuperer l'abstract d'un fichier
def RecupAbstract(fichier):
    keyword = ["Introduction", "INTRODUCTION","I NTRODUCTION", "introduction", "INDEX", "Index", "index", "Corresponding author"]
    # print("Recuperation des resumes de l'auteur")
    word1 = "Abstract"
    word2 = "ABSTRACT"
    word3 = "abstract"
    global nb_abstract_line 
    nb_abstract_line = 0
    
    # Chercher la ligne où se situe le mot "Abstract"
    abstractFound = False
    j = 0
    file = open(fichier, "r", encoding="ascii", errors='ignore')
    for line in file:
        nb_abstract_line += 1
        if word1 in line or word2 in line or word3 in line:
            # print("ABSTRACT found ! Line : ")
            # print(nb_abstract_line)
            abstractFound = True
            break
    file.close()
    
    # Chercher la ligne où se situe le KeyWord
    global nb_keyword_line
    nb_keyword_line = 0
    
    file = open(fichier, "r", encoding="ascii", errors='ignore')
    keywordFound = False

    for line in file:
        if keywordFound == True:
            break
        nb_keyword_line += 1
        for i in range(len(keyword)):
            if keywordFound == True:
                break
            if (keyword[i] in line) and (nb_keyword_line > nb_abstract_line):
                # print("KEYWORD keywordFound ! Line : ")
                # print(nb_keyword_line)
                keywordFound = True

# nb_abstract_line est maintenant la ligne où le asbtract se situe
# nb_keyword_line est maintenant la ligne où le keyword se situe
    # On doit traiter le cas où le mot "Abstract" n'est pas present
    if(abstractFound == True):
        with open(fichier, "r", encoding="ascii", errors='ignore') as f:
            lines = f.readlines()[nb_abstract_line-1:nb_keyword_line-1]
            tableau_base = [""] * len(lines)
            i = 0
            # stocker toutes les lignes dans un tableau
            for line in lines:
                tableau_base[i] = line
                i+=1
    else:
        with open(fichier, "r", encoding="ascii", errors='ignore') as f:
            # On a notre ligne Introduction (nb_keyword_line) mais pas notre mot cle "Abstract"
            # Faut maintenant stocker dans une liste en remontant le keyword 
            lines = f.readlines()[nb_keyword_line-2:nb_keyword_line-1]
            tableau_base = [""] * len(lines)
            i = 0
            # stocker toutes les lignes dans un tableau
            for line in lines:
                tableau_base[i] = line
                i+=1
    file.close()
    # Traitement du cas où le mot cle "abstract" n'a pas ete trouve
    # pdftotxtV4
    if(abstractFound == False):
        nb_abstract_line = nb_keyword_line -1
    #     # print("Abstract non trouve")
    #     # print(nb_keyword_line)
    #     j = 0
    #     for i in range(len(tableau_base)):
    #         if(tableau_base[i]=="\n"):
    #         #     j+=1
    #         #     if (tableau_base[i+1]=="\n"):
    #         #         j+=1
    #         #     else:
    #         #         j=0
    #         # if(j == 2):
    #             nb_abstract_line = i+1
    #             # print("oula", i)
    #             for x in range(i+1):
    #                 tableau_base.pop(0)
    #             break
        # for i in range(len(tableau_base)):
        #     print(tableau_base[i])
        
    # supprimer les lignes qui possède un ": " sur les 10 premiers caractères
    tableau_base = supp_void_lines_from_table(tableau_base)
    keyword = [": "]
    endroit = 200
    for x in tableau_base:
        if(": " in x):
            if(x.index(": ") < 10):
                endroit = tableau_base.index(x)
                break
    
    tableau_base = tableau_base[:endroit]
    
    #supprimer la ligne du tableau qui commence par un nombre
    for x in tableau_base:
        if(x != ""):
            for i in range(5):
                # print(x[i])
                if(x[i].isdigit() and x[i+1].isdigit() and x[i+2].isdigit() and x[i+3]):
                    tableau_base.remove(x)
                    break
    return tableau_base
    
def RecupAuteurs(fichier):
    f = open(fichier, "r", encoding="ascii", errors='ignore')
    lines = f.readlines()[nb_title_line:nb_abstract_line-1]
    tableau_base = [""] * len(lines)
    i = 0
    # stocker toutes les lignes dans un tableau
    for line in lines:
        tableau_base[i] = line
        # print(tableau_base[i])
        i+=1
    
    # pdftotxtV4
    # Pour torres.txt
    # Si le tableau fait plus de 25 lignes
    # if (len(tableau_base) > 25):
    #     # print("plus de 20")
    #     # On check si les 10 dernières lignes sont vides
    #     for i in reversed(range(len(tableau_base)-10, len(tableau_base))):
    #         # Si c'est le cas, on les supprime
    #         if (tableau_base[i] == "\n"):
    #             # print("aha")
    #             tableau_base.pop(i)
    #     # tableau_base.pop(len(tableau_base)-1)
    #     for i in reversed(tableau_base):
    #         if (i != "\n"):
    #             tableau_base.pop(tableau_base.index(i))
    #         else:
    #             break
    
    # Suppresion des sauts de ligne
    for i in tableau_base:
        if (i=="\n"):
            tableau_base.pop(tableau_base.index(i))
    return tableau_base

def recupIntroduction(fichier):
    keywordsIntro = ["Introduction", "INTRODUCTION", "I NTRODUCTION", "introduction"]
    keyWordsFinIntro = ["2.", "2", "2", "II.", "II"]
    file = open(fichier, 'r', encoding="ascii", errors='ignore')
    lines = file.readlines()
    intro = list()
    debutIntro = False
    for line in lines :
        if not debutIntro:
            if any(x in line for x in keywordsIntro): #Début de l'intro
                debutIntro = True
        else :
            words = list(line.split(" "))
            if words[0] in keyWordsFinIntro and len(line) < 75 : # Fin de l'intro
                file.close()
                return intro
            else:
                intro.append(line)

    file.close()
    if intro:
        return intro
    else:
        return ("Introduction non trouvée")
        
def recupCorps(fichier):
        keywordIntro = ["Introduction", "INTRODUCTION", "I NTRODUCTION", "introduction"]
        keywordFinCorps = ["Discussion", "DISCUSSION", "discussions", "Discussions", "DISCUSSIONS", "Conclusion", "CONCLUSION", "conclusion", "References", "Reference", "REFERENCES", "REFERENCE"]
        keywordDebutCorps = ["2.", "2", "2", "II.", "II"]
        file1 = open(fichier, 'r', encoding="utf-8", errors='ignore')
        lines = file1.readlines()
        corps = list()
        debutCorps=False
        debutIntro=False
        for line in lines :
            if not debutCorps :
                if not debutIntro :
                    if any(x in line for x in keywordIntro) :
                        debutIntro=True
                else :
                    words = list(line.split(" "))
                    if words[0] in keywordDebutCorps and len(line) < 75 :
                        debutCorps=True
            else :
                if any(x in line for x in keywordFinCorps) and len(line) < 40 :
                    file1.close();
                    return corps
                else :
                    corps.append(line)
        file1.close();
        return corps

def recupConclusion(fichier) :
    keywordConclusion = ["Conclusions", "Conclusion", "CONCLUSION", "CONCLUSIONS"]
    keywordFinConclu = ["Acknowledgements", "Acknowledgments", "Acknowledgement", "Acknowledgment", "References", "Reference", "ACKNOWLEDGMENT", "ACKNOWLEDGMENTS", "REFERENCES", "REFERENCE", "Appendix", "APPENDIX"]
    file = open(fichier, 'r', encoding="utf-8", errors='ignore')
    lines = file.readlines()
    conclusion = list()
    debutConclusion=False
    for line in lines :
        if not debutConclusion :
            if (len(line) < 50) and any(x in line for x in keywordConclusion) :
                debutConclusion=True
        else :
            if (len(line) < 50) and any(x in line for x in keywordFinConclu) :
                return conclusion
            else :
                conclusion.append(line)
    return conclusion

def recupDiscussion(fichier) :
    keywordDiscussion = ["Discussions", "Discussion", "DISCUSSION", "DISCUSSIONS"]
    keywordFinDiscu = ["Acknowledgements", "Acknowledgments", "Acknowledgement", "Acknowledgment", "References", "Reference", "ACKNOWLEDGMENT", "ACKNOWLEDGMENTS", "REFERENCES", "REFERENCE", "Conclusions", "Conclusion", "CONCLUSION", "CONCLUSIONS", "Appendix", "APPENDIX"]
    file = open(fichier, 'r', encoding="utf-8", errors='ignore')
    lines = file.readlines()
    discussion = list()
    debutDiscu=False
    for line in lines :
        if not debutDiscu :
            if (len(line) < 50) and any(x in line for x in keywordDiscussion) :
                debutDiscu=True
        else :
            if (len(line) < 50) and any(x in line for x in keywordFinDiscu) :
                return discussion
            else :
                # print(line)
                discussion.append(line)
    return discussion

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
    # print(references)
    return references

def convertToXml(v):
    tableOfNamesOfTxtFilesWithDotTxt = recupNamesOfTheTxtFiles(path)

    tableOfNamesOfTxtFilesWithTxtAndSpacesDeleted = suppSpacesFromStringTables(tableOfNamesOfTxtFilesWithDotTxt)
    tableOfNamesOfTxtFilesWithoutDotTxt = deleteDotTxtFromAStringTable(tableOfNamesOfTxtFilesWithDotTxt)
    folderName = path+"Apres_Analyse"
    createAfterDeleteDirectory(folderName)
    print("\n")

    # print(tableOfNamesOfTxtFilesWithoutDotTxt)
    # print(recupNamesOfTheTxtFiles(path))
    i = 0
    # print(v)
    for x in v:
        # PathFile = fichier d'où l'on va recuperer les informations
        pathFile = path + x
        # Creer le fichier "x"
        createFileInAFolder(tableOfNamesOfTxtFilesWithoutDotTxt[i], folderName)
        print("\n")

        # Ecrire dans le fichier "x"
        with open(folderName+"/"+ tableOfNamesOfTxtFilesWithoutDotTxt[i] + ".xml", "a", encoding="ascii", errors='ignore') as f:
            f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
            f.write("<article>\n")
            # Ecrire le nom de fichier sans espace
            f.write("\n<preamble>\n")
            f.write(tableOfNamesOfTxtFilesWithTxtAndSpacesDeleted[i]+"\n")
            f.write("</preamble>\n")
            f.write("\n")
            f.write("______________________________")
            f.write("\n")

            # Ecrire le nom du titre
            f.write("\n<titre>")
            titleTableOfStrings = RecupTitle(pathFile)

            if(not titleTableOfStrings):
                f.write("Title non trouve.")
            else:

                f.write(titleTableOfStrings)
            f.write("\n")
            f.write("</titre>\n")
            f.write("______________________________")
            f.write("\n")

            # Ecrire l'abstract
            abstractTableOfStrings = RecupAbstract(pathFile)
            f.write("\n<abstract>")
            if(not abstractTableOfStrings):
                f.write("Abstract non trouve.")
            else:
                for v in range(len(abstractTableOfStrings)):
                    f.write(abstractTableOfStrings[v]+"\n")
            f.write("\n")
            f.write("</abstract>\n")
            f.write("______________________________")
            f.write("\n")
            
            f.write("\n<auteur>")
            auteursTableStrings = RecupAuteurs(pathFile)
            if(not auteursTableStrings):
                    f.write("Auteurs non trouvee.")
            else:
                for v in range(len(auteursTableStrings)):
                    f.write(auteursTableStrings[v])
            f.write("\n")
            f.write("</auteur>\n")
            f.write("______________________________")
            f.write("\n")

            f.write("\n<introduction>")
            introductionTableStrings = recupIntroduction(pathFile)
            if(not introductionTableStrings):
                f.write("Introduction non trouvee.")
            else:
                for v in range(len(introductionTableStrings)):
                    f.write(introductionTableStrings[v])
            f.write("\n")
            f.write("</introduction>\n")
            f.write("______________________________")
            f.write("\n")
            
            f.write("\n<corps>")
            corpsTableStrings = recupCorps(pathFile)
            if(not corpsTableStrings):
                f.write("Corps non trouve.")
            else:
                for v in range(len(corpsTableStrings)):
                    f.write(corpsTableStrings[v])
            f.write("\n")
            f.write("</corps>\n")
            f.write("______________________________")
            f.write("\n")
            
            f.write("\n<conclusion>")
            conclusionTableStrings = recupConclusion(pathFile)
            if(not conclusionTableStrings):
                f.write("Conclusion non trouvee.")
            else:
                for v in range(len(conclusionTableStrings)):
                    f.write(conclusionTableStrings[v])
            f.write("\n")
            f.write("</conclusion>\n")
            f.write("______________________________")
            f.write("\n")
            
            f.write("\n<discussion>")
            discussionTableStrings = recupDiscussion(pathFile)
            if(not discussionTableStrings):
                f.write("Discussion non trouvee.")
            else:
                for v in range(len(discussionTableStrings)):
                    f.write(discussionTableStrings[v])
            f.write("\n")
            f.write("</discussion>\n")
            f.write("______________________________")
            f.write("\n")
            
            f.write("\n<biblio>")
            referencesTableStrings = recupReferences(pathFile)
            if(not referencesTableStrings):
                f.write("References non trouvees.")
            else:            
                for v in range(len(referencesTableStrings)):
                    f.write(referencesTableStrings[v])
            f.write("\n")
            f.write("\n</biblio>\n")
            f.write("\n</article>")
            f.close()
            # Supprime la sortie de pdftotext
            # if utiliserParseur:
            #     os.remove(pathFile)
        i += 1

def convertToTxt(v):
    tableOfNamesOfTxtFilesWithDotTxt = recupNamesOfTheTxtFiles(path)

    tableOfNamesOfTxtFilesWithTxtAndSpacesDeleted = suppSpacesFromStringTables(tableOfNamesOfTxtFilesWithDotTxt)
    tableOfNamesOfTxtFilesWithoutDotTxt = deleteDotTxtFromAStringTable(tableOfNamesOfTxtFilesWithDotTxt)
    folderName = path+"Apres_Analyse"
    createAfterDeleteDirectory(folderName)
    print("\n")

    # print(tableOfNamesOfTxtFilesWithoutDotTxt)
    # print(recupNamesOfTheTxtFiles(path))
    i = 0
    # print(v)
    for x in v:
        # PathFile = fichier d'où l'on va recuperer les informations
        pathFile = path + x
        # Creer le fichier "x"
        createFileInAFolder(tableOfNamesOfTxtFilesWithoutDotTxt[i], folderName)
        print("\n")

        # Ecrire dans le fichier "x"
        with open(folderName+"/"+ tableOfNamesOfTxtFilesWithoutDotTxt[i] + ".txt", "a", encoding="ascii", errors='ignore') as f:
            # Ecrire le nom de fichier sans espace
            f.write(tableOfNamesOfTxtFilesWithTxtAndSpacesDeleted[i]+"\n")
            f.write("\n")
            f.write("______________________________")
            f.write("\n")

            # Ecrire le nom du titre
            titleTableOfStrings = RecupTitle(pathFile)
            if(not titleTableOfStrings):
                f.write("Title non trouve.")
            else:
                f.write(titleTableOfStrings)
            f.write("\n")
            f.write("______________________________")
            f.write("\n")

            # Ecrire l'abstract
            abstractTableOfStrings = RecupAbstract(pathFile)
            if(not abstractTableOfStrings):
                f.write("Abstract non trouve.")
            else:
                for v in range(len(abstractTableOfStrings)):
                    f.write(abstractTableOfStrings[v]+"\n")
            f.write("\n")
            f.write("______________________________")
            f.write("\n")
            
            auteursTableStrings = RecupAuteurs(pathFile)
            if(not auteursTableStrings):
                    f.write("Auteurs non trouvee.")
            else:
                for v in range(len(auteursTableStrings)):
                    f.write(auteursTableStrings[v])
            f.write("\n")
            f.write("______________________________")
            f.write("\n")
            
            introductionTableStrings = recupIntroduction(pathFile)
            if(not introductionTableStrings):
                f.write("Introduction non trouvee.")
            else:
                for v in range(len(introductionTableStrings)):
                    f.write(introductionTableStrings[v])
            f.write("\n")
            f.write("______________________________")
            f.write("\n")
            
            corpsTableStrings = recupCorps(pathFile)
            if(not corpsTableStrings):
                f.write("Corps non trouve.")
            else:
                for v in range(len(corpsTableStrings)):
                    f.write(corpsTableStrings[v])
            f.write("\n")
            f.write("______________________________")
            f.write("\n")
            
            conclusionTableStrings = recupConclusion(pathFile)
            if(not conclusionTableStrings):
                f.write("Conclusion non trouvee.")
            else:
                for v in range(len(conclusionTableStrings)):
                    f.write(conclusionTableStrings[v])
            f.write("\n")
            f.write("______________________________")
            f.write("\n")
            
            discussionTableStrings = recupDiscussion(pathFile)
            if(not discussionTableStrings):
                f.write("Discussion non trouvee.")
            else:
                for v in range(len(discussionTableStrings)):
                    f.write(discussionTableStrings[v])
            f.write("\n")
            f.write("______________________________")
            f.write("\n")
            
            referencesTableStrings = recupReferences(pathFile)
            if(not referencesTableStrings):
                f.write("References non trouvees.")
            else:            
                for v in range(len(referencesTableStrings)):
                    f.write(referencesTableStrings[v])
            f.write("\n")

            # Supprime la sortie de pdftotext
            # if utiliserParseur:
            #     os.remove(pathFile)
        i += 1

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Nombre d'arguments incorrect.")
    exit()
path = sys.argv[1]
#Si path n'a pas de '/' à la fin, on le rajoute
if re.search("/$", path) != "/":
    path = path+"/"
typeSortie = sys.argv[2]
if(typeSortie != "-t") and (typeSortie != "-x"):
    print("Le second argument \""+typeSortie+"\" devrait etre \"-t\" ou \"-x\".")
    exit()

utiliserParseur = True

if len(sys.argv) == 4:
    if(sys.argv[3] == "-n"):
        utiliserParseur = False

# Debut du parseur
if utiliserParseur :
    filesPdf = recupNamesOfThePdfFiles(path)
    for file in filesPdf:
        os.system("pdftotext "+path+file.replace(" ","\\ "))
files = recupNamesOfTheTxtFiles(path)
#Fin du parseur

i = 0
for file in files:
    print(i, " ", file)
    i+=1
print("-1  Quitter")
choix = input("Entrez les numéros des fichier à analyser : ")
choix = choix.split(',')
fullNumber = True
outOfRangeIndex = False
choixFiles = list()
for nombre in choix:
    if nombre.isnumeric() and int(nombre) >=0 and int(nombre) < len(files):
        choixFiles.append(files[int(nombre)])
if(typeSortie == "-t"):
    convertToTxt(choixFiles)
elif(typeSortie == "-x"):
    convertToXml(choixFiles)
else:
    printf("Second argument incorrect")







# for nombre in choix:
#     if(not nombre.isnumeric()):
#         fullNumber = False
#         break
#     if(int(nombre) < 0 or int(nombre) >= i):
#         outOfRangeIndex = True
#         break
# if(choix):
#     if(choix[0] == "-1"):
#         print("Fin du programme")
#         exit()
#     else:
#         var = 0
#         choixTab = []
#         for file in choix:
#             if(fullNumber and not outOfRangeIndex):
#                 choixTab.append(files[int(file)])
#             else:
#                 if(not fullNumber):
#                     print("Entrez une suite de nombres !")
#                 if(outOfRangeIndex):
#                     print("Entrez des nombres correspondants à ceux affichés !")

#         if(typeSortie == "-t"):
#             convertToTxt(choixTab)
#         elif(typeSortie == "-x"):
#             convertToXml(choixTab)
#         else :
#             print("Entrez l'option -t ou -x !")
#             exit()

# createAfterDeleteDirectory("txt2XML")






# Fin du parseur. Il suffit de mettre les txts de Nico dans le dossier path avant de lancer le programme avec un troisième argument "-n" pour ne pas l'utiliser

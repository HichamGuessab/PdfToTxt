import os
import sys

# Utilisation : python3 fichier.py dossier_contenant_les_fichiers txt



# Sous dossier contenant les fichier TXT à analyser
#sous_dossier = sys.argv[1]


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
    print("Récupération des résumés de l'auteur")
    
def RecupTitlesInATable(path):
    print("Récupération des titres des fichiers txt du dossier "+path+" insérés dans un tableau")
    tableauDesFichiers = os.listdir(path)
    #for i in range(len(tableauDesFichiers)) :
        
def recupCorps(fichier):
        keywordIntro = ["Introduction", "INTRODUCTION", "I NTRODUCTION", "introduction"]
        keywordFinCorps = ["Discussion", "DISCUSSION", "discussions", "Discussions", "DISCUSSIONS", "Conclusion", "CONCLUSION", "conclusion"]
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
                    if words[0] in keywordDebutCorps :
                        debutCorps=True
            else :
                if any(x in line for x in keywordFinCorps) and len(line) < 40 :
                    return corps
                else :
                    corps.append(line)

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
                print(line)
                discussion.append(line)

recupDiscussion("CORPUS_TRAIN/Torres.txt")


# On parcourt chaque fichier du dossier "Pdftotext"
# i = 0                               # Pour parcourir le tableau tableau_des_TXT_sans_le_txt en même temps que le tableau tableau_des_TXT
# for x in tableau_des_TXT:
    
#     f = open(x)
    
#     f.write()


# for (x in tableau_des_PDF):
    # f = open('')
    # f.write()
    # f.close()



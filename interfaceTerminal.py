import sys
from fichier import *

folderName = "Apres_Analyse"
createAfterDeleteDirectory(folderName)
createAfterDeleteDirectory("txt2XML")
files = recupNamesOfTheTxtFiles('Pdftotext')

def convertToTxt(fichier):
    path = "Pdftotext/"
    TableOfNamesOfTxtFilesWithDotTxt = recupNamesOfTheTxtFiles(path)
    TableOfNamesOfTxtFilesWithTxtAndSpacesDeleted = suppSpacesFromStringTables(TableOfNamesOfTxtFilesWithDotTxt)
    TableOfNamesOfTxtFilesWithoutDotTxt = deleteDotTxtFromAStringTable(TableOfNamesOfTxtFilesWithDotTxt)

    folderName = "Apres_Analyse"

    i = 0
    # PathFile = fichier d'où l'on va récupérer les informations
    path = "Pdftotext/"
    pathFile = path + fichier
    # Créer le fichier "x"

    # Ecrire dans le fichier "x"
    with open(folderName+"/"+ fichier, "a", encoding="ascii", errors='ignore') as f:
        
        # Ecrire le nom de fichier sans espace
        f.write(fichier[:-4]+"\n")
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

        # Ecrire le nom des auteurs 
        AuteursTableStrings = RecupAuteurs(pathFile)
        for v in range(len(AuteursTableStrings)):
            f.write(AuteursTableStrings[v])
        f.write("\n")
        f.write("______________________________")
        f.write("\n")
        
        IntroductionTableStrings = recupIntroduction(pathFile)
        for v in range(len(IntroductionTableStrings)):
            f.write(IntroductionTableStrings[v])
        f.write("\n")
        f.write("______________________________")
        f.write("\n")
        
        CorpsTableStrings = recupCorps(pathFile)
        for v in range(len(CorpsTableStrings)):
            f.write(CorpsTableStrings[v])
        f.write("\n")
        f.write("______________________________")
        f.write("\n")
        
        ConclusionTableStrings = recupConclusion(pathFile)
        for v in range(len(ConclusionTableStrings)):
            f.write(ConclusionTableStrings[v])
        f.write("\n")
        f.write("______________________________")
        f.write("\n")
        
        DiscussionTableStrings = recupDiscussion(pathFile)
        for v in range(len(DiscussionTableStrings)):
            f.write(DiscussionTableStrings[v])
        f.write("\n")
        f.write("______________________________")
        f.write("\n")
        
        ReferencesTableStrings = recupReferences(pathFile)
        for v in range(len(ReferencesTableStrings)):
            f.write(ReferencesTableStrings[v])
        f.write("\n")

def ConvertToXml(file):
    sortie = open_file("Apres_Analyse/"+file)
    sortie = split_file(sortie)
    generate_xml(sortie)

while True :

    i = 0
    for file in files:
        print(i, " ", file)
        i+=1
    print(i, "Quitter")
    choix = input("Entrez les numéros des fichier à analyser : ")
    choix = choix.strip()
    if(choix):
        if(choix == str(i)):
            print("Fin du programme")
            break
        else:
            choix = list(choix.strip(" "))
            print(choix)
            for i in choix:
                print(files[int(i)])
            format = input("Entrez -x pour convertir en xml ou -t pour convertir en txt : ")
            format = format.strip()
            createAfterDeleteDirectory(folderName)
            createAfterDeleteDirectory("txt2XML")
            if(format == str("-x")):    
                for i in choix :
                    convertToTxt(files[int(i)])
                    ConvertToXml(files[int(i)])
            else :
                for i in choix:
                    convertToTxt(files[int(i)])

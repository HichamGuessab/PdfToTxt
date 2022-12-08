import sys
from tkinter import *
from tkinter import messagebox
from fichier import *

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
        f.write(fichier+"\n")
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

folderName = "Apres_Analyse"
createAfterDeleteDirectory(folderName)


checkbox = []
#RecupNameOfPDFFiles
files = recupNamesOfTheTxtFiles('Pdftotext')

window = Tk()

window.title("Parser d'article scientifique")
window.geometry("1920x900")
window.config(background='#486400')

window.iconbitmap("cacatoesque.ico")
bgimg=PhotoImage(file = "ico.png")


limg= Label(window, i=bgimg, font=("Helvetica", 25) ).pack()
label = Label(window, text="Selectionnez les fichiers à parser", font=("Helvetica", 25), background='#486400', fg="White").pack()

groupe = StringVar()
radioXML = Radiobutton(window, text="XML", variable=groupe, value="-x")
radioTXT = Radiobutton(window, text="TXT", variable=groupe, value="-t")

radioXML.pack()
radioTXT.pack()
radioXML.invoke()


#window.attributes('-fullscreen', True)


def affichage():
    for i in range(len(checkbox)):
        choix=""
        if checkbox[i].get()>=1:
            choix += str(i)
            if(groupe.get() == '-t'):
                convertToTxt(files[i])
                messagebox.showinfo(message="Le fichier " + files[i] + " a bien été traité au format txt")

            else :
                convertToTxt(files[i])
                ConvertToXml(files[i])
                messagebox.showinfo(message="Le fichier " + files[i] + " a bien été traité au format xml")

for i in range(len(files)):
    option = IntVar()
    option.set(0)
    checkbox.append(option)


i = 0
for file in files:
    Checkbutton(window, text=file,variable=checkbox[i], font=("Helvetica", 15), background='#486400' ).pack(expand=YES)
    i+=1

Button(window, text="Parser", command=affichage, font=("Helvetica", 15)).pack(side=BOTTOM)

window.mainloop()

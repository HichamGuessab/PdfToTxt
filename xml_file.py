import os
import sys

# J'assigne le nom de mon fichier à un string
filename = "exemple.txt"

# Fonction qui ouvre un fichier txt et qui le lit et envoie la sortie
def open_file(file):
    with open (file,"r") as f:
        sortie = f.read()
    f.close()
    return (sortie)

# Fonction qui va split notre txt et mettre les données separé par les trais, dans un tableau
def split_file(sortie):
    sortie = sortie.split("______________________________")
    return (sortie)

# Fonction qui va generer un fichier xml adapté pour les informations précédemment extraite.
def generate_xml(sortie):
    path = "txt2XML/" + sortie[0].strip() + ".xml";
    print("Path : ", path)
    with open (path, "w") as f:
        f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        #Balise article
        f.write("<article>\n")
        #Balise preamble
        f.write("\n<preamble>\n")
        f.write(sortie[0])
        f.write("</preamble>\n")
        #Balise titre
        f.write("\n<titre>")
        f.write(sortie[1])
        f.write("</titre>\n")
        #Balise auteur
        f.write("\n<auteur>")
        f.write(sortie[3])
        f.write("</auteur>\n")
        #Balise abstract
        f.write("\n<abstract>")
        f.write(sortie[2])
        f.write("</abstract>\n")
        #Balise abstract
        f.write("\n<introduction>")
        f.write(sortie[4])
        f.write("</introduction>\n")
        #Balise abstract
        f.write("\n<corps>")
        f.write(sortie[5])
        f.write("</corps>\n")
        #Balise abstract
        f.write("\n<conclusion>")
        f.write(sortie[6])
        f.write("</conclusion>\n")
        #Balise abstract
        f.write("\n<discussion>")
        f.write(sortie[7])
        f.write("</discussion>\n")
        #Balise biblio
        f.write("\n<biblio>")
        f.write(sortie[8])
        f.write("\n</biblio>\n")

        f.write("\n</article>")

    f.close()
    print("Fichier xml créé !")




# Test :
#print("-------- Test 1 -------- ")
#sortie = open_file(filename)
#print(sortie)
#print("-------- Test 2 -------- ")
#sortie = split_file(sortie)
#print(sortie[0])
#print("-------- Test 3 -------- ")
#Création d'un fichier xml en prenant en argument le tableau sortie (split de notre fichier txt contenant les informations du pdf)
#generate_xml(sortie)
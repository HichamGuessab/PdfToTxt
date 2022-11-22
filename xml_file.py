import os
import sys

Xml_tab = {}
key = 0
file = open("exemple.txt")
for line in file:
    value = line.split()
    Xml_tab[key] = value
    key+=1

print(Xml_tab)

print(Xml_tab[0])

j=0
dico_nb = 0
str = ""
for i in Xml_tab[dico_nb]:
    if(i!=Xml_tab[0][0]):
        str += " " + Xml_tab[dico_nb][j]
    j+=1
  
print(str)
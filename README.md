# Parseur txt

Ce programme est destiné à récupéré les informations d'un **fichier au format txt** et à les enregistrer dans un **autre fichier au format txt**.
Il analysera ainsi tous les fichiers txt d'un **dossier** et créera des fichiers txt dans un autre **dossier**.

**Informations récupérées :**
 - Nom du fichier
 - Titre du document
 - Résumé du document

---

### Exécution 

    python3 recupData.py Directory

---
### Fonctionnement

Les fichiers txt de l'argument **Directory** sont récupérés et analysés par le parseur.
Après analyse, des fichiers sont créés et stockés dans le sous-dossier "**Apres_Analyse**".
Le nom des fichiers reste le même mais les **espaces** sont remplacés par des "**_**"
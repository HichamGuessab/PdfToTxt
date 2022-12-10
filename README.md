
# Parser d'article scientifique

Ce programme est destiné à récupérer les informations d'un article scientifique converti du format PDF au format txt et à extraire les informations essentielles vers une sortie au format txt.

Il analysera ainsi tous les articles au format txt d'un dossier et créera des fichiers txt dans un autre dossier.

Nous utilisons la version 4.00 de pdftotext. 
Nous utilisons d'ailleurs pdftotext sans options.
## Prérequis

Pour éxécuter ce projet, vous aurez besoin de l'outil pdftotext.

Pour l'installer, vous pouvez éxécuter la commande suivante dans un terminal Linux.

`sudo apt install poppler-utils`


## Fonctionnalités

- Conversion au format xml
- Conversion au format txt


## Commandes de lancement

#### Générer un fichier xml

```http
  python3 fichier.py -x <chemin>
```

| Parametre | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-x` | `string` | **Requis**. Indication pour la conversion en xml |
| `<chemin>` | `string` | **Requis**. Chemin absolu du dossier contenant les articles au format txt |


#### Générer un fichier txt

```http
  python3 fichier.py -t <chemin>
```

| Parametre | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-t` | `string` | **Requis**. Indication pour la conversion en txt |
| `<chemin>` | `string` | **Requis**. Chemin absolu du dossier contenant les articles au format txt |

#### python3 fichier.py -t /home/nas-wks01/users/uapv2104331/IdeaProjects/pdftotxt/PDF

Extrait toutes les informations des fichiers du dossier indiqué et redirige les sorties vers un dossier ApresAnalyse.


## Auteurs

- [@AbdelghaniRechidi](https://gitlab.com/uapv2002373)
- [@HichamGuessab](https://gitlab.com/HichamGsb)
- [@NicolasUrban](https://gitlab.com/nclsurban)
- [@WalidMedouaz](https://gitlab.com/WalidME)




## Feedback

Si vous avez des feedback, merci de nous contacter à l'adresse PdfToTxtLesBoss@gmail.com


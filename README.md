# Parser d'article scientifique

Ce programme est destiné à récupérer les informations d'un article scientifique converti du format PDF au format txt et à extraire les informations essentielles vers une sortie au format txt.

Il permet ainsi d'analyser tous les articles au format txt d'un dossier et de créer des fichiers txt dans un autre dossier contenant les informations essentielles.

Nous utilisons la *version 4.00* de pdftotext, *sans options*.
## Prérequis

Pour éxécuter ce projet, vous avez normalement besoin de l'outil pdftotext.
Pour l'installer, vous pouvez éxécuter la commande suivante dans un terminal Linux.

`sudo apt install poppler-utils` ou `sudo apt install poppler-utils`

### ATTENTION
Nous avons rencontré des soucis sur la version de notre pdftotext (4.0) :
Nous nous étions basé sur toute une version avec laquelle nous ne pouvions pas interpréter avec Python.
Nous avons fait part de notre problème à M. Moreno Jimenez Luis Gil ainsi qu'à M. Juan-Manuel Torres-Moreno et nous nous sommes mit d'accord : 
- Les corpus donnés dans le dossier "Corpus" sont **déjà au format txt** et non au format pdf.
- Notre programme permet ainsi de récupérer les informations présentes dans des fichiers txt.


## Fonctionnalités

- Conversion au format xml
- Conversion au format txt
- Utilisation de l'interface via terminal

## Commandes de lancement

```http
  python3 fichier.py <chemin> (-t | -x) [-n] 
```

| Parametre | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `<chemin>` | `string` | **Requis**. Chemin relatif ou absolu du dossier contenant les articles au format txt |
| `-t` | `string` | **Requis**. Conversion en txt |
| `-x` | `string` | **Requis**. Conversion en xml |
| `-n` | `string` | **Optionnel**. Utiliser les fichiers txt à la place des fichiers pdf |

Extrait toutes les informations des fichiers du dossier indiqué et redirige les sorties vers un dossier ApresAnalyse dans ce même dossier.

## Utilisation de l'interface terminal

L'utilisation de l'interface est réglée par défaut.
Il suffit de lister, séparer par des virgules, les numéros associés aux fichiers que vous voulez analyser.

### Exemple : 
0   fichier0.txt

1   fichier1.txt

2   fichier2.txt

3   fichier3.txt

-1  Quitter

Entrez les numéros des fichier à analyser : 0,1,3

Analysera les fichiers "fichier0.txt","fichier1.txt" et "fichier3"

## Auteurs

- [AbdelghaniRechidi](https://gitlab.com/uapv2002373)
- [HichamGuessab](https://gitlab.com/HichamGsb)
- [NicolasUrban](https://gitlab.com/nclsurban)
- [WalidMedouaz](https://gitlab.com/WalidME)

## Feedback

Si vous avez des feedback, merci de nous contacter à l'adresse PdfToTxtLesBoss@gmail.com
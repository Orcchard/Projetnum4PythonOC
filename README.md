# Gestionnaire de tournois d'échecs

> Ce programme Python permet d'organiser et  de suivre des tournois d'échecs, avec sauvegarde des données en JSON.

## Prérequis

1. **Installer Python**, en vous rendant sur le site: [python.org/downloads](https://www.python.org/downloads)                                       ***Testé sous Windows 11 avec Python 3.12***

2. **Clonez le dépôt**: git clone [https://github.com/Orcchard/Projetnum4PythonOC.git](https://github.com/Orcchard/Projetnum4PythonOC.git)                              Ou téléchargez le ZIP via le bouton vert <> Code" > Download ZIP.

3. **Extraire l'ensemble des fichiers**:                                                                                Décompressez l'archive dans le repertoire de votre choix.

4. **Créez et activez l'environnement virtuel** dans votre editeur de code à l'aide de la commande :                                                  
**Windows** : python -m venv env puis  env\scripts\activate                                        
**Linux/macOS**: python -m venv env puis source env/bin/activat

5. **Installez les bibliothèques** :                                                                                                   pip install -r requirements.txt

6. **Lancez le script** python main.py

## **Générer le rapport Flake8**
 Flake8 va scanner le fichier "main" ainsi que les fichiers se trouvant dans les dossiers
 "controller", "models" et "views". Le rapport sera exporté au dans le fichier "index.html"
 situé dans le dossier "flake8-report"

a) **Installez flake8** avec la commande:  pip intall flake8-html

    S'il n'existe pas, créer un fichier .flake8  
    
   Y ecrire le texte suivant :  
   
   [flake8]  
   
max-line-length = 119  

exclude = env,venv,.venv,****pycache****,.git,.pyc,.pyo,*.pyd,.gitignore*



b) **Generer le rapport** : Saisissez la commande flake8 --format=html --htmldir=flake8_report --exit-zero  
        

    

c) Ouvrir le rapport

**Windows (PowerShell)** : **Invoke-Item flake8_report/index.html**

**Linux/macOS** :**xdg-open flake8_report/index.html**  

Si aucune erreur apparaitra:

 ![image](https://github.com/user-attachments/assets/7a8c86ff-9b15-4b77-9b1b-0b2067b5868f)





## Utilisation  


Le menu principal est divisé en 3 options.

![image](https://github.com/user-attachments/assets/ee02b24b-909d-460c-a640-a51a62fc0908)







##### 1. Créer un joueur

Ajoute un joueur dans Le fichier json nommé "all_player_data" prè alimenté.

##### 2) Créer un tournoi

* Cette section permet de créer et sauvegarder  un tournois dans "tournament_data.json"
* Vous serez  ensuite invité à choisir les 8 participants à ce tournois, en saisissant les 3 premières lettres du nom.

##### 3) Afficher des rapports

Cette section vous permet de générer différents rapport. Vous pouvez consulter:

1. La liste de tous les joueurs sauvegardés dans la base de donnée json.
2. La liste de tous les tournois enregistrés avec le nombre de rounds déjà joués.
3. Les joueurs d’un tournoi de votre choix, triés par leur score (décroissant)
4. Les détails complets d'un tournoi : (classement des joueurs, tours et matchs)

#### 4) Reprendre un tournoi
 Il est possible de directement commencer le tournoi lors de sa création, on peut également retourner au menu principal et le
 reprendre plus tard. Reprendre un tournois c'est se retrouver exactement à l'étape où le tournoi a été sauvegardé, avec tous les matchs, scores et participants intacts ou sans aucun rounds démarrés.


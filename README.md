# HMP - Formation DevSecOps

L'objectif de ce repository est de pouvoir fournir une formation d'introduction au DevSecOps. Pour cela on exploite une vulnérabilité qui permet à un utilisateur d'exécuter du code en injectant un fichier YAML.
L'application permet à un utilisateur de selectionner un fichier YAML et de l'upload. Il intègre, par défaut, la version 5.3 de la bibliothèque PyYAML qui est vulnérable. 

POC : https://gist.github.com/adamczi/23a3b6d4bb7b2be35e79b0667d6682e1

## Pré-requis :
- Avoir Git
- Avoir un PC sous Windows
- Python 
- Avoir un compte github
- De préférence, avoir un éditeur de code (ex: VS Code)

## Etapes à suivre :

### I - Préparation de l'environnement
1) Faire un fork de ce [projet](https://github.com/HMP-DSO/Formation-DSO) vers votre répository Head Mind.

2) Cliquer sur code (bouton vert), dans HTTPS copier l'URL (.git) et aller dans votre invite de commande et taper la commande :
```
git clone [URL .git]
```

### II - Découverte et test de l'application

2) Ouvrez le fichier requirements.txt et vérifier que la version de PyYAML est bien la 5.3 "PyYAML==5.3". (Si besoin taper: pip install pyyaml==5.3)

3) Avec python, exécutez :
```
application.py
```

4) Allez sur le navigateur et dans la barre de navigation tapez "127.0.0.1:5000". Vous devriez tomber sur un site web d'analyse de fichier de configuration 

5) Dans l'onglet "Upload", sélectionnez et upload le fichier "payload.yaml". Regardez alors votre terminal. La commande "dir" s'est exécutée et vous pouvez voir la liste des fichiers et dossiers de votre répertoire. Cela veut donc dire que la vulnérabilité a bien été exploitée.
Avec CTRL+C il est possible d'arréter l'exécution de l'application dans votre terminal. 

### III - Branch dev

5) Créer une nouvelle branch 'dev' et aller dessus
```
git branch dev
git checkout dev
```

### IV - Correction de la vuln

6) Tapez la commande "pip install pyyaml==5.3.1". La vulnérabilité que l'on vient d'exploiter a été corrigée dans la version PyYAML 5.3.1. Utiliser le script "update_requirements.py" pour mettre à jour le fichier requirements.txt

7) Relancez l'application et vérifiez que le fichier "requirements.txt" s'est bien mis à jour et que la version de PyYAML est bien la 5.3.1 "PyYAML==5.3.1".

8) Aller sur le navigateur et dans la barre de navigation taper "127.0.0.1:5000". Essayer à nouveau d'envoyer le fichier YAML et regarder le terminal. Une erreur (500) devrait apparaître. Il n'est donc plus possible d'exploiter la vulnérabilité.

9) Faire un git add / git commit / git push de l'application avec la nouvelle version de PyYAML vers la branch dev.

10) Faire un merge de la branch dev vers la branch main
```
git merge [branch]
```
#Help :
Supprimer tt les containers:
docker ps -aq | ForEach-Object { docker rm -f $_ } 
   
____________________________________________________________________________________________________________
   ![HMP](https://github.com/user-attachments/assets/e7576c9a-c7bd-4150-aba2-9adee745a976)



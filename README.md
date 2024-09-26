<<<<<<< HEAD
# HMP - Formation DevSecOps

L'objectif de ce repository et de pouvoir fournir une formation DevSecOps la plus complète possible. Pour cela on exploite une vulnérabilité qui permet à un utilisateur d'exécuter du code en injectant un fichier YAML.
L'application permet à un utilisateur de selectionner un fichier YAML et de l'upload. Il intègre, par défaut, la version 5.3 de la bibliothèque PyYAML qui est vulnérable. 

POC : https://gist.github.com/adamczi/23a3b6d4bb7b2be35e79b0667d6682e1
test
A faire :
- Finir présentation ppt
- Faire un rapport rapide de correction
- Ajouter mes/nos contact (Moi &/ou Joseph)
- Ajouter du story telling (Exploiter le fichier YAML)

Pré-requis :
- Avoir Git
- Avoir un PC sous Windows
- Avoir un compte github

Github :
1) Après s'être connecté, créer un repository
2) Une fois le repo créé, aller dans "code" en haut et cliquier sur le bouton vert "<> CODE" Puis sur le deux carrés "Copy url to clipboard"
3) Aller sur votre terminal et faites le commande suivi de ce qui a été copié "git clone <url>", cela va permettre de télécharger votre repository. Attention, si vous avez l'erreur "Repository not found", utiliser le même URL mais avec le username@ ex: git clone https://'username'@github.com/HMP-DSO/Formation-DSO.git
4) git pull --allow-unrelated-histories
5) git push

Etapes à suivre :

1) Téléchargez le fichier ZIP via GitHub et décompressez-le, puis copiez les fichiers dans le répertoire que vous avez cloné précédemment

2) Ouvrir le fichier requirements.txt et vérifier que la version de PyYAML est bien la 5.3 "PyYAML==5.3"

3) Avec python, lancer "application.py"

4) Aller sur le navigateur et dans la barre de navigation taper "127.0.0.1:5000". Vous devriez tomber sur un application simple qui vous demande d'upload un fichier

5) Selectionner et upload le fichier "payload.yaml" et regarder votre terminal. La commande "dir" s'est exécutée et vous pouvoir la liste des fichiers et dossiers de votre repertoire. Cela veut donc dire la vulnérabilité a bien été exploitée.

6) Avec CTRL+C arréter l'exécution de l'application dans votre terminal. Taper la commande "pip install pyyaml==5.3.1". La vulnérabilité que l'on vient d'exploiter a été corrigée dans la version PyYAML 5.3.1.

7) Relancer l'application et vérifier quand le fichier "requirements.txt" s'est bien mis à jour et que la version de PyYAML est bien la 5.3.1 "PyYAML==5.3.1"

8) Aller sur le navigateur et dans la barre de navigation taper "127.0.0.1:5000". Essayer à nouveau d'envoyer le fichier YAML et regarder le terminal. Une erreur (500) devrait apparaître. Il n'est donc plus possible d'exploiter la vulnérabilité.
   
____________________________________________________________________________________________________________
   ![HMP](https://github.com/user-attachments/assets/e7576c9a-c7bd-4150-aba2-9adee745a976)



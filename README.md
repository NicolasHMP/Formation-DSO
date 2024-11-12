# HMP - Formation DevSecOps

L'objectif de ce repository est de pouvoir fournir une formation d'introduction au DevSecOps. Pour cela on exploite une vulnérabilité qui permet à un utilisateur d'exécuter du code en injectant un fichier YAML.
L'application permet à un utilisateur de selectionner un fichier YAML et de l'upload. Il intègre, par défaut, la version 5.3 de la bibliothèque PyYAML qui est vulnérable. 

POC : https://gist.github.com/adamczi/23a3b6d4bb7b2be35e79b0667d6682e1

Pré-requis :
- Avoir Git
- Avoir un PC sous Windows
- Python 
- Avoir un compte github
- De préférence, avoir un éditeur de code (ex: VS Code)

Github :
1) Après s'être connecté, créer un repository.
2) Une fois le repo créé, aller dans "code" en haut et cliquer sur le bouton vert "<> CODE" Puis sur les deux carrés "Copy url to clipboard".
3) Aller sur votre terminal et faites la commande suivie de ce qui a été copié "git clone \<url\>", cela va permettre de télécharger votre repository. Attention, si vous avez l'erreur "Repository not found", utiliser le même URL mais avec le username de votre compte suivi de '@'. ex: git clone https://'username'@github.com/HMP-DSO/Formation-DSO.git.
5) Votre répertoire est maintenant prêt.

Etapes à suivre :

1) Téléchargez le fichier [ZIP de ce projet](https://github.com/HMP-DSO/Formation-DSO/archive/refs/heads/main.zip) via GitHub et décompressez-le, puis copiez les fichiers dans le répertoire que vous avez cloné précédemment. //Gitclone

2) Ouvrez le fichier requirements.txt et vérifier que la version de PyYAML est bien la 5.3 "PyYAML==5.3". (Si besoin taper: pip install pyyaml==5.3)

3) Avec python, lancez "application.py"

4) Allez sur le navigateur et dans la barre de navigation tapez "127.0.0.1:5000". Vous devriez tomber sur un site web d'analyse de fichier de configuration !

5) Dans l'onglet "Upload", sélectionnez et upload le fichier "payload.yaml". Regardez alors votre terminal. La commande "dir" s'est exécutée et vous pouvez voir la liste des fichiers et dossiers de votre répertoire. Cela veut donc dire que la vulnérabilité a bien été exploitée.

6) Avec CTRL+C arrétez l'exécution de l'application dans votre terminal. Tapez la commande "pip install pyyaml==5.3.1". La vulnérabilité que l'on vient d'exploiter a été corrigée dans la version PyYAML 5.3.1.

7) Relancez l'application et vérifiez que le fichier "requirements.txt" s'est bien mis à jour et que la version de PyYAML est bien la 5.3.1 "PyYAML==5.3.1".

8) Aller sur le navigateur et dans la barre de navigation taper "127.0.0.1:5000". Essayer à nouveau d'envoyer le fichier YAML et regarder le terminal. Une erreur (500) devrait apparaître. Il n'est donc plus possible d'exploiter la vulnérabilité.

#Help :
Supprimer tt les containers:
docker ps -aq | ForEach-Object { docker rm -f $_ } 
   
____________________________________________________________________________________________________________
   ![HMP](https://github.com/user-attachments/assets/e7576c9a-c7bd-4150-aba2-9adee745a976)



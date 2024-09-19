# pyyaml==5.3 required. Vulnerability has been fixed in 5.3.1   
# pip install PyYAML==5.3 / Correction pip install PyYAML==5.4
# CVE-2020-1747 

import yaml
import subprocess
import os
from colorama import Style, Fore, init
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from pathlib import Path
import sys

#Init est utilisé pour l'ajout de coleur dans le code
init()

secret="azerty123"

#Permet de définir l'application Flask
app = Flask(__name__)

#Permet d'exécuter le fichie HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/error')
def error():
    return render_template('error.html')

#Crée le /upload du HTML et permet de sélectionner un fichier et de l'envoyer
@app.route('/uploaded', methods=['GET', 'POST'])
def uploaded():
    if request.method == 'POST':

        #Permet la récupération du fcihier depuis l'HTML
        if 'file' not in request.files:
            err = "No file part"
            return render_template('error.html', err=err)
        file = request.files['file']
        if file.filename == '':
            err = "No selected file"
            return render_template('error.html', err=err)
            #return f'{Fore.RED}[-] No selected file{Fore.RESET}'
        
        file_name = file.filename
        #Check si le fichier entré est bon (test pour répondre à CodeQL)
        if ".." in file_name or "/" in file_name or "\\" in file_name:
            err = "Invalid filename"
            return render_template('error.html', err=err)
            #raise ValueError(f"{Fore.RED}[-] Invalid filename : {file.filename}{Fore.RESET}")
        else:
            file_content = process_file(file_name)
            string_file_content = str(file_content)
            if string_file_content.__contains__('Errno'):
                err = file_content
                return render_template('error.html', err=err)
            else:
                print(f"{Fore.GREEN}[+] file uploded !{Fore.RESET}")
    return render_template('upload.html', file_content=file_content)

#Utilisation de la fonction vulnérable selon le POC de la CVE-2020-1747
def process_file(file_name):
    """Lit le fichier texte et retourne son contenu. Pour d'autres types de fichiers, ajustez le traitement."""
    #Chargement du fichier YAML
    if ".yaml" in file_name or ".yml" in file_name:
        try:
            with open(file_name,'rb') as f:
                content = f.read()
                data = yaml.load(content, Loader=yaml.FullLoader) # Using vulnerable FullLoader
        except Exception as er:
            print(f"{Fore.RED}[-] {er}{Fore.RESET}")
            return er
        #Exécution de la fonction vulnérable

        return data
    else:
        err = "Upload file is not a YAML file"
        return render_template('error.html', err=err)
        #return f"{Fore.RED}[-] Uploaded file is not a YAML file.{Fore.RESET}"

#Permet de générer le fichier requirements.txt
def gen_reqtxt(directory):

    #Exécute pipreqs pour récupérer le nom des libs à mettre dans le requirements.txt
    subprocess.run([sys.executable, "-m", "pipreqs.pipreqs", "--force", directory])
    with open("installed_versions.txt", "w") as f:
        try:
            subprocess.run(["pip", "freeze"], stdout=f)
        except Exception as e:
            print(f'{Fore.RED}Erreur dans le fichier de freeze{Fore.RESET}')

    #Récupère toutes les dépendances installées avec leur version
    all_lib_install = []
    with open("installed_versions.txt", "r") as file_install:
        for ligne in file_install:
            all_lib_install.append(ligne)
    os.remove("installed_versions.txt")

    #Récupère seulement le pattern (sans les versions) des dépendances à ajouter dans requirements.txt (ex: PyYAML==)
    lib_pipreqs = []
    with open("requirements.txt", "r") as file_pipreqs:
        for ligne in file_pipreqs:
            lib_pipreqs.append(ligne[:ligne.index('==')+2])

    #Fait le match pour récupérer les versions des dépendances présentes dans pipreqs
    final_lib = []
    for value in all_lib_install:
        if value[:value.index('==')+2] in lib_pipreqs:
            final_lib.append(value)

    #Ecrit le réquirements.txt
    with open("requirements.txt", "w") as f:
        for item in final_lib:
            f.write(item)

if __name__ == '__main__':
    #Récupère le path de l'application
    directory = f'{Path(__file__).parent}'
    gen_reqtxt(directory)
    app.run(debug=False)

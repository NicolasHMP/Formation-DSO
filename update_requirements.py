from pathlib import Path
import subprocess
import sys
from colorama import Style, Fore, init
import os

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
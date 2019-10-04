#!C:\Python3\python.exe

import sys

nb_ligne_comment = 0
nb_ligne_empty = 0
nb_fonction = 0
nb_ligne_total = 0
nb_ligne_code = 0

print(f"Traitement su fichier : {sys.argv[1]}")
with open(sys.argv[1], 'r') as file_read:
    for line in file_read:
        nb_ligne_total += 1
        if line[0] == '\n':
            nb_ligne_empty += 1
        else:
            line_pure = line.strip(' ')
            first_car = line_pure[0]
            four_car = line_pure[:4]
            if first_car == '#':
                nb_ligne_comment += 1
            elif four_car == 'def ':
                nb_fonction += 1
                nb_ligne_code += 1
            else:
                nb_ligne_code += 1

print(f"Nombre de ligne vide : {nb_ligne_empty}")
print(f"Nombre de ligne de commentaire : {nb_ligne_comment}")
print(f"Nombre de fonctions : {nb_fonction}")
print(f"Nombre de ligne de code : {nb_ligne_code}")
print(f"Nombre de ligne total : {nb_ligne_total}")
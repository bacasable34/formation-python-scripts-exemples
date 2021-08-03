#! /usr/bin/env python3
#
# parfait_en_ligne.py - Mickaël Seror
# affiche les nombres entiers compris entre 6 et 28
# sur une seule ligne.
#
# Usage : ./parfait_en_ligne.py
#
# 2020.01.04 : version originale

nb_print=""
nombre=6
while nombre<=28:
    if nb_print=="":
        nb_print += str(nombre)
    else:
        nb_print+=" ; " + str(nombre)
    nombre+=1
print(nb_print)
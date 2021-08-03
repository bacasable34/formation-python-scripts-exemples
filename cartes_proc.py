#! /usr/bin/env python3
#
# carte_proc.py - Mickaël Seror
#
# Usage : ./carte_proc.py
#
# 2020.01.05 : version originale

def couleur(numcoul):
    if numcoul == 1:
        print("pique")
    elif numcoul == 2:
        print("coeur")
    elif numcoul == 3:
        print("trèfle")
    elif numcoul == 4:
        print("carreau")

def valeur(numval):
    if numval == 1:
        print("as")
    elif numval <= 13:
        print(str(numval))

couleur(2)
valeur(1)
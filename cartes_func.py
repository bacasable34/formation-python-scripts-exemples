#! /usr/bin/env python3
#
# carte_func.py - Mickaël Seror
#
# Usage : ./carte_func.py
#
# 2020.01.05 : version original

def couleur(numcoul):
    if numcoul == 1:
        return("pique")
    elif numcoul == 2:
        return("coeur")
    elif numcoul == 3:
        return("trèfle")
    elif numcoul == 4:
        return("carreau")

def valeur(numval):
    if numval == 1:
        return("as")
    elif numval <= 13:
        return(str(numval))

print(couleur(2) + "  " + valeur(5))

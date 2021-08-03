#! /usr/bin/env python3
#
# volubile.py - Mickaël Seror
# commente la longueur de la phrase entrée par l'utilisateur.
#
# Usage : ./volubile.py
#
# 2020.01.04 : version originale

phrase = input("Bonjour, Entrer une phrase s'il vous plait : ")
if len(phrase) <10 :
    print("Votre phrase est d'une longueur inférieur à 10 caractères")
elif len(phrase)<=20:
    print("Votre phrase est d'une longueur entre 10 et 20 caractères")
else:
    print("Votre phrase est plus longue de 20 caractères !")

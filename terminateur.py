#! /usr/bin/env python3
#
# terminateur.py - Mickaël Seror
# interroge l'utilisateur jusqu'à  ce qu'il réponde
# "No problemo". Ce programme doit afficher une dernière phrase en quittant.
#
# Usage : ./terminateur.py
#
# 2020.01.04 : version originale

reponse =""
while reponse != "No problemo":
    reponse = input("Est-ce que ça va ? : ")
print("Ben enfin tu vois que ça va finalement !")
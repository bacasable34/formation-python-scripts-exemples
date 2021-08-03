#! /usr/bin/env python3
#
# garfield.py - Mickaël Seror
# Demande le jour de la semaine et souhaite une bonne
# journée à l'utilisateur sauf si c'est un lundi !
# 
# Usage : ./garfield.py
#
# 2020.01.04 : version originale

jour = input("Bonjour, quel jour de semaine sommes-nous aujourd'hui ? : ")
if jour == "lundi":
    print("je n'aime pas le lundi !")
else:
    print("Bonne journée !")



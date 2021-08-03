#! /usr/bin/env python3
#
# is_what.py - Mickaël Seror
# Détermine et affiche la composition du mot saisi par l'utilisateur
# si ce mot contient des lettres, on veut savoir si il y a
# uniquement des lettres, uniquement des minuscules, et uniquement des majuscules
# et si ce mot contient des chiffres on veut savoir s'il est composé uniquement de chiffres
#
# usage : ./is_what.py
#
# 2020.01.10 : version originale
alphabet='abcdefghijklmnopqrstuvwxyz'
chiffres = ['0','1','2','3','4','5','6','7','8','9']
mot=input('Entrer un mot : ')
print('liste1 : ' + str([l in alphabet for l in mot.lower()]))
print('liste2 : ' + str([True for me in mot]))
if [l in alphabet for l in mot.lower()]!=[False for m in mot]:
    print('mot contient au moins une lettre')
if [l in alphabet for l in mot.lower()]==[True for m in mot]:
    print('mot contient que des lettres')
if [l in alphabet for l in mot]==[True for m in mot]:
    print('mot contient que des lettres en minuscule')
elif [l in alphabet.upper() for l in mot]==[True for m in mot]:
    print('mot contient que des lettres en majuscule')
if [l in chiffres for l in mot]!=[False for m in mot]:
    print('mot contient au moins un chiffre')
    if [l in chiffres for l in mot]==[True for m in mot]:
        print('mot contient que des chiffres')
    else:
        print('mot ne contient pas que des chiffres')
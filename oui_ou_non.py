#! /usr/bin/env python3
#
# oui_ou_non.py - Mickaël Seror
# Déterminer si l'utilisateur a répondu à l'affirmative par oui, Oui ou OUI
# ou à la négative par non, Non ou NON
#
# Usage : ./oui_ou_non.py
#
# 2020.01.10 : version originale

ouiounon = input('dite oui ou non : ')
if ouiounon.lower()=="oui":
    print('Vous avez répondu par l\'affirmative en écrivant ' + ouiounon + ' !') 
elif ouiounon.lower()=="non":
    print('Vous avez dit par la négative en écrivant ' + ouiounon + ' !')
else:
    print('Vous n\'avez pas compris ce qui était demandé...')
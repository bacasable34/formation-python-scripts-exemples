#! /usr/bin/env python3
#
# coquillages.py - Mickaël Seror
# affiche les mois en r de l'année.
#
# Usage : ./coquillages.py
#
# 2020.01.04 : version originale

for mois in "Janvier","Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre":
    if "bre" in mois[len(mois)-3:len(mois)]:
        print(mois)
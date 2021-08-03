#! /usr/bin/env python3
#
# taxi.py - Mickaël Seror
# programme donnant le tarif du taxi
#
# Usage : ./taxi.py
#
# 2020.01.05 : version originale

prise_en_charge=2
A=0.91
B=1.35
C=1.82
D=2.7

def course(distance, tarif=C, minimum=prise_en_charge, supplement=0):
    return distance*tarif+minimum+supplement
print("Le montant de la course est de : " + str(course(50,A)) + " euros")
#! /usr/bin/env python3
#
# ascii.py - Mickaël Seror
# Affiche le code binaire, octal, hexadécimal et décimal des 128 caractères de la table ASCII
#
# Usage : ./ascii.py
#
# 2021.01.11 : version originale

code = 1
while code <= 128:
    print('{1:2} | {0:^8b} | {0:^8o} | {0:^8X} | {0:^8}'.format(code, chr(code)))
    code+=1

#! /usr/bin/env python3
#
# ascii_range.py - Mickaël Seror
# Affiche le code binaire, octal, hexadécimal et décimal des 128 caractères de la table ASCII
#
# Usage : ./ascii_range.py
#
# 2021.01.14 : version originale

code = tuple(range(1,128,1))
for c in code:
    print('{1:2} | {0:^8b} | {0:^8o} | {0:^8X} | {0:^8}'.format(c, chr(c)))
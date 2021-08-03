#! /usr/bin/env python3
#
# programme is_caracteres.py - Mickaël Seror
# affiche les caractères et leurs caractèristiques
#
# Usage : ./is_caracteres.py
#
# 2020.01.06 : version originale

for caractere in 'Aé9<.µ$¤€²_\\a\\nb c\td':
    resultat = caractere + ' : '
    resultat += 'alnum-'        if caractere.isalnum()       else '     -'
    resultat += 'alpha-'        if caractere.isalpha()       else '     -'
    resultat += 'decimal-'      if caractere.isdecimal()     else '       -'
    resultat += 'digit-'        if caractere.isdigit()       else '     -'
    resultat += 'identifier-'   if caractere.isidentifier()  else '          -'
    resultat += 'lower-'        if caractere.islower()       else '     -'
    resultat += 'numeric-'      if caractere.isnumeric()     else '       -'
    resultat += 'printable-'    if caractere.isprintable()   else '          -'
    resultat += 'space-'        if caractere.isspace()       else '     -'
    resultat += 'title-'        if caractere.istitle()       else '     -'
    resultat += 'upper-'        if caractere.isupper()       else '     -'    
    print(resultat)

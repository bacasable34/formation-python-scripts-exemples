#! /usr/bin/env python3
#
# who_are_you.py - Mickaël Seror
# Demande votre prénom et vous congratule en tant
# qu'expert si celui-ci est Horation, Mac ou Gil.
#
# Usage : ./who_are_you.py
#
# 2020.01.04 : version originale

prenom = input('Donner votre prénom : ')
if prenom in ("Horatio","Mac","Gil"):
    print("Bravo vous êtes un expert " + prenom + " !")


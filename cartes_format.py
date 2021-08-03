#! /usr/bin/env python3
# programme cartes.py

def couleur(numcoul):
    if numcoul == 1:
        return("pique")
    elif numcoul == 2:
        return("coeur")
    elif numcoul == 3:
        return("trèfle")
    elif numcoul == 4:
        return("carreau")

def valeur(numval):
    if numval == 14:
        return("as")
    elif numval == 13:
        return("Roi")
    elif numval == 12:
        return("Dame")
    elif numval == 11:
        return("Vallet")
    elif numval <= 52:
        return(str(numval))

numcoul=1
while numcoul <= 4:
    numval = 2
    while numval < 14:
        numval+=1
        print('|{0:10}|{1:10}|'.format(valeur(numval),couleur(numcoul)))
    #print("Change de couleur ...")
    numcoul+=1
#! /usr/bin/env python3
#
# test_sub.py - Mickaël Seror
# demande à l'utilisateur une chaine et une sous chaine
# Compte le nombre de fois qu'apparaît la sous chaine dans la chaine
# affiche les positions de la sous chaine dans la chaine
# affiche la chaine avec le caractère * à la place de la sous chaine
#
# Usage : ./test_sub.py
#
# 2021.01.09 : version originale

chaine = input('donner une chaîne : ')
sschaine = input('donner une sous-chaîne : ')

print('nombre de fois que la sous chaîne apparaît : ' + str(chaine.count(sschaine)))
# Utilisation de find à la place de index car qd la sschaine n'est pas trouvé find renvoie -1 
# tandis que index renvoie une erreur
pos=chaine.find(sschaine)
while pos>=0:
    print('position de la sous chaine dans la chaine : ' + str(pos))
    pos = chaine.find(sschaine,pos +1)
print('affiche la chaine avec le caractère * à la place de la sous chaine : ' + chaine.replace(sschaine,'*'*len(sschaine)))

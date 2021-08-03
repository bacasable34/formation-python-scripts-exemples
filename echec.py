#! /usr/bin/env python3
# programme echecs.py


damier={}

for x in 'ABCDEFGH':
    for y in (1,2,3,4,5,6,7,8):
        if (x,y) == ('A',1) or (x,y) == ('H',1):
            damier[x,y]='Tour (blanc)'
        elif (x,y) == ('A',8) or (x,y) == ('H',8):
            damier[x,y]='Tour (noir)'
        elif (x,y) == ('B',1) or (x,y) == ('G',1):
            damier[x,y]='Cavalier (blanc)'
        elif (x,y) == ('B',8) or (x,y) == ('G',8):
            damier[x,y]='Cavalier (noir)'
        elif (x,y) == ('C',1) or (x,y) == ('F',1):
            damier[x,y]='Fou (blanc)'
        elif (x,y) == ('C',8) or (x,y) == ('F',8):
            damier[x,y]='Fou (noir)'
        elif (x,y) == ('E',1):
            damier[x,y]='Roi (blanc)'
        elif (x,y) == ('E',8):
            damier[x,y]='Roi (noir)'
        elif (x,y) == ('D',1):
            damier[x,y]='Dame (blanc)'
        elif (x,y) == ('D',8):
            damier[x,y]='Dame (noir)'
        elif y == 2:
            damier[x,y]='Piont (blanc)'
        elif y == 7:
            damier[x,y]='Piont (noir)'
        else:
            damier[x,y]='vide'
print(damier)
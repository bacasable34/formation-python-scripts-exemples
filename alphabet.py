alphabet='abcdefghijklmnopqrstuvwxyz'
car=0
# print(alphabet[0:4])
while car <26:
    #print(str(car+1) + ' ' + alphabet[car])
    #print(alphabet[car])
    if alphabet[car]=='r':
        print(alphabet[car:car+4])
    car+=1
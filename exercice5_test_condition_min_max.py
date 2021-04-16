#!/usr/bin/python

#commun
val1 = int(input("Saisir la valeur 1:"))
val2 = int(input("Saisir la valeur 2:"))


#methode1
while not(val1 > val2):
    print("Valeur min:",val1)
    break

while not(val1 < val2):
    print("Valeur min:",val2)
    break



#Methode2
#liste= [val1, val2]
#val_min=min(liste)
#print("Valeur min:", val_min)
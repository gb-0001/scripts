#!/usr/bin/python

#import pair_impair
#import mini_maxi
import mini_maxid
import pair_impair

typeval = input("La valeur est-elle de type 'numerique' ou 'chaine' ?")

if typeval == "numerique":
    a = str(input("Saisir une valeur a:"))
    b = str(input("Saisir une valeur b:"))
    min1=mini_maxid.mini(a,b)
    max1=mini_maxid.maxi(a,b)
    print("La valeur la plus petite :", min1)
    print("La valeur la plus grande :", max1)
elif typeval == "chaine":
    nombre = int(input("Saisir une valeur:"))
    nombrepair=pair_impair.pair(nombre)
    nombreimpair=pair_impair.impair(nombre)
    if nombrepair:
        print("La fonction pair retourne True pour la valeur {}".format(nombre))
    elif nombreimpair:
        print("La fonction impair retourne True pour la valeur {}".format(nombre))
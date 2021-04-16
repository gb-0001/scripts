#!/usr/bin/python

def pair(nbre):
    calcule=nbre % 2
    if calcule == 0:
        return True

def impair(nbre):
    calcule=nbre % 2
    if calcule != 0:
        return True
'''
nombre = int(input("Saisir une valeur:"))

retourpair=pair(nombre)
retourimpair=impair(nombre)

if retourpair:
    print("La fonction pair retourne True pour la valeur {}".format(nombre))
elif retourimpair:
    print("La fonction impair retourne True pour la valeur {}".format(nombre))
'''
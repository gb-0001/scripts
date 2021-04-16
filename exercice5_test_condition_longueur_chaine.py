#!/usr/bin/python

chaine1 = str(input("Saisir la chaine de caractères 1:"))
chaine2 = str(input("Saisir la chaine de caractères 2:"))

len_chaine1=len(chaine1)
len_chaine2=len(chaine2)

if len_chaine1 > len_chaine2:
    print("Chaine la plus longue:", chaine1)
elif len_chaine1 < len_chaine2:
    print("Chaine la plus longue:", chaine2)
else:
    print("Chaine de longeur identique")

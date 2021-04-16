#!/usr/bin/python

devise = str(input("Saisir la devise 'E' ou '$' à convertir:"))
TAUX_DOL_TO_EUR=0.83
TAUX_EUR_TO_DOL=1.20
if devise == 'E':
    montant = str(input("Saisir le montant en Euro à convertir en Dollars:"))
    calcul= int(montant) * float(TAUX_DOL_TO_EUR)
    print("Le montant en Dollars est:", calcul)
elif devise == '$':
    montant = str(input("Saisir le montant en Dollars à convertir en Euro:"))
    calcul= int(montant) * float(TAUX_EUR_TO_DOL)
    print("Le montant en Dollars est:", calcul)
else:
    print("Saisir E ou $ ")
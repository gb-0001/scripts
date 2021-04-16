#!/usr/bin/python

import os

repertoire_courant=os.getcwd()
contenu=os.listdir(repertoire_courant)
print("Contenu du repertoire courant ==> {} :\n {}".format(repertoire_courant,contenu))

cpt_dossier=0
cpt_fichier=0
for f in contenu:
    if os.path.isdir(f):
        cpt_dossier+=1
    elif os.path.isfile(f):
        cpt_fichier+=1

print()
print("{} dossiers et {} fichiers".format(cpt_dossier,cpt_fichier))
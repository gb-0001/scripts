#!/usr/bin/python

import ex9


#Objet
jeu = ex9.Jeu()

choix = int(input("Saisir 1 pour lister les jeux, 2 pour ajouter un jeu, 3 pour voir les infos du jeu, 4 pour supprimer un jeu:"))

if choix == 1:
    print(jeu.Listejeu())
elif choix == 2:
    jeu.AjoutJeu()
elif choix == 3:
    val1 = int(input("Saisir id du jeu pour voir les infos:"))
    print(jeu.VoirJeu(val1))
elif choix == 4:
    val1 = int(input("Saisir id du jeu à supprimer:"))
    jeu.SupprimeJeu(val1)

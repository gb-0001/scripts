def Listejeu():
    fichier = "jeux.txt"
    fichierjeux=open(fichier, 'r')
    cpt=0
    for line in fichierjeux.readlines():
        cpt+=1
        print(line)
        Nom_jeux,Editeur,Annee_de_sortie,Descriptif,Categorie,Duree,Nombre_de_joueur=line.split(",")
        print(cpt,Nom_jeux,Editeur,Annee_de_sortie,Descriptif,Categorie,Duree,Nombre_de_joueur)
    fichierjeux.close()

Listejeu()

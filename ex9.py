#!/usr/bin/python

class Jeu():
    Nom_jeux = ""
    Editeur = ""
    Annee_de_sortie = ""
    Descriptif = ""
    Categorie = ""
    Duree = ""
    Nombre_de_joueur = ""
    cpt = 0

    def Listejeu(self):
        fichier = "jeux.txt"
        fichierjeux=open(fichier, 'r')
        mondico={}
        for line in fichierjeux.readlines():
            line.strip()
            if line:
                self.cpt+=1
                self.Nom_jeux,self.Editeur,self.Annee_de_sortie,self.Descriptif,self.Categorie,self.Duree,self.Nombre_de_joueur=line.split(",")
                mondico.update({self.cpt: (self.Nom_jeux,self.Editeur,self.Annee_de_sortie,self.Descriptif,self.Categorie,self.Duree,self.Nombre_de_joueur)})

        return mondico
        fichierjeux.close()

    def AjoutJeu(self):
        fichier = "jeux.txt"
        fichierjeux=open(fichier, 'a')
        self.Nom_jeux=input("Saisir Nom du jeu:")
        self.Editeur=input("Saisir Nom de l'editeur:")
        self.Annee_de_sortie=input("Saisir l'a'nnée de sortie:")
        self.Descriptif=input("Saisir le descriptif:")
        self.Categorie=input("Saisir la categorie:")
        self.Duree=input("Saisir la durée:")
        self.Nombre_de_joueur=input("Saisir le nombre de joueur:")
        fichierjeux.write(self.Nom_jeux + "," + self.Editeur + "," + self.Annee_de_sortie + "," + self.Descriptif + "," + self.Categorie + "," + self.Duree + "," + self.Nombre_de_joueur + "\n")
        fichierjeux.close()

    def VoirJeu(self,iddujeu):
        fichier = "jeux.txt"
        fichierjeux=open(fichier, 'r')
        mondico={}
        for line in fichierjeux.readlines():
            self.cpt = self.cpt + 1
            cle = self.cpt
            self.Nom_jeux,self.Editeur,self.Annee_de_sortie,self.Descriptif,self.Categorie,self.Duree,self.Nombre_de_joueur=line.split(",")
            mondico.update({cle: (self.Nom_jeux,self.Editeur,self.Annee_de_sortie,self.Descriptif,self.Categorie,self.Duree,self.Nombre_de_joueur)})
        fichierjeux.close()
        if iddujeu in mondico:
            return mondico[iddujeu]

    def SupprimeJeu(self,iddujeu):
        fichier = "jeux.txt"
        fichierjeux=open(fichier, 'r')
        mondico={}
        for line in fichierjeux.readlines():
            self.cpt = self.cpt + 1
            cle = self.cpt
            self.Nom_jeux,self.Editeur,self.Annee_de_sortie,self.Descriptif,self.Categorie,self.Duree,self.Nombre_de_joueur=line.split(",")
            mondico.update({cle: (self.Nom_jeux,self.Editeur,self.Annee_de_sortie,self.Descriptif,self.Categorie,self.Duree,self.Nombre_de_joueur)})
        fichierjeux.close()
        if iddujeu in mondico:
            del mondico[iddujeu]
            fichierjeux=open(fichier, 'w')
            fichierjeux.close()
            fichierjeux=open(fichier, 'a')
            for id1,val in mondico.items():
                print("id1",id1)
                print("val",val)
                texttowrite= mondico[id1]
                fichierjeux.write(str(texttowrite) + "\n")
        fichierjeux.close()



'''
demo = Jeu()
demo.Nom_jeux,demo.Editeur,demo.Annee_de_sortie,demo.Descriptif,demo.Categorie,demo.Duree,demo.Nombre_de_joueur=demo.Listejeu()
print(demo.Nom_jeux)
'''

'''
    def VoirJeu(iddujeu):



    def SupprimeJeu(iddujeu):
'''

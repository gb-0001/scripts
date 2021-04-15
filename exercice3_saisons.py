#!/usr/bin/python

hiver=[janvier,fevrier,mars]
printemps=[avril,mai,juin]
ete=[juillet,aout,septembre]
automne=[octobre,novembre,decembre]

saisons= [hiver,printemps,ete,automne]

print("Q1 - Saison[2] affichage des mois de l'été:\n")
print(saisons[2])
print()

print("Q2 - Saison[1][0] affichage du 1er mois du printemps:\n")
print(saisons[1][0])
print()

print("Q3 - Saison[1][0] affichage des mois du printemps et l'ete:\n")
print(saisons[1:2])
print()

print("Q4 - Saison[:][1] affichage des mois du printemps \n")
print(saisons[:][1])
print()
#!/usr/bin/python
semaine = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
print()


print("Retour Q1: les 5 premiers jours\n")
print("{}, {}, {}, {}, {}".format(semaine[0], semaine[1], semaine[2], semaine[3], semaine[4]))
print()

print("Retour Q1: Jour du week-end\n")
print("{}, {}".format(semaine[5], semaine[6]))
print()

print("Retour Q2: les 5 premiers jours\n")
print(semaine[0:5])
print()

print("Retour Q2: Jour du week-end\n")
print(semaine[-2:])
print()

print("Retour Q3: dernier jour de la semaine\n")
print(semaine[len(semaine)-1])

print("Retour Q3: dernier jour de la semaine\n")
print(semaine[-1])
print()


print("Retour Q4: jour de la semaine inversé en une commande\n")
semaine.reverse()
print(semaine)
#print(semaine[::-1])
print()
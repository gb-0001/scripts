def mini(valeur1, valeur2):
    if valeur1 < valeur2 :
        return valeur1
    else :
        return valeur2

def maxi(valeur1, valeur2):
    if valeur1 > valeur2 :
        return valeur1
    else :
        return valeur2

valeur1 = len(input('Valeur 1 :'))

valeur2 = len(input('Valeur 2 :'))

print('Valeur la plus petite : ')
print(mini(valeur1,valeur2))
print('Valeur la plus grande :')
print(maxi(valeur1,valeur2))
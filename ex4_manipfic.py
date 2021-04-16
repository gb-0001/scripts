#!/usr/bin/python


file1 = "ressources/loremipsum.txt"

fileread=open(file1, 'r')
filer=fileread.read()
print(filer)
fileread.close()

fileread=open(file1, 'a+')
filer=fileread.readlines()
filer.insert(4, "\nMa nouvelle chaine insérée dans mon fichier texte au milieu du lorem ipsum\n" )
fileread.seek(0)
fileread.writelines(filer)
fileread.close()

fileread=open(file1, 'r')
filer=fileread.read()
print(filer)
fileread.close()



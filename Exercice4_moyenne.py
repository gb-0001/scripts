#!/usr/bin/python

notesfile = "notes.txt"
notesfile2 = "notes2.txt"

liste=[]
filenotes=open(notesfile, 'r')

for line in filenotes.readlines():
    liste.append(float(line))

moyenne=sum(liste)/len(liste)
print("La moyenne est de ", "%.2f" % moyenne)
filenotes.close()


filenotes2=open(notesfile2, 'a')

filenotes=open(notesfile, 'r')

for line in filenotes.readlines():
    line=float(line)
    if line < 10:
        notedecimale= "%.1f" % line
        filenotes2.write(notedecimale + str(" recalé") + "\n" )
    elif line >= 10:
        notedecimale= "%.1f" % line
        filenotes2.write(notedecimale + str(" admis") + "\n" )

filenotes.close()
filenotes2.close()

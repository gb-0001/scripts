#!/usr/bin/python

liste1=[ '9x1=9','9x2=18','9x3=27','9x4=36','9x5=45','9x6=54','9x7=63','9x8=72','9x9=81']
liste1=list(range(0,9,1))
for val in liste1:
    print("{} x {} = ".format(int(9),val), val x 9 )

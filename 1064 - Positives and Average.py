# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:07:37 2022

@author: Jaykel JJ
"""

i = 0
cont = 0
j = 0

while i <6:
    i = i+1
    numbs = float(input())
    if numbs > 0:
        cont = cont+1
        j = j + numbs

media = j/cont
print("{} valores positivos".format(cont))
print("{:.1f}".format(media))

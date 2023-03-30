# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:02:41 2022

@author: Jaykel JJ
"""

i = 0
cont = 0

while i <6:
    i = i+1
    numbs = float(input())
    if numbs > 0:
        cont = cont+1

print("{} valores positivos".format(cont))

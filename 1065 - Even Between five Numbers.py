# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:18:33 2022

@author: Jaykel JJ
"""

i = 0
cont = 0

while i < 5:
    i = i + 1
    numbs = int(input())
    if numbs%2==0:
        cont = cont + 1
print("{} valores pares".format(cont))
    
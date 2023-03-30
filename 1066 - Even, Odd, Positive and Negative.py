# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:22:49 2022

@author: Jaykel JJ
"""

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
i = 0

while i < 5:
    i = i + 1
    number = int(input())
    if number%2==0:
        cont1 = cont1 + 1
        
    else:
        cont2 = cont2 + 1
        
    if number > 0:
        cont3 = cont3 + 1
        
    elif number < 0:
        cont4 = cont4 + 1

print("{} valor(es) par(es)".format(cont1))
print("{} valor(es) impar(es)".format(cont2))
print("{} valor(es) positivo(s)".format(cont3))
print("{} valor(es) negativo(s)".format(cont4))
        
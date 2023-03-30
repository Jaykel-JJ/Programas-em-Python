# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:12:07 2022

@author: Jaykel JJ
"""

n = int(input("Digite o valor de n: "))

contador=1
fatorial=1

if n==0:
    print(1)

else:
    while contador<=n:
        
        fatorial = fatorial*contador
        contador=contador+1
    print(fatorial)
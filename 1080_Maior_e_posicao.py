# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:30:11 2022

@author: jayke
"""
maior = menor = 0
for c in range(0,10):
    n = int(input())
    if c == 0:
        maior = menor = 0
    else:
        if n>maior:
            maior = n
            loc = c+1
print(maior)
print(loc)

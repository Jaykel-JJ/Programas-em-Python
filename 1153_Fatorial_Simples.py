# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:49:17 2022

@author: jayke
"""
#duas soluções do fatorial
'''from math import factorial
N = int(input())
print(factorial(N))'''

fatorial = 1
N = int(input())
for i in range(N,0,-1):
    fatorial*=i
print(fatorial)

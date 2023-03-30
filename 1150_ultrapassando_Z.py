# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:00:03 2022

@author: jayke
"""
X = int(input())
while True:
    Z = int(input())
    if Z>X:
        break
cont = 0
soma = 0
for i in range(X,Z):
    cont+=1
    soma+=i
    if soma>Z:
        break
print(cont)

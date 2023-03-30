# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:58:10 2022

@author: jayke
"""
soma = 0
cont = 0
while True:
    idade = int(input())
    if idade>0:
        soma+=idade
        cont+=1
        media = soma/cont
    else:
        break
print('{:.2f}'.format(media))

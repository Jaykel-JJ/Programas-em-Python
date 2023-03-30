# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:05:09 2022

@author: Jaykel JJ
"""
x = int(input("Numero: "))

soma = 0

while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print(soma)
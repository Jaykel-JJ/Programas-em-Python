# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:03:04 2022

@author: jayke
"""
numerador = denominador = 1
S = 0
while True:
    div = numerador/denominador
    S+=div
    numerador+=2
    denominador*=2
    if numerador == 39:
        break
print('{:.2f}'.format(S))

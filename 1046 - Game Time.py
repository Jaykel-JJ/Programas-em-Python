# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:57:54 2022

@author: Jaykel JJ
"""

s,f = map(int, input().split())

if s>f:
    horas = 24 - s
    total = horas + f
    print("O JOGO DUROU", total, "HORA(S)")

elif s<f:
    total_1 = f-s
    print("O JOGO DUROU", total_1, "HORAS(S)")

elif s==f:
    print("O JOGO DUROU 24 HORA(S)")
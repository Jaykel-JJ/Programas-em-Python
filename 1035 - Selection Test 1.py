# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:03:02 2022

@author: Jaykel JJ
"""

n = map(int, input().split())
A,B,C,D = n

if B>C and D>A and (C+D)>(A+B) and C>0 and D>0 and A%2==0:
    print("Valores aceitos")

else:
    print("Valores não aceitos")
    
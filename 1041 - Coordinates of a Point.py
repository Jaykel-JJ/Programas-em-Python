# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:14:08 2022

@author: Jaykel JJ
"""

valors = map(float, input().split())

X,Y = valors

if X==0 and Y==0:
    print("Origem")

elif X==0:
    print("Eixo Y")

elif Y==0:
    print("Eixo X")

elif X>0 and Y>0:
    print("Q1")

elif X<0 and Y>0:
    print("Q2")

elif X<0 and Y<0:
    print("Q3")

elif X>0 and Y<0:
    print("Q4")
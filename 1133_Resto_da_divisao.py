# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:20:57 2022

@author: jayke
"""

X = int(input())
Y = int(input())
if X<Y:
    for i in range(X,Y):
        if i%5 == 2 or i%5 == 3 and X!=Y:    
            print(i)
if X>Y:
    for i in range(Y,X):
        if i%5 == 2 or i%5 == 3 and X!=Y:
            print(i)

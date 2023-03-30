# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 21:30:30 2022

@author: jayke
"""
while True:
    X,Y = list(map(int,input().split()))
    if X>Y:
        print('Decrescente')
    if X<Y:
        print('Crescente')
    if X == Y:
        break

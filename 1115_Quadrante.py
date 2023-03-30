# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 21:41:30 2022

@author: jayke
"""
while True:
    X,Y = list(map(int,input().split()))
    if X>0 and Y>0:
        print('primeiro')
    elif X<0 and Y>0:
        print('segundo')
    elif X<0 and Y<0:
        print('terceiro')
    elif X>0 and Y<0:
        print('quarto')
    if X==0 or Y==0:
        break

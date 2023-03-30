# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 21:51:15 2022

@author: jayke
"""
N = int(input())
for i in range(N):
    X,Y = list(map(int,input().split()))
    if Y !=0:
        div = X/Y
        print('{:.1f}'.format(div))
    else:
        print('divisao impossivel')

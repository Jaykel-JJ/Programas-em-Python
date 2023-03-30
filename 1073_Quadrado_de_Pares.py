# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:28:51 2022

@author: jayke
"""
N = int(input())
for i in range(1,N+1):
    par = i % 2
    if par == 0:
        quad = pow(i,2)
        print('{}^2 = {}'.format(i,quad))

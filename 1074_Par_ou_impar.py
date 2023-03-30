# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:05:36 2022

@author: jayke
"""
N = int(input())
for i in range (0,N):
    X = int(input())
    if X % 2 == 0 and X >0:
        print('EVEN POSITIVE')
    elif X % 2 == 0 and X<0:
        print('EVEN NEGATIVE')
    elif X % 2 != 0 and X>0:
        print('ODD POSITIVE')
    elif X % 2 != 0  and X<0:
        print('ODD NEGATIVE')
    elif X == 0:
        print('NULL')

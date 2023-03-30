# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:03:23 2022

@author: jayke
"""
a = int(input())
b = int(input())
Sum = 0
if a<b:
    for i in range(a,b+1):
        if i%13!=0:
            Sum+=i
if a>b:
    for i in range(b,a+1):
        if i%13!=0:
            Sum+=i
print(Sum)

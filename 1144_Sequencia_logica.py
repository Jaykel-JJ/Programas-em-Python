# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:16:36 2022

@author: jayke
"""
N = int(input())
c = 1
for i in range(1,N+1):
    print('{} {} {}'.format(i,pow(i,2),pow(i,3)))
    print('{} {} {}'.format(i,pow(i,2)+1,pow(i,3)+1))

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:15:04 2022

@author: jayke
"""
tot_in = tot_out = 0
N = int(input(''))
for i in range(1,N+1):
    X = int(input(''))
    if X>=10 and X<=20:
        tot_in +=1
    else:
        tot_out+=1
print('{} in'.format(tot_in))
print('{} out'.format(tot_out))

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:45:29 2022

@author: jayke
"""
v1 = -1
v2 = 1
N = int(input())
for cont in range(1,N+1):
    v3 = v2+v1
    v1 = v2
    v2 = v3
    print('{}'.format(v2),end=' ')
print()

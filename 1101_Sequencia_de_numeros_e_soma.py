# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:57:25 2022

@author: jayke
"""
while True:
    M,N = list(map(int,input('\n').split()))
    Sum = 0
    if M <= 0 or N <= 0:
        break
    if M<N:
        for i in range(M,N+1):
            Sum+=i
            print(i,end=' ')
        print('Sum={}'.format(Sum))
    if M>N:
        for i in range(N,M+1):
            Sum+=i
            print(i,end=' ')
        print('Sum={}'.format(Sum))

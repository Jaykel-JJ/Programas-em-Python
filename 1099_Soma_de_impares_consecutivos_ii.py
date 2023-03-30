# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:53:45 2022

@author: jayke
"""
Sum = 0
N = int(input())
for i in range(N):
    X,Y = list(map(int,input().split()))
    if X<Y:
        for i in range(X,Y):
            if i%2!=0:
                Sum+=i
                print(Sum)
                Sum = 0
    if X>Y:
        for i in range(Y,X):
            if i%2!=0:
                Sum+=i
                print(Sum)
                Sum = 0
    if X == Y or X-Y == -1 or Y-X==1:
        print(0)

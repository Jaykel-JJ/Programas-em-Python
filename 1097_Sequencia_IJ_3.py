# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:22:33 2022

@author: jayke
"""
i = 1
while i<=9:
    
    if i == 1:
        for j in range(7,4,-1):
            print('I={} J={}'.format(i,j))
    elif i ==3:
        for j in range(9,6,-1):
            print('I={} J={}'.format(i,j))
    elif i == 5:
        for j in range(11,8,-1):
            print('I={} J={}'.format(i,j))
    elif i == 7:
        for j in range(13,10,-1):
            print('I={} J={}'.format(i,j))
    elif i == 9:
        for j in range(15,12,-1):
            print('I={} J={}'.format(i,j))
    i+=2

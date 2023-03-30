# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:50:24 2022

@author: jayke
"""
alcool = gas = diesel = n = 0
while (n!=4):
    n = int(input())
    if n==1:
        alcool+=1
    if n ==2:
        gas+=1
    if n ==3:
        diesel+=1
    if n == 4:
        break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gas))
print('Diesel: {}'.format(diesel))

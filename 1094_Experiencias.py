# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:26:26 2022

@author: jayke
"""
C = R = S = Total = 0
N = int(input())
for i in range(0,N):
    Quantia,Tipo = list(map(str,input().split()))
    Quantia = int(Quantia)
    if Tipo == 'C':
        C+=Quantia
    elif Tipo == 'R':
        R+=Quantia
    elif Tipo == 'S':
        S+=Quantia
    Total = C+R+S
x = (C*100)/Total
y = (R*100)/Total
z = (S*100)/Total
print('Total: {} cobaias'.format(Total))
print('Total de coelhos: {}'.format(C))
print('Total de ratos: {}'.format(R))
print('Total de sapos: {}'.format(S))
print('Percentual de coelhos: {:.2f} %'.format(x))
print('Percentual de ratos: {:.2f} %'.format(y))
print('Percentual de sapos: {:.2f} %'.format(z))

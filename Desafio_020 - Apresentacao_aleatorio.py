# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:37:45 2022

@author: jayke
"""

from random import shuffle

a = str(input('Digite o 1° nome: '))
b = str(input('Digite o 2° nome: '))
c = str(input('Digite o 3° nome: '))
d = str(input('Digite o 4° nome: '))

lista = [a,b,c,d]

shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))

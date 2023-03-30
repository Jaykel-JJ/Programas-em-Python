# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:18:20 2022

@author: jayke
"""
#importando a biblioteca math
from math import radians,sin,cos,tan
#entrada de dados
n = float(input('Digite um ângulo: '))
#calculos
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))
#saida de dados
print('O ângulo de {} tem seno de {:.2f}'.format(n,seno))
print('O ângulo de {} tem cosseno de {:.2f}'.format(n,cosseno))
print('O ângulo de {} tem tangente de {:.2f}'.format(n,tangente))

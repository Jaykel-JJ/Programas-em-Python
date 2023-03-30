# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:51:41 2022

@author: jayke
"""
#importando a biblioteca math
from math import hypot
#entrada de dados
C_a = float(input('Digite o valor do cateto adjascente: '))
C_o = float(input('Digite o valor do cateto oposto: '))
#usando o comando maht.hypot para calcular a hipotenusa
hip = hypot(C_a,C_o)
#saida de dados
print('Cateto adjascente {} + Cateto oposto {} resulta na sua hipotenusa {:.2f}.'.format(C_a,C_o,hip))

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:36:58 2022

@author: jayke
"""
#entrada com o valor
n = float(input('Qual o preço do produto? '))

#calculando o 5% de desconto
desc = (n*5)/100
#calculando o novo preço
nprec = n-desc

#dando print no preco
print('O produto com 5% de desconto vai custar R$ {:.2f} reais.'.format(nprec))
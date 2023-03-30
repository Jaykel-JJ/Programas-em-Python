# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:49:38 2022

@author: jayke
"""
#entrada de dados
km = float(input('Digite a quantidade de Km percorrido:'))
dias = int(input('Digite a quantidade de dias que o carro ficou alugado'))

#calculos
preco = (60*dias)+(0.15*km)

#saida de dados
print('O preco a pagar será de {}'.format(preco))

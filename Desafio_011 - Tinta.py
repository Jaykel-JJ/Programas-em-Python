# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:31:21 2022

@author: jayke
"""
#entrando com as diemnsões
h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede ?'))
#calculando a área e a quantidade de tinta
A = h*l

Tinta = A/2
#exibindo o resultado e mensagem na tela
print('Sua parede tem a dimensão de {} X {} e sua área é {}m²'.format(h,l,A))
print('Vc vai precisar de {}L de tinta para pintar a parede.'.format(Tinta))
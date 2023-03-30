# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:40:42 2022

@author: jayke
"""
#entrando com o sal do funcionario
sal = float(input('Digite o valor do sal do funcionario: '))

#calculando o aumento com os 15% exigido
aumen = (sal*15)/100

#novo salario
nsal = sal+aumen

#dando print no novo sal
print('O novo salario do funcionario é R${:.2f} reais.'.format(nsal))
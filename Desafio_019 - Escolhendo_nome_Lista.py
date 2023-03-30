# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:24:14 2022

@author: jayke
"""
#importando a biblioteca random
from random import choice
#entrada de dados
a = str(input('Digite o 1° nome: '))
b = str(input('Digite o 2° nome: '))
c = str(input('Digite o 3° nome: '))
d = str(input('Digite o 4° nome: '))
#colocando os nomes na lista
lista = [a,b,c,d]
#usando o comando choice importado de random para fazer a escolha da lista
nome = choice(lista)
#saida de dados
print(nome)

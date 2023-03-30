# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:32:41 2022

@author: Jaykel JJ
"""

N = int(input("Entre com um valor numerico inteiro "))

horas = N//3600
rest_horas = N%3600

minutos = rest_horas//60
rest_minutos = rest_horas%60

segundos = rest_horas%60

print("{}:{}:{}" .format(horas,minutos,segundos))
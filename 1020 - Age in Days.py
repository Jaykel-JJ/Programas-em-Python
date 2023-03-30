# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:49:17 2022

@author: Jaykel JJ
"""

D = int(input())

anos = D//365
rest_anos = D%365

meses = rest_anos//30
rest_meses = rest_anos%30

dias = rest_meses

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:28:31 2022

@author: Jaykel JJ
"""

n = map(int, input().split())

X,Y = n
#CACHORRO QUENTE
if X==1:
    Total = 4.00*Y
    print("Total: R$ {:.2f}".format(Total))
#X-SALADA
if X==2:
    Total = 4.50*Y
    print("Total: R$ {:.2f}".format(Total))
#X-BACON
if X==3:
    Total = 5.00*Y
    print("Total: R$ {:.2f}".format(Total))
#TORRADA SIMPLES
if X==4:
    Total = 2.00*Y
    print("Total: R$ {:.2f}".format(Total))
#REFRIGERANTE
if X==5:
    Total = 1.50*Y
    print("Total: R$ {:.2f}".format(Total))
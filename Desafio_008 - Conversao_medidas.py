# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:19:02 2022

@author: jayke
"""

n = float(input('Digite o valor em metros para conversão: '))
#convertendo o valor em metros para as medidas
mm = n*1000
cm = n*100
dm = n*10
dam = n*0.1
hm = n*0.01
km = n*0.001

#exibindo o resultado na tela
print('A conversão de {} é\n {:.2f}mm\n {:.2f}cm\n {:.2f}dm\n {:.2f}dam\n {:.2f}hm\n {:.2f}km'.format(n,mm,cm,dm,dam,hm,km))

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:26:58 2022

@author: jayke
"""

c = d = 0
resp = 0
while resp!=2:
    a = float(input())
    if a>=0 and a<=10:
        d+=a
        c+=1
    else:
        print('nota invalida')
    if c==2:
        media = d/2
        print('media = {:.2f}'.format(media))
        d=0
        c=0
        resp = 0
        while True:
            resp = int(input('novo calculo (1-sim 2-nao)'))
            if resp==1 or resp==2:
                break
    if resp == 2:
        break

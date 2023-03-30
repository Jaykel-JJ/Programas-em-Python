# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:21:47 2022

@author: jayke
"""
c= d = 0
while True:
    if c==2:
        break
    a = float(input())
    if a>=0 and a<=10:
        d+=a
        c+=1
    else:
        print('nota invalida')
media = d/2
print('media = {:.2f}'.format(media))

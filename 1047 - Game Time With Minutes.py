# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:43:06 2022

@author: Jaykel JJ
"""

a,c,b,d=list(map(int,input().split()))

dif=((b*60)+d)-((a*60)+c)
if(dif<=0):
    dif+=24*60
    
time=dif//60
minute=dif%60
print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")
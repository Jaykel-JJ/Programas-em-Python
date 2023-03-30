# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:45:41 2022

@author: jayke
"""
GRENAIS = Inter = Gremio = Empate = 0
while True:
    I,G = list(map(int,input().split()))
    GRENAIS+=1
    if I>G:
        Inter+=1
    if I<G:
        Gremio+=1
    if I==G:
        Empate+=1
    t = 0
    while True:
        print('Novo grenal (1-sim 2-nao)')
        t = int(input())
        if t==1 or t==2:
            break
    if t == 2:
        break
print('{} grenais'.format(GRENAIS))
print('Inter:{}'.format(Inter))
print('Gremio:{}'.format(Gremio))
print('Empates:{}'.format(Empate))
if Inter>Gremio:
    print('Inter venceu mais')
else:
    print('Gremio venceu mais')

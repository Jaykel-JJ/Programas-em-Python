# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:23:56 2022

@author: Jaykel JJ
"""

resp_1 = str(input())
resp_2 = str(input())
resp_3 = str(input())

if resp_1=="vertebrado" and resp_2=="ave" and resp_3=="carnivoro":
    print("aguia")

elif resp_1=="vertebrado" and resp_2=="ave" and resp_3=="onivoro":
    print("pomba")
    
elif resp_1=="vertebrado" and resp_2=="mamifero" and resp_3=="onivoro":
    print("homem")
    
elif resp_1=="vertebrado" and resp_2=="mamifero" and resp_3=="herbivoro":
    print("vaca")
    
elif resp_1=="invertebrado" and resp_2=="inseto" and resp_3=="hematofago":
    print("pulga")

elif resp_1=="invertebrado" and resp_2=="inseto" and resp_3=="herbivoro":
    print("lagarta")
    
elif resp_1=="invertebrado" and resp_2=="anelideo" and resp_3=="hematofago":
    print("sanguessuga")

elif resp_1=="invertebrado" and resp_2=="anelideo" and resp_3=="onivoro":
    print("minhoca")
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:42:54 2022

@author: Jaykel JJ
"""
import math

n = map(float, input().split())
A,B,C = n

delta = float((B**2)-4*A*C)

if delta<0 or (A==0):
    print("Impossivel calcular")
else:
    R1 = (-B+math.sqrt(delta))/(2*A)
    R2 = (-B-math.sqrt(delta))/(2*A)
    print("R1 = {:.5f}".format(R1))
    print("R1 = {:.5f}".format(R2))

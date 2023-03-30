# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:26:25 2022

@author: Jaykel JJ
"""

A,B = map(int, input().split())

if A%B == 0 or B%A==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
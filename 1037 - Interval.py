# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:23:40 2022

@author: Jaykel JJ
"""

n = float(input())

if n<0 or n>100:
    print("Fora de intervalo ")
else:
    if n>=0 and n<=25:
        print("Intervalo [0,25]")
    else:
        if n>25 and n<=50:
            print("Intervalo (25,50]")
        else:
            if n>50 and n<=75:
                print("Intervalo (50,75]")
            else:
                if n>75 and n<=100:
                    print("Intervalo (75,100]")
                    
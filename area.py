# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:41:43 2022

@author: Jaykel JJ
"""

valors = input().split()
A,B,C = valors


rectangle_triangle = (float(A)*float(C)/2)
circle = 3.14159*(float(C)**2)
trapezium = ((float(A)+float(B))*float(C))/2
square = (float(B)*float(B))
rectangle = (float(A))*(float(B))

print("TRIANGULO: {:.3f}".format(rectangle_triangle))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trapezium))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rectangle))
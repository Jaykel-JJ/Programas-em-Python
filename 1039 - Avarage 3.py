# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:38:12 2022

@author: Jaykel JJ
"""

notas = map(float, input().split())
N1,N2,N3,N4 = notas

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print("Media: {:.1f}".format(media))

if media>=7.0:
    print("Aluno aprovado.")
if media<5.0:
    print("Aluno reprovado.")

if media>=5.0 and media<=6.9:
    print("Media: {:.1f}".format(media))
    print("Aluno em exame.")
    N5 = float(input())
    print("Nota do exame: {:.1f}".format(N5))
    nota_exame = (media+N5)/2
    if nota_exame>=5.0:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(nota_exame))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(nota_exame))
    
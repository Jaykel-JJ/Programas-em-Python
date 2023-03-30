# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:43:13 2022

@author: Jaykel JJ
"""
print("DIGITE ZERO PARA PARAR COM O PROGRAMA !")

i='sim'

while i=='sim':
    
    nota = int(input("Digite a nota do seu aluno: "))

    if nota>3 and nota<=5:
        print("Aluno em recuperação")

    if nota>5:
        print("Aluno Aprovado")
    else:
        print("Aluno reprovado")
    i = input("Deseja continuar?")
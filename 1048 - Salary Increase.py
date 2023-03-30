# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:06:48 2022

@author: Jaykel JJ
"""

salary = float(input())

if salary<=400.00:
    reajuste = salary*0.15
    novo_salary = reajuste + salary
    print("Novo salario: {:.2f}".format(novo_salary))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 15 %")

elif salary>=400.01 and salary <=800.00:
    reajuste = salary*0.12
    novo_salary = reajuste + salary
    print("Novo salario: {:.2f}".format(novo_salary))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 12 %")
    
elif salary>=800.01 and salary<=1200.00:
    reajuste = salary*0.10
    novo_salary = reajuste + salary
    print("Novo salario: {:.2f}".format(novo_salary))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 10 %")
    
elif salary>= 1200.01 and salary<=2000.00:
    reajuste = salary*0.07
    novo_salary = reajuste + salary
    print("Novo salario: {:.2f}".format(novo_salary))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 7 %")
    
elif salary>2000.00:
    reajuste = salary*0.04
    novo_salary = reajuste + salary
    print("Novo salario: {:.2f}".format(novo_salary))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 4 %")
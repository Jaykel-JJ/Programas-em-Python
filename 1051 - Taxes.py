# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:04:12 2022

@author: Jaykel JJ
"""

salary = float(input("type here you salary: "))

if salary > 0 and salary <= 2000:
    print("Isento")
    
elif salary>2000 and salary <=3000:
    resto = salary-2000
    tax = resto*0.08
    print("R$ {:.2f}".format(tax))

elif salary>3000 and salary <4500:
    resto = salary-3000
    tax = (resto*0.18)+(1000*0.08)
    print("R$ {:.2f}".format(tax))
    
else:
    resto = salary - 4500
    tax = (resto*0.28)+(1500*0.18)+(1000*0.08)
    print("R$ {:.2f}".format(tax))
    
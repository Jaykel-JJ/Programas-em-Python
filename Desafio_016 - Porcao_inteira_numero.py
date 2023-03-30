#importando a biblioteca para truncar 
from math import trunc

#entrando com o valor numerico
n = float(input('Digite um valor decimal: '))

#printando na tela o valor que precisa
print('O valor digitado foi {} e a sua porção inteiro é {}.'.format(n,trunc(n)))

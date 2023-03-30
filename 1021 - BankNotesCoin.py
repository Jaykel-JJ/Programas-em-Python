N=float(input("aq: "))

rest = N%100
inteira = N//100
    
n = rest
    
rest2 = n%50
inteira2 = n//50
    
n = rest2
    
rest3 = n%20
inteira3 = n//20
    
n = rest3
    
rest4 = n%10
inteira4 = n//10
    
n = rest4
    
rest5 = n%5
inteira5 = n//5
    
n = rest5
    
rest6 = n%2
inteira6 = n//2
    
n = rest6
    
rest7 = n%1
inteira7 = n//1

n = rest7

rest8 = n%0.5
inteira8 = n//0.5

n = rest8

rest9 = n%0.25
inteira9 = n//0.25

n = rest9

rest10 = n%0.10
inteira10 = n//0.10

n = rest10

rest11 = n%0.05
inteira11 = n//0.05

n = rest11

rest12 = n%0.01
inteira12 = n//0.01

    
print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00".format(inteira))
print("{:.0f} nota(s) de R$ 50.00".format(inteira2))
print("{:.0f} nota(s) de R$ 20.00".format(inteira3))
print("{:.0f} nota(s) de R$ 10.00".format(inteira4))
print("{:.0f} nota(s) de R$ 5.00".format(inteira5))
print("{:.0f} nota(s) de R$ 2.00".format(inteira6))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00".format(inteira7))
print("{:.0f} moeda(s) de R$ 0.50".format(inteira8))
print("{:.0f} moeda(s) de R$ 0.25".format(inteira9))
print("{:.0f} moeda(s) de R$ 0.10".format(inteira10))
print("{:.0f} moeda(s) de R$ 0.05".format(inteira11))
print("{:.0f} moeda(s) de R$ 0.01".format(inteira12))

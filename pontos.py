n=int(input("Digite o valor para o saque: "))

rest = n%100
inteira = n//100
    
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
    
print("{} nota(s) de R$ 100,00".format(inteira))
print("{} nota(s) de R$ 50,00".format(inteira2))
print("{} nota(s) de R$ 20,00".format(inteira3))
print("{} nota(s) de R$ 10,00".format(inteira4))
print("{} nota(s) de R$ 5,00".format(inteira5))
print("{} nota(s) de R$ 2,00".format(inteira6))
print("{} nota(s) de R$ 1,00".format(inteira7))
n=int(input())
resto1=n%3
resto2=n%5

if(resto1==0) and (resto2==0):
    print("FizzBuzz")
else:
    print(n)
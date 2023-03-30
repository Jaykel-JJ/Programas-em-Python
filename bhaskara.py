import math

a = float(input())
b = float(input())
c = float(input())

delta = (b**2)-(4*a*c)

if(delta<0):
    print("esta equação não possui raízes reais")
    
else:
    if(delta==0):
        X = (-b+math.sqrt(delta))/(2*a)
        Y = (-b-math.sqrt(delta))/(2*a)
        print("a raiz dupla desta equação é ", X)
        
if(delta>0):
                    X = (-b+math.sqrt(delta))/(2*a)
                    Y = (-b-math.sqrt(delta))/(2*a)
                    if(X>Y):
                        print("as raízes da equação são", Y, "e", X)
                    else:
                        print("as raízes da equação são", X, "e", Y)
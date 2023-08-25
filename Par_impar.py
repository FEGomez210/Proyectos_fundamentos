import math

def parimpar(c):
    y=c%2
    if (y==0):
        print("el numero es par")
    else:
        print("el numero es impar")
    
    return(y)        

x=float (input("ingrese un numero a evaluar:"))
print(parimpar(x))
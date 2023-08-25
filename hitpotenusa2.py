import math



#Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la
#hipotenusa

def hepi(a,b):
    x=((a**2)+(b**2))**(1/2)
    
    return(x)

def parimpar(c):
    y=c%2
    if (y==0):
        print("el numero es par")
    else:
        print("el numero es impar")
    
    return(y)        
            

h=3
j=4
print(hepi(h,j))

zamba= float (input("ingrese un numero a evaluar:"))
print(parimpar(zamba))
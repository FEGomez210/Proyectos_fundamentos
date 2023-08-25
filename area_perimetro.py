import math
x=math.pi

def area(a,b):
    ar=a*(b**2)
    return(ar)    

def perimetro(c,d,e):
    peri=c*d*e
    return(peri)

#Dado el número matemático PI, se solicita al usuario que ingrese el valor del radio de una
#circunferencia y calcule y muestre por pantalla el área y perímetro. (área = PI * radio2
#perímetro = 2 * PI * radio.
rest=(input("quiere ingresar a la calculadora? si/no  :"))
while rest=="si":
    radio= float (input("ingrese el radio de la circunferencia:"))
    y=area(x,radio)
    z=perimetro(2,x,radio)
    print("el area de la circunceria es de:", y)
    print("el peremietro de la circunferencia es de:", z)
    rest=(input("quiere seguir calculando?si/no  :"))
else:
    print("ha salido de la calculadora:")    
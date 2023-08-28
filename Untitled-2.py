#Escribir una función lógica vocal que determine si un carácter es una vocal.
import math

def vocal(x):
    if (x=="a") or (x=="e") or (x=="i") or (x=="o") or (x=="u"):
        y=print("es una vocal en español")
    else:
        y=print("no es una vocal en español, ingrese otro caracter")

voc=input("ingrese un caracter:")
while vocal(voc)==y:
    voc=input("ingrese otro caracter:")
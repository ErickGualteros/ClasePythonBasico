"""Primer trabajo en clase, Manejo de variables"""
A="hola mundo"
print(A)
B=" soy el primer programa de la clase"
print(B)
#concatenar variables
c=A+B
D=4*A
print('¿Que variables tenemos?', type(D))
#Variables str
E=5
print('Tipo de variable numerica', type(E))
#convertir variables:
str(E)
print('Tipo de variable numerica', type(E))
float(E)
print('Tipo de variable numerica', type(E))
import this 
#encadenado de variables 
nombre=input('¿Cual es tu nombre?\n')
print("hola " + nombre + B)
#primer condicional identificar un número mayor
a=int(input("Ingrese un valor: \n"))
b=int(input("Ingrese otro valor: \n"))
if a>b:
  print("El número mayor es ",a, "\n El número menor es ",b)
elif b>a:
  print("El número mayor es ",b, "\n El número menor es ",a)
else:
  print("Las dos variables son iguales")

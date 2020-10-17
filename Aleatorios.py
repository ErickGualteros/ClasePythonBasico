import random as rm #alias par aenontrar librerias
#from random import randrange, randint #otra forma de importar
a=rm.randrange(0,10)
print('EL NÚMERO SECRETO')
print("Adivina el número que esta pensando la maquina entre 0 y 10")
b=int(input('Ingresa el número: '))
if b>a:
  print("El número ingresado es mayor")
elif a>b:
  print("El número ingresado es Menor")
else:
  print("Son iguales: ")
  print("Felicidades, GAnaste")
print(a)
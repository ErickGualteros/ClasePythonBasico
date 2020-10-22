#Trabajo con funciones
def suma(a,b):
  return a+b
def resta (a,b):
  return a-b
def producto (a,b):
  return a*b
def cociente (a,b):
  return a/b
#función que no retorna el Valor
def incrementar(c):
  global a
  c+=a
  print('Resultado de la función incrementar',c)
#funcion si no se le pasa un valor:
def div2(a,b=3):
  return a/b
a=int(input('Ingrese el primer valor: '))
b=int(input('Ingrese el segundo valor: '))
r1=suma(a,b)
r2=resta(a,b)
r3=producto(a,b)
r4=cociente(a,b)
r5=div2(a)
print (r1)
print (r2)
print (r3)
print (r4)
incrementar(a)
print (r5)
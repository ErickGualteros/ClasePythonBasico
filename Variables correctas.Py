""" Ejemplos de nombres de variables validas y no validas"""
#comparacion de variables
Mivariable="Buen día"
MiVariable="Buen día"
Variable="Hola mundo"
variable="'Hola Mundo'"
print(Mivariable==Variable)
print(Mivariable==MiVariable)
print(variable)
#varias variables
x,y,z=10,20,12
print(x,y,z)
#otra forma de llamar
X='GENIAL'
def f():
  global z
  z=3 #la variable ahora es global
  print('Python es: '+X)
  y=2
  print(y,"Variable interna de la función")

f()
print(y, "Variable externa de la función")
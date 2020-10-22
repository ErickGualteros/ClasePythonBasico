"""Variables de control"""
x=int(input("ingrese un valor númerico: "))
print("Usted ingreso el valor :" + str(x))
if x % 2==0: #si es modulo de 2
  x=x/2
elif x %3==0: #si es modulo de 3
  x=x/3
elif x%4==0: #si es modulo de 4
  x=x/4
else: 
  x=x+1
print("Ahora el valor es :" + str(x))
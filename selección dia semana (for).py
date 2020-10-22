"""Programa para adivinar el día"""
dia=int(input("ingrese un Valor:"))
semana=["Lunes", "Martes","Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print("PRIMERA FORMA")
if dia <1 or dia >7:
  print ("Número no valido")
else:
  print(semana[dia-1])
  
print("SEGUNDA FORMA")
if dia==1:
  print ("Lunes")
elif dia==2:
  print("Martes")
elif dia==3:
  print("Miercoles")
elif dia==4:
  print("Jueves")
elif dia==5:
  print("Viernes")
elif dia==6:
  print("Sabado")
elif dia==7:
  print("Domingo")
else:
  print("Ingrese un valor correcto")
print("Todas las semanas")
for d in semana:
  print(d)


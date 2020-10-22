semana=["Lunes", "Martes","Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
while True:
  dia=int(input("ingrese un Valor para el día de la semana: "))
  if dia>=1 and dia <=7:
    break
print(semana[dia-1])
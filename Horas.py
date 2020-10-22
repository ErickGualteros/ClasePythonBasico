h=int(input('Ingrese el valor de las horas: '))
m=int(input('Ingrese el valor de los minutos: '))
s=int(input('Ingrese el valor de los segubdos : '))
lapso=int(input('Ingrese el valor en segundos: '))
segundos=h*3600+m*60+s+lapso
h=segundos//3600
segundos%=3600
m=segundos//60
segundos%=60
s=segundos
print('La nueva hora es: \n',h,'h',m,"'",s,"''")
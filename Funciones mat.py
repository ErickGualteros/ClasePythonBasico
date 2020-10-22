#potencia natural
def potencia(x,n):
  if n==0:
    return 1
  else:
    return x*potencia(x,n-1)
print(potencia(5,20))
#factorial
def factorial(a):
  if a==1:
    return 1
  elif a==0:
    return 1
  else:
    return a*factorial(a-1)
print(factorial(20))
#factorial iteratico
def fact(a):
  acumulador=1
  contador=a
  for n in range(a):
    acumulador*=contador
    contador -=1
  return acumulador
print(fact(20))
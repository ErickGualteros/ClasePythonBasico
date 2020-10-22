#Colección
pintas=['Picas','brevoles','Diamantes','Corazones']
valores=['A','J','Q','K']
mazo=[(v,p) for v in valores for p in pintas]
for carta in mazo:
  print(carta)
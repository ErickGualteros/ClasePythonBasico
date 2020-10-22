#Colección
pintas=['Picas','Treboles','Diamantes','Corazones']
valores=['A','J','Q','K','2','3','4','5','6','7','8','9']
mazo=[(v,p) for v in valores for p in pintas]
for a in range(0,len(mazo),5):
  print(mazo[a])
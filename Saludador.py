def saludo(nombre):
  print ('Hola '+nombre)
saludo('Erick')
def salinvitados(invitados):
  for n in invitados:
    saludo(n)
inv=['Erick','Alejo','Deya','Todos']
salinvitados(inv)

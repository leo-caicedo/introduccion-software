#programa de votos para saber si paso el umbral para asignar curules

VotosValidos = int(input("Ingrese votos validos: "))
VotosPartido = int(input("Ingrese votos por su partido: "))

Umbral = VotosValidos * 0.03

if(VotosPartido > Umbral):

  print("Tu partido tendrá curules")
else:

  print("Se quemaron")


#Realice un programa que indique segun el año que naciste la
#generación a la que perteneces

año= int(input("Ingrese el año en que naciste: "))

if(año >= 1994 and año <= 2010):
  print("Eres generación Z ")
elif(año >= 1981 and año <= 1993):
    print("Eres milenial")
else:
  print("Eres de otra generación")


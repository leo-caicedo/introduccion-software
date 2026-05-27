matematicas = float(input("Ingrese la nota de matemáticas: "))
castellano = float(input("Ingrese la nota de castellano: "))
ingles = float(input("Ingrese la nota de inglés: "))
sociales = float(input("Ingrese la nota de sociales: "))

promedio = (matematicas + castellano + ingles + sociales) / 4

print("El promedio es:", promedio)

if promedio > 4.5:
    print("Puedes acceder a la beca")
else:
    print("Aún no puedes acceder a la beca, intenta el otro semestre")

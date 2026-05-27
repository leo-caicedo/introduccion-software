# condicionales
# Construir un código que permita ingresar
# un número, si el número es mayor de 500, se debe
# calcular y mostrar en pantalla el 18% de este.

numero = int(input('Ingrese un número: '))
if numero > 500:
    porcentaje = numero * 0.18
    print("El 18% de este número es", porcentaje)
else:
    print("Ingrese otro número")
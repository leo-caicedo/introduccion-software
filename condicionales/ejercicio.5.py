#En una oficina de empleos categorizan a los postulantes en función del sexo y de la edad
#de acuerdo con lo siguiente:Si la persona es de sexo femenino:
#categoria FA si tiene menos de 23 años y FB, en caso contrario.
#Si la persona es de sexo masculino: categoria MA si tiene menos de 25 años y MB,
#en caso contrario.Dado el sexo y la edad de un postulante,
#diseñe un programa que determine su categoría.

Genero = str(input("Ingrese su genero (F para femenino, M para masculino): ")).upper()
Edad = int(input("Ingrese su edad: "))

if Genero == "F":
    if Edad < 23:
        Categoria = "FA"
    else:
        Categoria = "FB"

elif Genero == "M":
    if Edad < 25:
        Categoria = "MA"
    else:
        Categoria = "MB"

else:
    print ("Genero no valido")

print(f"Su categoria es: {Categoria}")

print("Fin del programa")

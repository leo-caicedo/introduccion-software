sexo = input("Ingrese el sexo del postulante: ")
edad = int(input("Ingrese la edad del postulante: "))

if sexo.lower() == "femenino":
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
else:
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"

print("La categoría del postulante es:", categoria)

#Generos musicales


genero= str(input("Ingrese genero: ")).lower
if genero == "electronica" or genero == "pop":
    anio = int(input("Ingrese el año: "))
    if anio > 2000 and genero == "pop":
        print("Tengo la camisa negra")
    else:
        print("Por siempre Daft Punk")
else:
    print("Los únicos géneros buenos son Electrónica y Pop")

print("Fin programa")
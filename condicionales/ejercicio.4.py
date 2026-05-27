#Crear un sistema que permita al usuario cambiar su divisa de Soles a
#Euros o Dólares según sus necesidades, este pide el nombre,
#el monto y selecciona la moneda a la que desea cambiarlo

nombre = input("Ingrese el nombre del cliente: ")
monto = float(input("Ingrese el monto a cambiar en soles: "))

moneda = 0

while moneda >=3 or moneda <=0:
    print("Seleccione moneda de cambio")
    print("(1)Dólares")
    print("(2)Euros")
    moneda = int(input("Ingrese opcion: "))

if moneda == 1:
    cambio= monto / 2.35
    simbolo= "Dólares"
elif moneda == 2:
    cambio= monto / 3.58
    simbolo= "Euros"
else:
    print("El valor ingresado no es valido, por favor introduzca una opcion valida")

print(f"Se cambio en {simbolo}: {cambio}")
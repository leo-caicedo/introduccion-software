nombre = input("Ingrese el nombre del cliente: ")
monto = float(input("Ingrese el monto a cambiar en soles: "))

print("Seleccione moneda de cambio:")
print("[1] Dólares")
print("[2] Euros")
moneda = int(input("Opción: "))

if moneda == 1:
    cambio = monto / 2.35
    simbolo = "$"
elif moneda == 2:
    cambio = monto / 3.58
    simbolo = "€"
else:
    cambio = 0
    simbolo = ""

print("Se cambió en", simbolo, cambio)

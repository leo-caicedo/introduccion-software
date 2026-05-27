p = float(input("Ingrese el precio de la entrada: "))
edad = int(input("Ingrese la edad del cliente: "))

monto_final = p
if edad < 10:
    monto_final = p - (p * 0.25)

print("El monto final a pagar es:", monto_final)

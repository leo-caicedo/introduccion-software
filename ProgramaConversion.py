# Crear un programa que permita convertir dinero de soles
# a dólares o euros, según la opción elegida por el usuario.

nombre = str(input('Ingrese el nombre del cliente: '))
monto = float(input('Ingrese el monto a cambiar en soles: '))

moneda = int(
    input(
        'Seleccione la moneda de cambio.\n'
        '[1] Dólares [2] Euros\n'
    )
)

if moneda == 1:
    cambio = monto / 2.35
    simbolo = '$'

else:
    cambio = monto / 3.58
    simbolo = '€'

print(f'Se cambió en {simbolo} {cambio}')
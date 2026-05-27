# Flores
# Crear un programa que calcule el valor a pagar
# según la cantidad de flores compradas.

cantidadFlores = int(
    input('Ingrese la cantidad de flores: ')
)  # Cantidad de flores ingresada por el usuario.

# Evaluar el precio dependiendo de la cantidad de flores.
if cantidadFlores >= 10:

    precioTotal = cantidadFlores * 8

    print(f'Total a pagar: {str(precioTotal)}')

elif cantidadFlores >= 5:

    precioTotal = cantidadFlores * 10

    print(f'Total a pagar: {str(precioTotal)}')

elif cantidadFlores == 3:

    print('No debes pagar nada, las flores son gratis.')

else:

    precioTotal = cantidadFlores * 15

    print(f'Total a pagar: {str(precioTotal)}')

print("Fin programa")
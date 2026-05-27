# Temperatura
# Crear un programa que solicite la temperatura al usuario.
#
# - Si la temperatura es mayor a 27 grados,
#   mostrar el mensaje: "Comprar helado".
#
# - Si la temperatura es menor a 15 grados,
#   mostrar el mensaje: "Comprar chocolate".
#
# - En cualquier otro caso,
#   mostrar el mensaje: "Comprar jugo de naranja".
#
# Al finalizar, el programa debe imprimir:
# "Fin programa".

temperatura = float(input('Ingrese la temperatura: '))

if temperatura > 27:
    print('Comprar helado.')

elif temperatura < 15:
    print('Comprar chocolate.')

else:
    print('Comprar jugo de naranja.')

print('Fin programa.')
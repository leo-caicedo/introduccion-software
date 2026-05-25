# Ejercicio For - Ciclos - Bucles.
# Mostrar la tabla de multiplicar de un número.

# Solicitar el número al usuario.
N = int(input('Ingrese un número: '))

# Recorrer los números del 1 al 9.
for vc in range(1, 10):

    # Multiplicar el número ingresado.
    resultado = vc * N

    # Mostrar el resultado de la multiplicación.
    print(f'{N} x {vc} = {resultado}')
    
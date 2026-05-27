# Ejercicio For - Ciclos - Bucles.
# Mostrar las primeras N potencias de 2.

# Solicitar la cantidad de potencias.
N = int(input('Ingrese la potencia: '))

# Definir la base.
base = 2

# Variable para almacenar el resultado.
resultado = 1

# Recorrer desde 1 hasta N.
for i in range(1, N + 1):

    # Multiplicar el resultado por la base.
    resultado *= base

    # Mostrar cada potencia obtenida.
    print(resultado)
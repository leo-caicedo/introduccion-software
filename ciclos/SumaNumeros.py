# Ejercicio While - Ciclos - Bucles.
# Crear un programa que muestre los números desde 1 hasta N
# y al final calcule la suma total de esos números.

# Solicitar al usuario un número entero.
n = int(input('Ingrese un número entero: '))

# Variable contador que iniciará desde 1.
vc = 1

# Variable acumuladora para guardar la suma de los números.
suma = 0

# Ciclo while que se ejecutará mientras el contador
# sea menor o igual al número ingresado.
while vc <= n:

    # Mostrar el número actual del contador.
    print(f'Cuenta: {vc}')

    # Acumular el valor actual en la variable suma.
    suma += vc

    # Incrementar el contador en 1
    # para continuar con el siguiente número.
    vc += 1

# Mostrar el resultado final de la suma.
print(f'La suma de 1 hasta {n} es {suma}')
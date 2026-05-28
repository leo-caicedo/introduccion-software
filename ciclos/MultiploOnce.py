# Ejercicio propuesto en clase.
# Crear un programa que solicite números enteros
# hasta que el usuario ingrese un número múltiplo de 11.

# Solicitar el primer número al usuario.
number = int(input('Ingrese un número: '))

# Ciclo que se repetirá mientras el número
# no sea múltiplo de 11.
while number % 11 != 0:

    # Mostrar mensaje indicando que el número
    # ingresado no cumple la condición.
    print(f'El número {number} no es múltiplo de 11')

    # Solicitar nuevamente otro número.
    number = int(input('Ingrese un número: '))

# Mensaje final cuando el número sí es múltiplo de 11.
print(f'\nEl número {number} es múltiplo de 11')
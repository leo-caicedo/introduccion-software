# Ejercicio While - Ciclos - Bucles.
# Pedir números hasta que el usuario ingrese 0.
# Mostrar si cada número es par o impar.

# Solicitar el primer número.
num = int(input('Ingrese un número: '))

# Repetir mientras el número sea diferente de 0.
while num != 0:

    # Verificar si el número es par.
    if num % 2 == 0:
        print(f'El número {num} es par.')
    
    # Si no es par, es impar.
    else:
        print(f'El número {num} es impar.')

    # Solicitar otro número.
    num = int(input('Ingrese un número: '))

# Mostrar mensaje final.
print(f'El número ingresado es {num}.')
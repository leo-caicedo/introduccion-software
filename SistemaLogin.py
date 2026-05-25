# Sistema de Login

# Credenciales correctas.
usuario_correcto = 'admin'
contrasena_correcta = '123'

# Variable para controlar el menú.
opcion = 0

# Ciclo principal del programa.
while opcion != 2:

    # Mostrar menú.
    print('\n===== LOGIN ADMINISTRATIVO =====')
    print('1. Ingresar credenciales')
    print('2. Salir')

    # Solicitar opción.
    opcion = int(input('Seleccione una opción: '))

    # Validar opción 1.
    if opcion == 1:

        # Pedir usuario y contraseña.
        usuario = input('Ingrese el usuario: ')
        contrasena = input('Ingrese la contraseña: ')

        # Validar credenciales.
        if usuario == usuario_correcto and contrasena == contrasena_correcta:

            print('Inicio de sesión válido.')

        else:

            print('Credenciales incorrectas.')

    # Validar opción 2.
    elif opcion == 2:

        print('Has salido del sistema.')

    # Mensaje si la opción no existe.
    else:

        print('La opción ingresada no es válida.')
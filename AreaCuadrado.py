# Área de un cuadrado
# Crear un programa que calcule el área de un cuadrado.

ladoCuadrado = float(
    input("Ingrese el lado del cuadrado: ")
)  # Solicitar el valor del lado.

# Verificar que el lado sea mayor que 0.
if ladoCuadrado > 0:

    areaCuadrado = ladoCuadrado * ladoCuadrado

    print(f'El área del cuadrado es de {areaCuadrado}.')

# Mensaje en caso de que el valor ingresado sea inválido.
else:
    print('El lado del cuadrado no puede ser menor o igual a 0')
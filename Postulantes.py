# En una oficina de empleos se clasifican los postulantes
# según su sexo y edad, de acuerdo con las siguientes reglas:
#
# - Si la persona es de sexo femenino:
#   * Categoría FA si tiene menos de 23 años.
#   * Categoría FB en caso contrario.
#
# - Si la persona es de sexo masculino:
#   * Categoría MA si tiene menos de 25 años.
#   * Categoría MB en caso contrario.
#
# Diseñar un programa que determine la categoría del postulante.

sexo = str(
    input('Ingrese el sexo del postulante (Masculino o Femenino): ')
).lower()

while sexo != "femenino" and sexo != "masculino":
    print('Sexo inválido, ingrese "Femenino" o "Masculino"')

    sexo = str(
        input('Ingrese el sexo del postulante (Masculino o Femenino): ')
    ).lower()

edad = int(input('Ingrese la edad del postulante: '))

if sexo == 'femenino':

    if edad < 23:
        categoria = 'FA'
    else:
        categoria = 'FB'

elif sexo == 'masculino':

    if edad < 25:
        categoria = 'MA'
    else:
        categoria = 'MB'

print(f'La categoría del postulante es {categoria}')
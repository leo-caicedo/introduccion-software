# Crear un programa que identifique a qué generación pertenece una persona
# según el año de nacimiento ingresado.

# El programa debe solicitar el año de nacimiento.
#
# - Si el año está entre 1994 y 2010,
#   mostrará: "Eres Generación Z".
#
# - Si el año está entre 1981 y 1993,
#   mostrará: "Eres Millennial".
#
# - En cualquier otro caso,
#   mostrará: "Eres de otra generación".

year = int(input('Ingresa el año en que naciste: '))

if year >= 1994 and year <= 2010:

    print('Eres generación Z.')

elif year >= 1981 and year <= 1993:

    print('Eres Millennial.')

else:

    print('Eres de otra generación.')
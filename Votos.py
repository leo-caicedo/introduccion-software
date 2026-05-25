# Votos
# Crear un programa que valide si un partido político
# superó el umbral necesario para obtener curules.

# El programa debe solicitar:
# - La cantidad de votos válidos.
# - La cantidad de votos obtenidos por el partido.
#
# Luego, debe verificar si los votos del partido
# son mayores al 3% de los votos válidos.
#
# Si cumple la condición, se mostrará:
# "Tu partido tendrá curules".
#
# En caso contrario, se mostrará:
# "Se quemaron".

votos_validos = int(input('Ingrese la cantidad de votos válidos: '))
votos_partido = int(input('Ingrese la cantidad de votos de su partido: '))

umbral = votos_validos * 0.03

if votos_partido > umbral:
    print('Tu partido tendrá curules.')

else:
    print('Se quemaron.')
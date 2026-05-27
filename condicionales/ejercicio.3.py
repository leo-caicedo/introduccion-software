Nombre_del_trabajador = input('Ingrese el nombre del trabajador: ')
Sueldo_basico = float(input('Ingrese el sueldo básico: '))
Numero_de_hijos = int(input('Ingrese el número de hijos: '))

Bonificacion = 0

if Numero_de_hijos > 0:
    Bonificacion = 0.7

Sueldo_final = Sueldo_basico + Bonificacion

print("Nombre_del_trabajador", Nombre_del_trabajador)
print("Sueldo_basico", Sueldo_basico)
print("Numero_de_hijos", Numero_de_hijos)
print("Bonificacion", Bonificacion)
print("Sueldo_final", Sueldo_final)
nombre = input("Ingrese el nombre del trabajador: ")
basico = float(input("Ingrese el sueldo básico: "))
hijos = int(input("Ingrese el número de hijos: "))

Bonificacion_ = 0
if hijos > 0:
    Bonificacion_ = basico * 0.07

sueldo_final = basico + Bonificacion_

print("La Bonificación es:", Bonificacion_)
print("El sueldo final es:", sueldo_final)

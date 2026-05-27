capital = int(input("Ingrese el monto a invertir: "))
dias = int(input("Ingrese el número total de días del mes a considerar: "))

interes = 0.02
ganancia = (capital * dias) * interes

print("La ganancia por cobrar después del mes es de:", ganancia)

KmRecorrido = float(input("Ingrese el total de Km recorridos: "))
precio = float(input("Ingrese el precio de la gasolina (por litro): "))
dinero = float(input("Ingrese el dinero gastado en el viaje: "))
Horas = float(input("Ingrese el tiempo de Horas del viaje: "))
minutos = float(input("Ingrese el tiempo adicional de minutos: "))

consumoGasoTotal = dinero / precio
consumoGasoKm = consumoGasoTotal / KmRecorrido
consumoGaso100Km = consumoGasoKm * 100

precioGasoKm = consumoGasoKm * precio
precioGaso100Km = precioGasoKm * 100

velKmHora = KmRecorrido / (Horas + (minutos / 60))
velMetrSeg = (KmRecorrido * 1000) / ((Horas * 3600) + (minutos * 60))

print("El consumo de gasolina en litros por 100 kilometros es:", consumoGaso100Km)
print("El consumo de gasolina en litros por kilometros es:", consumoGasoKm)
print("El consumo de gasolina en euros por kilometro es:", precioGasoKm)
print("La velocidad media de km/hora es:", velKmHora)
print("La velocidad media de metros/seg es:", velMetrSeg)

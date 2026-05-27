#La entrada a un circo vale p soles por persona,
#sin embargo, si la edad de la persona es menor
#de 10 años se le da un descuento del 25% en el
#valor del boleto. Escribir el seudocódigo que
#calcule y muestre lo que pagará por la entrada
#al circo según la edad.

precio = float(input('Ingrese el precio de la entrada: '))
edad = int(input('Ingrese la edad: '))

if edad < 10:
    precio = precio - (precio * 0.25)

print('El precio a pagar es: ', precio)
#Ejercicio para el lado de un cuadrado

LadoCuadrado = float(input("Ingrese el lado del cuadrado: "))
3
if(LadoCuadrado > 0):
  AreaCuadrado = LadoCuadrado * LadoCuadrado
  print("El área es: " + str(AreaCuadrado))

else:
  print(("Lado no puede ser menor o igual a cero"))
  print("Fin Programa")
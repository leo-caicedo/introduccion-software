//promedio de 4 materias.
//imprime el promedio en pantalla
//y muestra un mensaje diferente si el promedio es mayor o menor que 4.5
Algoritmo NotasMaterias 
	Imprimir ("ingrese la nota de matematicas:");
	Leer matematicas;
	Imprimir ("ingrese la nota de castellano:");
	Leer castellano;
	Imprimir ("ingrese la nota de ingles:");
	leer ingles;
	imprimir ("ingrese la nota de sociales:");
	Leer sociales;
	promedio <- (matematicas+castellano+ingles+sociales)/4
	Imprimir (promedio);
	si(promedio > 4.5) Entonces
		Imprimir ("puedes acceder a la beca");
	SiNo
		Imprimir ("aún no puedes acceder a la beca , intenta el otro semestre");
		
	FinSi
	
	
FinAlgoritmo

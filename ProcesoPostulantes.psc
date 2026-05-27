Algoritmo ProcesoPostulantes
	//En una oficina de empleos categorizan a los postulantes en
	//función del sexo y de la edad de acuerdo con lo siguiente:
	//- Si la persona es de sexo femenino: categoría FA si tiene menos
	//de 23 años y FB, en caso contrario.
	//- Si la persona es de sexo masculino: categoría MA si tiene
	//menos de 25 años y MB, en caso contrario.
	//Dado el sexo y la edad de un postulante, diseñe un programa
	//que determine su categoría.
	
	Definir sexo como Cadena
	Definir edad Como Entero
	Definir categoria como cadena
	
	Escribir "Ingrese el sexo del postulante ";
	Leer sexo;
	Escribir"ingrese la edad del pstulante ";
	leer edad;
	
	//Proceso 
	si sexo = "Femenino" Entonces
		si edad < 23 Entonces
			categoria <- "FA"
		siNo
			categoria <-"FB"
			
		FinSi
	SiNo
		si edad < 25 Entonces 
			categoria <- "MA";
		SiNo
			categoria <- "MB";
		FinSi
		
	FinSi
	
	Escribir "La categoria del postulante es :",categoria;
	
	
FinAlgoritmo

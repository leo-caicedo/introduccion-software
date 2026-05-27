Algoritmo Bonificación
	//Elaborar un algoritmo que permita ingresar el
	//nombre del trabajador, su sueldo básico y el
	//número de hijos, se deberá mostrar su
	//bonificación y el sueldo final. Tenga en cuenta
	//que la empresa está dando una bonificación
	//del 7% del sueldo básico sólo en el caso el
	//trabajador tuviese hijos
	
	Definir nombre como Cadena ;
	Definir basico Como Real;
	Definir hijos Como Entero;
	Definir Bonificacion_,sueldo_final como Real;
	
	Escribir "Ingrese el nombre del trabajador";
	Leer nombre;
	Escribir"Ingrese el sueldo basico";
	leer basico;
	Escribir "Ingrese el numero de hijo";
	Leer hijos;
	
	Bonificacion_ <- 0;
	Si hijos > 0 Entonces
		Bonificacion_ <- basico * 0.07
		
		
	FinSi
	sueldo_final <- basico + Bonificacion_;
	
	Escribir "La Bonificacion es :",Bonificacion_;
	Escribir "El sueldo_final es :",sueldo_final;
	
	
	
FinAlgoritmo

Algoritmo EntradaCirco
	//La entrada a un circo vale p soles por persona,
	//sin embargo, si la edad de la persona es menor
	//de 10 años se le da un descuento del 25% en el
	//valor del boleto. Escribir el seudocódigo que
	//calcule y muestre lo que pagará por la entrada
	//al circo según la edad.
	
	//Declaracion de Variables
	Definir p Como Real;
	Definir edad como Entero;
	
	//Entrada
	Escribir "Ingrese el precio de la entrada ";
	Leer p ;
	Escribir "Ingrese la edad del cliente";
	Leer edad;
	
	//Proceso 
	monto_final <- p
	si edad <= 10 Entonces;
		monto_final <- (monto_final * 0.25);
		
		
	FinSi
	Escribir "El monto final a pagar es ",monto_final;
	
	
FinAlgoritmo

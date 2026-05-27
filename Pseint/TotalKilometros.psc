Algoritmo Total_Kilometros
	//Diseñar el algoritmo pseudocódigo correspondiente
	//a un programa que pida el total de kilómetros
	//recorridos, el precio de la gasolina (por litro),
	//el dinero de gasolina gastado en el viaje y el
	//tiempo que se ha tardado (en horas y minutos)
	//y que calcule:
	//? Consumo de gasolina (en litros y euros) por cada 100 km.
	//? Consumo de gasolina (en litros y euros)
	Definir KmRecorrido Como Real;
	Definir precio,dinero Como Real;
	Definir Horas, minutos Como Real;
	Definir consumoGasoTotal Como Real;
	Definir consumoGasoKm, consumoGaso100Km como Real;
	Definir precioGasoKm, precioGaso100Km como Real;
	Definir velKmHora, velMetrSeg como Real;
	
	Escribir "Ingrese el total de Km recorridos"
	Leer KmRecorrido;
	Escribir "Ingrese el precio de la gasolina (por litro)";
	Leer precio;
	Escribir "Ingrese el dinero gasatdo en el viaje";
	leer dinero;
	Escribir "Ingrese el tiempo de Horas del viaje"
	Leer Horas;
	ESCRIBIR"Ingrese el tiempo adicional de minutos ";
	Leer minutos;
	
	consumoGasoTotal <- dineo/precio//Total en litros 
	consumoGasoKm <- consumoGasoTotal/KmRecorrido//litros por kilometros
	consumoGaso100Km <- consumoGasoKm * 100;
	
		precioGasoKm <- consumoGasoKm * precio//gastos en Euros por Kilometro 
		precioGaso100Km <- precioGasoKm * 100;
		
     velKmHora <- KmRecorrido/(horas+(minutos/60));
     velMetrSeg <-(KmRecorrido * 1000)/((horas * 3600)+(minutos*60));
	 
	 Escribir "El consumo de gasolina en litros por 100 kilometros es :",consumoGaso100Km;
	  
	 Escribir "El consumo de gasolina en litros por kilometros es:",consumoGasoKm;
	  
	 Escribir "El consumo de gasolina en euros por kilometro es :",precioGasoKm;
	  
	 Escribir "la velocidad media de km/Hora es :",velKmHora;
	  
	 Escribir "la velocidad media de metros/seg es:",velMetrSeg;
	  
	
	
	FinAlgoritmo

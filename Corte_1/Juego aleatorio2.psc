Algoritmo random1
	//Programa que genera aleatoriamente un numero egntre menos cien a cien
	//Y Muestre si el jugador es ganador en las siquientes circunstancias:
	//Si n1 es positivo y par o negativo e impar
	//Si n1 es negativo y par muestra empate
	//En las demas premisas: NO APLICA

	Definir n1 Como Entero
	n1<-Aleatorio(-100,100)
	Escribir "El numero generado es: ",n1
	//Valido si es PAR o IMPAR

	//Valido reglas del juego
	Si n1 > 0 y n1 mod 2 = 0 o n1 < 0 y n1 mod 2 <> 0 Entonces 
		Escribir "::: GANADOR :::"
	SiNo
		
		Si n1 < 0 y n1 mod 2 =0 Entonces
			Escribir "::: EMPATE :::"
		
		SiNo
			Escribir "::: NO APLICA :::"
		FinSi
		
	FinSi
FinAlgoritmo

Algoritmo numeropar
	//Programa que reciba un numero y me muestre un mensaje de ganador, si el numero es par y positivo
	Definir num Como Entero
	
	Escribir "Ingrese el numero: "
	Leer num
	
	Si(num Mod 2 = 0) y (num > 0) entonces
		Escribir "Ganador"
	SiNo
		Escribir "Perdedor"
	Fin Si
FinAlgoritmo

	
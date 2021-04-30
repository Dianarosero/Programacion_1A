Algoritmo numeropar
	//Programa que reciba un numero y me muestre un mensaje de ganador,
	//si el numero esta ente uno Y diez Y es impar,o esta entre 20 y 30 y es par
	Definir num Como Entero
	
	Escribir "Ingrese el numero: "
	Leer num

	Si(num >= 1) y (num <= 10) y (num mod 2<>0) o (num >= 20) y (num <= 30) y (num mod 2 = 0)  entonces
		Escribir "Ganador"
	SiNo
		Escribir "Perdedor"
	Fin Si
FinAlgoritmo
Algoritmo random1
	//Programa que genera aleatoriamente un numero de cero a cien
	//Muestra por pantalla si es par o impar,y si es negativo o positivo
	Definir n1 Como Entero
	n1<-Aleatorio(-100,100)
	Escribir "El numero generado es: ",n1
	//Valido si es PAR o IMPAR
	Si n1 mod 2 = 0 Entonces
		Escribir "El numero es PAR"
	SiNo
		Escribir "El numero es IMPAR"
	FinSi
	//Valido si es POSITIVO o NEGATIVO
	Si n1 > 0 Entonces
		Escribir "El numero es POSITIVO"
	SiNo
		Si n1 < 0 Entonces
			Escribir "El numero es NEGATIVO"
		FinSi
		si n1=0 Entonces
			Escribir "El numero es CERO"
		FinSi
	FinSi
FinAlgoritmo

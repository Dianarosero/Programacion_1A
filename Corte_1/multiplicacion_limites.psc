Algoritmo multiplicar_con_limites
	Definir num1,num2,num3,contador Como Entero
	Escribir "Ingrese numero de la tabla:"
	leer num1
	Escribir "Ingrese serie limite inferior:"
	leer num2
	Escribir "Ingrese serie limite superior:"
	leer num3
	
	Para contador<-num2 Hasta num3 Con Paso 1 Hacer
		Escribir num1,"x",contador,"=",num1*contador
	Fin Para
	
FinAlgoritmo

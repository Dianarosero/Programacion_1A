Algoritmo multiplicion_basica
	Definir num,contador Como Entero
	Escribir "Ingrese numero de la tabla:"
	leer num
	
	Para contador<-1 Hasta 10 Con Paso 1 Hacer
		Escribir num,"x",contador,"=",num*contador
	Fin Para
	
	contador<-1
	//Mientras contador<=10 Hacer
	//	Escribir num,"x",contador,"=",num*contador
	//	contador<-contador+1
	//Fin Mientras
	
	Hacer
		contador<-contador+1
		Escribir num,"x",contador,"=",num*contador
	Hasta Que contador=10
FinAlgoritmo

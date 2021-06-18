Algoritmo dados2
	Definir dado1,dado2,contador Como Entero
	contador<-1
	Hacer
		dado1<-Aleatorio(1,6)
		dado2<-Aleatorio(1,6)
		
		Escribir dado1
		Escribir dado2
		Escribir "-------"
		contador<-contador+1
	Hasta Que contador>=30 o dado1=1 y dado2=1
	Si dado1=1 y dado2=1 Entonces
		Escribir "GANADOR"
	SiNo
		Escribir "PERDEDOR"
	FinSi
	Escribir contador

	

	
FinAlgoritmo



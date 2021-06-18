Algoritmo par_unos
	//Declaracion de variables
	Definir dado1,dado2,tot_tiros,tot_pares,sum_total Como Entero
	Definir estado_juego Como Logico
	Definir espera_tecla Como Caracter
	//Inicializacion de variables
	dado1<-0
	dado2<-0
	tot_tiros<-0
	tot_pares<-0
	sum_total<-0
	estado_juego<-Verdadero
	//Entradas-Procesos
	Mientras estado_juego Hacer
		dado1<-Aleatorio(1,6)
		dado2<-Aleatorio(1,6)
		Escribir "Dado 1: ",dado1
		Escribir "Dado 2: ",dado2
		//Contador de tiros
		tot_tiros=tot_tiros+1
		//Acumulador de valores
		sum_total=sum_total+(dado1+dado2)
		Si (dado1=1 y dado2=1 y tot_tiros<=30) Entonces
			estado_juego<-Falso
			Escribir ":::GANASTE:::"
			Escribir ":::Presione una tecla para ver el reporte final:::"
		FinSi
		
		Si (dado1<>1 y dado2<>1 y tot_tiros=30) Entonces
			estado_juego<-Falso
			Escribir ":::PERDISTE:::"
			Escribir ":::Presione una tecla para ver el reporte final:::"		
		FinSi
		
		Si dado1 == dado2 Entonces
			//Contador de parejas generadas
			tot_pares = tot_pares + 1
		FinSi
		
		Si (dado1<>1 y dado2<>1 y tot_tiros<30) Entonces
			Escribir ":::Presione una tecla para lanzar los dados nuevamente:::"
		FinSi
		
		Leer espera_tecla
	FinMientras
	
	//Mostrar reporte
	Escribir "Total tiros generados: ", tot_tiros
	Escribir "Total parejas generadas: ", tot_pares
	Escribir "Suma total valores de los dados generados: ", sum_total
	
FinAlgoritmo

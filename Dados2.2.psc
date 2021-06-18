Algoritmo Ciclo_white_dados2
	//Cree un Pseudocodigo o un Script: Debe permitir lanzar los dados N veces.
	//Terminara unicamente cuando el jugador obtenga un par de unos (GANADOR) 
	// O Si despues de 20 lanzamientos NO HA OBTENIDO el PAR DE UNOS REQUERIDO ( PERDEDOR ) 
	//Al finalizar el juego ,se debe visualizar por pantalla , el siguiente reporte:
	//->TOTAL DE TIROS GENERADOS
	//->TOTAL DE PARES GENERADOS INCLUYENDO EL PAR DE UNOS GANADOR (SI LO HAY)
	//->SUMA TOTAL DEL VALOR DE LOS DATOS GENERADOS
	Definir dado1, dado2, op, contador,acumulador,numpar Como Entero
	//####################################################
	op = 9
	contador=1 
	acumulador=0
	numpar=0
	//###################################################
	Mientras (op <> 0) y (contador<=20) Hacer
		dado1<-Aleatorio(1,6)
		dado2<-Aleatorio(1,6)
		Escribir "DADO 1 : " (dado1)
		Escribir "DADO 2 : " (dado2)
		Si dado1=dado2 Entonces
			numpar=numpar+1
			Escribir " VA " numpar " PAR" " o " " PARES "
		FinSi
		//#######################################################
		Si (dado1==1) y  (dado2==1) y (contador<=20) Entonces
			Escribir "GANADOOOOR!! "
			Escribir "TOTAL DE TIROS DE DADOS GENERADOS : " contador
			Escribir "TOTAL DE LA SUMA DEL VALOR DE LOS DATOS GENERADOS : " (acumulador)+(dado1)+(dado2)
			Escribir "TOTAL DE PARES OBTENIDOS : " numpar 
			op=0
			//####################################################
		SiNo
			Escribir "OPCIONES:"
			Escribir "Digite 1 para tirar dados de nuevo"
			Escribir "Digite 0 para salir del juego"
			Escribir " ::::VA " contador " intentos::: "
			op=0
			contador=contador+1
			acumulador=acumulador+(dado1+dado2)
			leer op
			//###################################################
			Si contador>20 Entonces
				Escribir "PERDEDOR!!! "
				Escribir " TOTAL DE TIROS DE DADOS GENERADOS : " contador-1
				Escribir "TOTAL DE LA SUMA DEL VALOR DE LOS DATOS GENERADOS : " (acumulador)
				Escribir "TOTAL DE PARES OBTENIDOS : " numpar
				op=0
				//#####################################################
			FinSi
			
		FinSi
		
	Fin Mientras
	
FinAlgoritmo

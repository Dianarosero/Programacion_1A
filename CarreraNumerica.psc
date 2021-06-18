Algoritmo carrera_numerica
	//Declaracion de variables
	Definir jugadores,tableros,dado1,dado2,acu_jugadores,cont_jugadores Como Entero
	Definir estado_juego Como Logico
	Definir espera_tecla Como Caracter
	//Inicializacion de variables
	acu_jugadores<-0
	cont_jugadores<-0
	estado_juego<-Verdadero
	//Entradas-Procesos
	Mientras estado_juego Hacer
		Escribir "::::::: JUEGO CARRERA NUMERICA :::::::"
		Escribir "- DIGITE LA CANTIDAD DE JUGADORES: "
		Escribir "Recuerde debe ser mínimo 2 y máximo 4"
		Leer jugadores
		Si (jugadores < 2) o (jugadores > 4) Entonces
			Repetir
				Escribir ": CANTIDAD DE JUGADORES INVALIDO :"
				Escribir "Recuerde debe ser mínimo 2 y máximo 4"
				Escribir "- DIGITE NUEVAMENTE LOS JUGADORES: "
				Leer jugadores
			Hasta Que jugadores=2 o jugadores=3 o jugadores=4
		FinSi
		acu_jugadores=acu_jugadores+(jugadores)
		cont_jugadores=cont_jugadores+1
		Escribir "- SELECCIONE EL NIVEL DE TABLERO: "
		Escribir "Digite 1 para el nivel básico (Tablero de 20 posiciones)"
		Escribir "Digite 2 para el nivel intermedio (Tablero de 30 posiciones)"
		Escribir "Digite 3 para el nivel avanzado (Tablero de 50 posiciones)"
		Leer tableros
		
		Segun tableros Hacer
			1:
				Escribir "- INICIO DEL JUEGO"
				Escribir "Turno:",cont_jugadores
				dado1<-Aleatorio(1,6)
				dado2<-Aleatorio(1,6)
				Escribir "Dado 1: ",dado1
				Escribir "Dado 2: ",dado2
			2:
				dado1<-Aleatorio(1,6)
				dado2<-Aleatorio(1,6)
			3:
				dado1<-Aleatorio(1,6)
				dado2<-Aleatorio(1,6)
		Fin Segun
		
		Leer espera_tecla
	FinMientras
	
	

FinAlgoritmo

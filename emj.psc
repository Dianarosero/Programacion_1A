Algoritmo sin_titulo
	definir palabr, palabra, casillas como caracter
	definir aciertos, turnos como real
	
	Escribir "      *Menú*"
	
	Escribir "   1. Nivel Bàsico"
	Escribir "   2. Nivel Medio"
	escribir "   3. Salir "
	escribir"   Ingrese su opciòn (1-3)"
	leer OP
	Segun OP hacer
		1:
			
			p_tb<-20
			oportunidades<-8
			dimension palabra[p_tb]
			
			palabra[0]<-"duda"
			palabra[1]<-"ojo"
			palabra[2]<-"anima"
			palabra[3]<-"duro"
			palabra[4]<-"pua"
			palabra[5]<-"ahoga"
			palabra[6]<-"dije"
			palabra[7]<-"vos"
			palabra[8]<-"acero"
			palabra[9]<-"echo"
			palabra[10]<-"uso"
			palabra[11]<-"apoye"
			palabra[12]<-"cuña"
			palabra[13]<-"rie"
			palabra[14]<-"almas"
			palabra[15]<-"gota"
			palabra[16]<-"via"
			palabra[17]<-"amigo"
			palabra[18]<-"copo"
			palabra[19]<-"feo"
			
			
			a_<-' '
			h_<-' '
			o_<-' '
			r_<-' '
			c_<-' '
			ax<-' '
			d_<-' '
			ox<-' '
			
			turnos<-0
			aciertos<-0
			
			palabr<-palabra[azar(p_tb)+1]
			n<-Longitud(palabr)
			Dimension casillas(n)
			Para x<-1 Hasta n Con Paso 1 Hacer
				casillas[x]<-"_"
			Fin Para
			Repetir
				Escribir ""
				escribir "Oportuniddes restantes: ", oportunidades-turnos
				Para x<-1 Hasta n Con Paso 1 Hacer
					Escribir Sin Saltar " ", casillas[x]
				Fin Para
				escribir " "
				Escribir Sin Saltar "Escriba la letra: "
				leer letra
				encontrando<-Falso
				Para x<-1 Hasta n Con Paso 1 Hacer
					chr<-Subcadena(palabr, x,x)
					Si Mayusculas(letra)=Mayusculas(chr) Entonces
						encontrando<-Verdadero
						si casillas[x]="_" Entonces
							casillas[x]<-chr
							aciertos<-aciertos+1
							
						FinSi
					Fin Si
				FinPara
				si no encontrando Entonces
					turnos<-turnos+1
					Escribir "Letra no encontrada."
					Segun turnos hacer
						1:
							a_<-'A'
						2:
							h_<-'H'
						3:
							o_<-'O'
						4 :
							r_<-'R'
						5:
							c_<-'C'
						6:
							ax<-'A'
						7:
							d_<-'D'
						8:
							Ox<-'O'
							
							
					FinSegun	
				FinSi
				Escribir "",a_
				Escribir "",h_
				Escribir "",o_
				Escribir "",r_
				Escribir "",c_
				Escribir "",ax
				Escribir "",d_
				Escribir "",ox
				
				
			Hasta Que turnos>=oportunidades o aciertos>=n;
			si aciertos=n Entonces
				
				Escribir "Felicidades, has ganado"
			sino
				Escribir "Has perdido."
			FinSi
			Escribir "La palabra secreta es: ", palabr;
			escribir "Aciertos: ",aciertos,"  Fallos: ",turnos
			escribir "PRESIONE CUALQUIER TECLA PARA CONTINUAR";
			esperar Tecla;
			
		2:
			
			p_tb<-20
			oportunidades<-8
			dimension palabra[p_tb]
			
			palabra[1]<-"fabricado"
			palabra[2]<-"camiseta"
			palabra[3]<-"ninguno"
			palabra[4]<-"zapato"
			palabra[5]<-"habaneros"
			palabra[6]<-"cabellera"
			palabra[7]<-"celular"
			palabra[8]<-"cobija"
			palabra[9]<-"habilidad"
			palabra[10]<-"eliminar"
			palabra[11]<-"galleta"
			palabra[12]<-"alarma"
			palabra[13]<-"vacilados"
			palabra[14]<-"bolsillo"
			palabra[15]<-"archivo"
			palabra[16]<-"espejo"
			palabra[17]<-"compilado"
			palabra[18]<-"celebrar"
			palabra[19]<-"rebotar"
			//palabra[20]<-"adorno"
			
			a_<-' '
			h_<-' '
			o_<-' '
			r_<-' '
			c_<-' '
			ax<-' '
			d_<-' '
			ox<-' '
			
			turnos<-0
			aciertos<-0
			//fallos<-0
			
			palabr<-palabra[azar(p_tb)+1]
			n<-Longitud(palabr)
			Dimension casillas(n)
			Para x<-1 Hasta n Con Paso 1 Hacer
				casillas[x]<-"_"
			Fin Para
			Repetir
				Escribir ""
				or=oportunidades-turnos
				escribir "Oportuniddes restantes: ", or
				Para x<-1 Hasta n Con Paso 1 Hacer
					Escribir Sin Saltar " ", casillas[x]
				Fin Para
				escribir " "
				Escribir Sin Saltar "Escriba la letra: "
				leer letra
				encontrando<-Falso
				Para x<-1 Hasta n Con Paso 1 Hacer
					chr<-Subcadena(palabr, x, x)
					Si Mayusculas(letra)=Mayusculas(chr) Entonces
						encontrando<-Verdadero
						si casillas[x]='_' Entonces
							casillas[x]<-nose
							aciertos<-aciertos+1
							
						FinSi
					Fin Si
				FinPara
				si no encontrando Entonces
					turnos<-turnos+1
					Escribir "Letra no encontrada."
					Segun turnos hacer
						1:
							a_<-'A'
						2:
							h_<-'H'
						3:
							o_<-'O'
						4 :
							r_<-'R'
						5:
							c_<-'C'
						6:
							ax<-'A'
						7:
							d_<-'D'
						8:
							Ox<-'O'
							
							
					FinSegun	
				FinSi
				Escribir "",a_
				Escribir "",h_
				Escribir "",o_
				Escribir "",r_
				Escribir "",c_
				Escribir "",ax
				Escribir "",d_
				Escribir "",ox
				
				
				
			Hasta Que turnos>=oportunidades o aciertos>=n;
			si aciertos=n Entonces
				
				Escribir "Felicidades, has ganado"
			sino
				Escribir "Has perdido."
			FinSi
			Escribir "La palabra secreta es: ", palabr;
			escribir "Aciertos: ",aciertos,"  Fallos: ",fallos, "  Intentos: ",intentos
			
			
		3:
			escribir "Usted ha salido del juego"
			
			de otro modo
			escribir "Obcion no valida"
	FinSegun
	
	escribir "PRESIONE CUALQUIER TECLA PARA CONTINUAR";
	esperar Tecla;
FinAlgoritmo
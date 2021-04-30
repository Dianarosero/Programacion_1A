Algoritmo Servicio_Militar
	Definir nom,gen,enf,resp Como Caracter
	Definir nacimiento,actual,edad Como Entero
	
	resp<-"S"
	Mientras resp="S" Hacer
		Borrar Pantalla
		Escribir "PROCESO PARA LEGALIZAR SERVICIO MILITAR"
		Escribir "---------------------------------------"
		Escribir "Digitar Nombres y Apellidos"
		Leer nom 
		Escribir "Digitar Año de Nacimiento" 
		Leer nacimiento
		Escribir "Digitar Año Actual" 
		Leer actual
		edad<-actual-nacimiento
		Escribir "Seleccionar Genero (M/F)"
		Leer gen
		Escribir "Enfermedad Cronica (S/N)" 
		Leer enf
		
		Si (edad >= 18) y (gen = "M") y (enf="N") o (edad >= 18) y (gen="F") y (enf="N") Entonces
			Escribir nom," debe prestar servicio militar"
		FinSi
		Si (edad >= 18) y (gen = "M") y (enf="S") Entonces
				Escribir nom," debe prestar servicio social"
			FinSi
				Si (edad >= 18) y (gen = "F") y (enf = "S") Entonces
					Escribir nom," no debe prestar ningun tipo de servicio"
				FinSi
					Si (edad <= 18) y (gen = "F") y (enf = "N") Entonces
						Escribir nom," debe prestar servicio social"
					FinSi
		Escribir "---------------------------------------"
		Escribir "Desea ingresar otro habitante? (S/N)"
		Leer resp
	FinMientras
FinAlgoritmo

Algoritmo Condicional
	Definir n1,n2,Answer Como Real
	n1 <- 0
	n2 <- 0
	n3 <- 0
	opt <- 0
	Escribir 'Digite primer numero: '
	Leer n1
	Escribir 'Digite segundo numero: '
	Leer n2
	Escribir ':.:.:MENU DE OPCIONES:.:.:'
	Escribir '[1] Sumar'
	Escribir '[2] Restar'
	Escribir '[3] Multiplicar'
	Escribir '[4] Dividir'
	Escribir 'Digite una opcion de la operacian a relizar: '
	Leer opt
	Si (opt==1) Entonces
		Answer <- n1+n2
		operacion <- 'Suma'
	SiNo
		Si (opt==2) Entonces
			Answer <- n1-n2
			operacion <- 'resta'
		SiNo
			Si (opt==3) Entonces
				Answer <- n1*n2
				operacion <- 'multiplicacion'
			SiNo
				Si (opt==4) Entonces
					Answer <- n1/n2
					operacion <- 'division'
				SiNo
					Borrar Pantalla
					Escribir 'La opcion seleccionada no es valida'
				FinSi
			FinSi
		FinSi
	FinSi
	Si (opt==1 O opt==2 O opt==3 O opt==4) Entonces
		Escribir 'El resultado de la ',operacion,' es: ',Answer
	FinSi
FinAlgoritmo

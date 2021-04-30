Algoritmo Condicipnal
	Definir n1,n2,answer Como Entero
	n1<-0
	n2<-0
	n3<-0
	opt<-0
	
	Escribir "Digite primer numero: "
	leer n1
	Escribir "Digite segundo numero"
	leer n2
	
	Escribir":::MENU DE OPCIONES:::"
	Escribir "[1] Sumar"
	Escribir "[2] Restar"
	Escribir "[3] Multiplicar"
	Escribir "[4] Dividir"
	Escribir "Digite una opcion de la operacian a relizar: "
	Leer opt
	
	Si (opt==1) Entonces
		Answer<-n1+n2
		operacion<-"Suma"
		Escribir "El resultado de la suma es: ",Answer
	SiNo
		Si (opt==2) Entonces
			Answer<-n1-n2
			operacion<-"resta"
			Escribir "El resultado de la resta es: ",Answer			
		SiNo
			Si (opt==3) Entonces
				Answer<-n1*n2
				operacion<-"multiplicacion"
				Escribir "El resultado de la multiplicacion es:",Answer
			SiNo
				Si (opt==4) Entonces
					Answer<-n1/n2
					operacion<-"division"
					Escribir "El resultado de la division es:",Answer
				SiNo
					Borrar Pantalla
					Escribir "La opcion seleccionada no es valida" 
				Fin Si
			Fin Si
		Fin Si
	FinSi
FinAlgoritmo

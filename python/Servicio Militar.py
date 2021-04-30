import os
resp="S"
def borrar():
    if os.name=="posix":
        os.system("clear")
    elif os.name=="ce" or os:
        os.system("cls")

while resp == "S":
    borrar()
    print("PROCESO PARA LEGALIZAR SERVICIO MILITAR")
    print("---------------------------------------")
    nom=input("Digitar Nombres y Apellidos: ")
    nacimiento=int(input("Digitar Año de Nacimiento: "))
    actual=int(input("Digitar Año Actual: " ))
    edad=actual-nacimiento
    gen=input("Digitar Genero (M/F): ")
    enf=input("Enfermedad cronica (S/N): ")
    print("---------------------------------------")

    if edad>=18 and gen=="M" and enf=="N" or edad>=18 and gen=="F" and enf=="N":
        print(f"{nom} debe prestar servicio militar")
    elif edad>=18 and gen=="M" and enf=="S":
        print(f"{nom} debe prestar servicio social")
    elif edad >=18 and gen=="F" and enf=="S":
        print(f"{nom} no debe prestar ningun tipo de servicio")
    elif edad<=18 and gen=="F" and enf=="N":
        print(f"{nom} debe prestar servicio social")

    print(" ")
    resp=input("Desea ingresar otro habitante? S/N: ")
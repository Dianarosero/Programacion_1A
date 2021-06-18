import os
from random import randint

# funciones

def validacionjugadores():
    global listajugadores,jugador1,jugador2,jugador3,jugador4,ronda,cont_par,cont_choque1,cont_choque2,cont_choque3,cont_choque4,acu_d1,acu_d2,acu_d3,acu_d4

    listajugadores=[]
    jugador1=[]
    jugador2=[]
    jugador3=[]
    jugador4=[]

    cont_jugadores=0
    ronda=0

    cont_par=0
    cont_choque1=0
    cont_choque2=0
    cont_choque3=0
    cont_choque4=0

    acu_d1=0
    acu_d2=0
    acu_d3=0
    acu_d4=0

    os.system("cls")

    print("####################################################################")
    print("                         Welcome Number Race                        ")
    print("####################################################################\n")
    
    estado = True
    while estado:
        print("::.                         CONFIG ZONE                          .::\n")
        print("----- Number of players \n")
        print("Los jugadores permitidos para empezar deben ser minimo 2 y maximo 4")
        jugadores = int(input("Digite numero de jugadores: "))
        
        if(jugadores == 2 or jugadores == 3 or jugadores == 4):
            estado = False
        
        else:
            print("\n::: La cantidad ingresada en incorrecta")
            
            key = input(".:: Presione una tecla para ingresar de nuevo ::.")
            validacionjugadores()

    print("\n----- Name of players")
    print("\nDigite el nombre de cada uno de los jugadores: \n")

    for x in range (jugadores):
        cont_jugadores=cont_jugadores+1
        listajugadores.append(input(f"Jugador {cont_jugadores} digite su nombre: "))
    
    menu()

def menu():

    global op

    print("\n::.                         MAIN MENU                         .::\n")
    print("----- Level \n")
    print("Ingresar el nivel para jugar: \n")
    print("[1] Nivel basico ( 50 posiciones )")
    print("[2] Nivel intermedio ( 100 posiciones )")
    print("[3] Nivel avanzado (Tablero de 200 posiciones)")
    print("[4] Informacion del desarrollador")
    print("[5] Ayuda")
    print("[6] Salir\n")
    
    op = int(input(".:: Ingrese opción: "))
    
    if op == 1:
        basico()
    elif op == 2:
        intermedio()
    elif op == 3:
        avanzado()
    elif op == 4:
        info()
    elif op ==5:
        ayuda()
    elif op==6:    
        print("\n::: Has salido del juego :::\n")
    else:
        print("::: Opción inválida, intente nuevamente :::")
        key = input(".::: Presione una tecla para volver al menú :::.")
        menu()

#NIVELES
    
def basico():
    
    global posiciones
    
    os.system("cls")
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("::::                    NIVEL BASICO                    ::::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    key = input(".:: Presione una tecla para empezar el juego ::.")

    posiciones=50

    juego()

def intermedio():

    global posiciones
    
    os.system("cls")
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":::                     NIVEL INTERMEDIO                 :::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    key = input(".:: Presione una tecla para empezar el juego ::.")

    posiciones=100

    juego()

def avanzado():

    global posiciones

    os.system("cls")
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":::                      NIVEL AVANZADO                  :::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    key = input(".:: Presione una tecla para empezar el juego ::.")

    posiciones=200
    
    juego()

#INICIACION

def juego():

    global jugador1,jugador2,jugador3,jugador4,ronda,cont_par,acu_d1,acu_d2,acu_d3,acu_d4,cont_choque1,cont_choque2,cont_choque3,cont_choque4

    estado=True
    while estado :
        i = 0
        a = False
        while i < len(listajugadores):
            a = True
            i = i + 1

        if(a):
            ronda = ronda + 1
            print(f"\n-------------------------- RONDA {ronda} --------------------------")

# JUGADOR 1

        if(a):
            dado1=0
            dado2=0
        
            if acu_d1 >= posiciones-6:
                dado1=randint(1,6)            
        
                print(f"\n::.                       TURNO DE {listajugadores[0]}                      .::")
                print("\nDado uno: ",dado1)

                acu_d1=acu_d1+dado1
                if acu_d1<=posiciones and (dado1 != 1 or dado2 !=1):
                    print(f"\nEl jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")

            if acu_d1 < posiciones-6:

                dado1=randint(1,6)
                dado2=randint(1,6)

                print("")
                print(f"\n::.                       TURNO DE {listajugadores[0]}                      .::")
                print("\nDado uno: ",dado1)
                print("Dado dos: ",dado2)    

                acu_d1=acu_d1+(dado1+dado2)
                if acu_d1<=posiciones and (dado1 != 1 or dado2 !=1):
                    print(f"\nEl jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")
                        
            if dado1==1 and dado2==1:
                acu_d1=acu_d1-(dado1+dado2)
                acu_d1=acu_d1+21 
                if acu_d1<posiciones:
                    print(f"El jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")
                elif acu_d1 > posiciones:
                    acu_d1=acu_d1-21
                    acu_d1=acu_d1+(dado1+dado2)
                    print(f"\nEl jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")

            if acu_d1 == acu_d2 and acu_d1 < posiciones:
                cont_choque2=cont_choque2+1
                acu_d2=acu_d2-acu_d2
                print(f"\nEl jugador {listajugadores[0]} chocó con el jugador {listajugadores[1]}")
                print(f"El jugador {listajugadores[1]} regresa a la salida\n")  

            if len(listajugadores) == 3:
                if acu_d1 == acu_d3 and acu_d1 < posiciones:
                    cont_choque3=cont_choque3+1
                    acu_d3=acu_d3-acu_d3
                    print(f"\nEl jugador {listajugadores[0]} chocó con el jugador {listajugadores[2]}")
                    print(f"El jugador {listajugadores[2]} regresa a la salida\n")

            if len(listajugadores) == 4:
                if acu_d1 == acu_d4 and acu_d1 < posiciones:
                    cont_choque4=cont_choque4+1
                    acu_d4=acu_d4-acu_d4
                    print(f"\nEl jugador {listajugadores[0]} chocó con el jugador {listajugadores[3]}")
                    print(f"El jugador {listajugadores[3]} regresa a la salida\n")

            while acu_d1 > posiciones:  
                if True:
                    acu_d1=acu_d1-(dado1+dado2)
                    print(f"Usted se encuentra en la posicion {acu_d1} de {posiciones}\n")
                    print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                    print(f"El jugador {listajugadores[0]} pierde el turno\n")

                    break

            if dado1 == dado2:
                cont_par=cont_par+1
            else:
                cont_par=0

            while dado1 == dado2:

                if acu_d1 >= posiciones-6:
                    dado1=randint(1,6)            

                    key = input(".:: Presione una tecla para volver a tirar ::.") 

                    print(f"\n::.                       TURNO DE {listajugadores[0]}                      .::")
                    print("\nDado uno: ",dado1)

                    acu_d1=acu_d1+dado1
                    if acu_d1<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")

                if acu_d1 < posiciones-6:

                    dado1=randint(1,6)
                    dado2=randint(1,6)

                    key = input(".:: Presione una tecla para volver a tirar ::.") 

                    print("")
                    print(f"\n::.                       TURNO DE {listajugadores[0]}                      .::")
                    print("\nDado uno: ",dado1)
                    print("Dado dos: ",dado2)    

                    acu_d1=acu_d1+(dado1+dado2)
                    if acu_d1<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")
                
                if dado1 == dado2:
                    cont_par=cont_par+1
                else:
                    cont_par=0
                            
                if cont_par == 3 or acu_d1==posiciones:
                    fin()             
                
                if dado1==1 and dado2==1:
                    acu_d1=acu_d1-(dado1+dado2)
                    acu_d1=acu_d1+21 
                    if acu_d1<posiciones:
                        print(f"El jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")
                    elif acu_d1 > posiciones:
                        acu_d1=acu_d1-21
                        acu_d1=acu_d1+(dado1+dado2)
                        print(f"\nEl jugador {listajugadores[0]} ha movido {acu_d1} posiciones de {posiciones}")
                
                if acu_d1 == acu_d2 and acu_d1 < posiciones:
                    cont_choque2=cont_choque2+1
                    acu_d2=acu_d2-acu_d2
                    print(f"\nEl jugador {listajugadores[0]} chocó con el jugador {listajugadores[1]}")
                    print(f"El jugador {listajugadores[1]} regresa a la salida\n")  

                if len(listajugadores) == 3:
                    if acu_d1 == acu_d3 and acu_d1 < posiciones:
                        cont_choque3=cont_choque3+1
                        acu_d3=acu_d3-acu_d3
                        print(f"\nEl jugador {listajugadores[0]} chocó con el jugador {listajugadores[2]}")
                        print(f"El jugador {listajugadores[2]} regresa a la salida\n")

                if len(listajugadores) == 4:
                    if acu_d1 == acu_d4 and acu_d1 < posiciones:
                        cont_choque4=cont_choque4+1
                        acu_d4=acu_d4-acu_d4
                        print(f"\nEl jugador {listajugadores[0]} chocó con el jugador {listajugadores[3]}")
                        print(f"El jugador {listajugadores[3]} regresa a la salida\n")

                while acu_d1 > posiciones:  
                    if True:
                        acu_d1=acu_d1-(dado1+dado2)
                        print(f"Usted se encuentra en la posicion {acu_d1} de {posiciones}\n")
                        print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                        print(f"El jugador {listajugadores[0]} pierde el turno\n")

                        break

        jugador1.append(acu_d1)
        if acu_d1==posiciones or cont_par == 3:
                fin()         

        if acu_d1 < posiciones:
            key = input(".:: Presione una tecla para continuar con el siguiente turno")
        
# JUGADOR 2

        if(a):
            dado1=0
            dado2=0
            if acu_d2 >= posiciones-6:
                dado1=randint(1,6)            
        
                print(f"\n::.                       TURNO DE {listajugadores[1]}                      .::")
                print("\nDado uno: ",dado1)

                acu_d2=acu_d2+dado1
                if acu_d2<=posiciones and (dado1 != 1 or dado2 !=1):
                    print(f"\nEl jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")

            if acu_d2 < posiciones-6:

                dado1=randint(1,6)
                dado2=randint(1,6)

                print("")
                print(f"\n::.                       TURNO DE {listajugadores[1]}                      .::")
                print("\nDado uno: ",dado1)
                print("Dado dos: ",dado2)    

                acu_d2=acu_d2+(dado1+dado2)
                if acu_d2<=posiciones and (dado1 != 1 or dado2 !=1):
                    print(f"\nEl jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")
                        
            if dado1==1 and dado2==1:
                acu_d2=acu_d2-(dado1+dado2)
                acu_d2=acu_d2+21 
                if acu_d2<posiciones:
                    print(f"El jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")
                elif acu_d2 > posiciones:
                    acu_d2=acu_d2-21
                    acu_d2=acu_d2+(dado1+dado2)
                    print(f"\nEl jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")

            if acu_d2 == acu_d1 and acu_d2 < posiciones:
                cont_choque1=cont_choque1+1
                acu_d1=acu_d1-acu_d1
                print(f"\nEl jugador {listajugadores[1]} chocó con el jugador {listajugadores[0]}")
                print(f"El jugador {listajugadores[0]} regresa a la salida\n")  

            if len(listajugadores) == 3:
                if acu_d2 == acu_d3 and acu_d2 < posiciones:
                    cont_choque3=cont_choque3+1
                    acu_d3=acu_d3-acu_d3
                    print(f"\nEl jugador {listajugadores[1]} chocó con el jugador {listajugadores[2]}")
                    print(f"El jugador {listajugadores[2]} regresa a la salida\n")

            if len(listajugadores) == 4:
                if acu_d2 == acu_d4 and acu_d2 < posiciones:
                    cont_choque4=cont_choque4+1
                    acu_d4=acu_d4-acu_d4
                    print(f"\nEl jugador {listajugadores[1]} chocó con el jugador {listajugadores[3]}")
                    print(f"El jugador {listajugadores[3]} regresa a la salida\n")

            while acu_d2 > posiciones:  
                if True:
                    acu_d2=acu_d2-(dado1+dado2)
                    print(f"Usted se encuentra en la posicion {acu_d2} de {posiciones}\n")
                    print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                    print(f"El jugador {listajugadores[1]} pierde el turno\n")

                    break

            if dado1 == dado2:
                cont_par=cont_par+1
            else:
                cont_par=0

            while dado1 == dado2:

                if acu_d2 >= posiciones-6:
                    dado1=randint(1,6)            

                    key = input(".:: Presione una tecla para volver a tirar ::.") 

                    print(f"\n::.                       TURNO DE {listajugadores[1]}                      .::")
                    print("\nDado uno: ",dado1)

                    acu_d2=acu_d2+dado1
                    if acu_d2<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")

                if acu_d2 < posiciones-6:

                    dado1=randint(1,6)
                    dado2=randint(1,6)

                    key = input(".:: Presione una tecla para volver a tirar ::.") 

                    print("")
                    print(f"\n::.                       TURNO DE {listajugadores[1]}                      .::")
                    print("\nDado uno: ",dado1)
                    print("Dado dos: ",dado2)    

                    acu_d2=acu_d2+(dado1+dado2)
                    if acu_d2<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")
                
                if dado1 == dado2:
                    cont_par=cont_par+1
                else:
                    cont_par=0
                            
                if cont_par == 3 or acu_d2==posiciones:
                    fin()             
                
                if dado1==1 and dado2==1:
                    acu_d2=acu_d2-(dado1+dado2)
                    acu_d2=acu_d2+21 
                    if acu_d2<posiciones:
                        print(f"El jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")
                    elif acu_d2 > posiciones:
                        acu_d2=acu_d2-21
                        acu_d2=acu_d2+(dado1+dado2)
                        print(f"\nEl jugador {listajugadores[1]} ha movido {acu_d2} posiciones de {posiciones}")
                
                if acu_d2 == acu_d1 and acu_d2 < posiciones:
                    cont_choque1=cont_choque1+1
                    acu_d1=acu_d1-acu_d1
                    print(f"\nEl jugador {listajugadores[1]} chocó con el jugador {listajugadores[0]}")
                    print(f"El jugador {listajugadores[0]} regresa a la salida\n")  

                if len(listajugadores) == 3:
                    if acu_d2 == acu_d3 and acu_d2 < posiciones:
                        cont_choque3=cont_choque3+1
                        acu_d3=acu_d3-acu_d3
                        print(f"\nEl jugador {listajugadores[1]} chocó con el jugador {listajugadores[2]}")
                        print(f"El jugador {listajugadores[2]} regresa a la salida\n")

                if len(listajugadores) == 4:
                    if acu_d2 == acu_d4 and acu_d2 < posiciones:
                        cont_choque4=cont_choque4+1
                        acu_d4=acu_d4-acu_d4
                        print(f"\nEl jugador {listajugadores[1]} chocó con el jugador {listajugadores[3]}")
                        print(f"El jugador {listajugadores[3]} regresa a la salida\n")

                while acu_d2 > posiciones:  
                    if True:
                        acu_d2=acu_d2-(dado1+dado2)
                        print(f"Usted se encuentra en la posicion {acu_d2} de {posiciones}\n")
                        print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                        print(f"El jugador {listajugadores[1]} pierde el turno\n")

                        break

        jugador2.append(acu_d2)
        if acu_d2==posiciones or cont_par == 3:
                fin()         

        if acu_d2 < posiciones:
            key = input(".:: Presione una tecla para continuar con el siguiente turno")

#JUGADOR 3

        if len(listajugadores) == 3 or len(listajugadores) == 4:
            if(a):
                dado1=0
                dado2=0
                if acu_d3 >= posiciones-6:
                    dado1=randint(1,6)            
            
                    print(f"\n::.                       TURNO DE {listajugadores[2]}                      .::")
                    print("\nDado uno: ",dado1)

                    acu_d3=acu_d3+dado1
                    if acu_d3<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")

                if acu_d3 < posiciones-6:

                    dado1=randint(1,6)
                    dado2=randint(1,6)

                    print("")
                    print(f"\n::.                       TURNO DE {listajugadores[2]}                      .::")
                    print("\nDado uno: ",dado1)
                    print("Dado dos: ",dado2)    

                    acu_d3=acu_d3+(dado1+dado2)
                    if acu_d3<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")
                            
                if dado1==1 and dado2==1:
                    acu_d3=acu_d3-(dado1+dado2)
                    acu_d3=acu_d3+21 
                    if acu_d3<posiciones:
                        print(f"El jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")
                    elif acu_d3 > posiciones:
                        acu_d3=acu_d3-21
                        acu_d3=acu_d3+(dado1+dado2)
                        print(f"\nEl jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")

                if acu_d3 == acu_d1 and acu_d3 < posiciones:
                    cont_choque1=cont_choque1+1
                    acu_d1=acu_d1-acu_d1
                    print(f"\nEl jugador {listajugadores[2]} chocó con el jugador {listajugadores[0]}")
                    print(f"El jugador {listajugadores[0]} regresa a la salida\n")  

                if acu_d3 == acu_d2 and acu_d3 < posiciones:
                    cont_choque2=cont_choque2+1
                    acu_d2=acu_d2-acu_d2
                    print(f"\nEl jugador {listajugadores[2]} chocó con el jugador {listajugadores[1]}")
                    print(f"El jugador {listajugadores[1]} regresa a la salida\n")

                if len(listajugadores) == 4:
                    if acu_d3 == acu_d4 and acu_d3 < posiciones:
                        cont_choque4=cont_choque4+1
                        acu_d4=acu_d4-acu_d4
                        print(f"\nEl jugador {listajugadores[2]} chocó con el jugador {listajugadores[3]}")
                        print(f"El jugador {listajugadores[3]} regresa a la salida\n")

                while acu_d3 > posiciones:  
                    if True:
                        acu_d3=acu_d3-(dado1+dado2)
                        print(f"Usted se encuentra en la posicion {acu_d3} de {posiciones}\n")
                        print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                        print(f"El jugador {listajugadores[2]} pierde el turno\n")

                        break

                if dado1 == dado2:
                    cont_par=cont_par+1
                else:
                    cont_par=0

                while dado1 == dado2:

                    if acu_d3 >= posiciones-6:
                        dado1=randint(1,6)            

                        key = input(".:: Presione una tecla para volver a tirar ::.") 

                        print(f"\n::.                       TURNO DE {listajugadores[2]}                      .::")
                        print("\nDado uno: ",dado1)

                        acu_d3=acu_d3+dado1
                        if acu_d3<=posiciones and (dado1 != 1 or dado2 !=1):
                            print(f"\nEl jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")

                    if acu_d3 < posiciones-6:

                        dado1=randint(1,6)
                        dado2=randint(1,6)

                        key = input(".:: Presione una tecla para volver a tirar ::.") 

                        print("")
                        print(f"\n::.                       TURNO DE {listajugadores[2]}                      .::")
                        print("\nDado uno: ",dado1)
                        print("Dado dos: ",dado2)    

                        acu_d3=acu_d3+(dado1+dado2)
                        if acu_d3<=posiciones and (dado1 != 1 or dado2 !=1):
                            print(f"\nEl jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")
                    
                    if dado1 == dado2:
                        cont_par=cont_par+1
                    else:
                        cont_par=0
                                
                    if cont_par == 3 or acu_d3==posiciones:
                        fin()             
                    
                    if dado1==1 and dado2==1:
                        acu_d3=acu_d3-(dado1+dado2)
                        acu_d3=acu_d3+21 
                        if acu_d3<posiciones:
                            print(f"El jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")
                        elif acu_d3 > posiciones:
                            acu_d3=acu_d3-21
                            acu_d3=acu_d3+(dado1+dado2)
                            print(f"\nEl jugador {listajugadores[2]} ha movido {acu_d3} posiciones de {posiciones}")
                    
                    if acu_d3 == acu_d1 and acu_d3 < posiciones:
                        cont_choque1=cont_choque1+1
                        acu_d1=acu_d1-acu_d1
                        print(f"\nEl jugador {listajugadores[2]} chocó con el jugador {listajugadores[0]}")
                        print(f"El jugador {listajugadores[0]} regresa a la salida\n")  

                    if acu_d3 == acu_d2 and acu_d3 < posiciones:
                        cont_choque2=cont_choque2+1
                        acu_d2=acu_d2-acu_d2
                        print(f"\nEl jugador {listajugadores[2]} chocó con el jugador {listajugadores[1]}")
                        print(f"El jugador {listajugadores[1]} regresa a la salida\n")

                    if len(listajugadores) == 4:
                        if acu_d3 == acu_d4 and acu_d3 < posiciones:
                            cont_choque4=cont_choque4+1
                            acu_d4=acu_d4-acu_d4
                            print(f"\nEl jugador {listajugadores[2]} chocó con el jugador {listajugadores[3]}")
                            print(f"El jugador {listajugadores[3]} regresa a la salida\n")

                    while acu_d3 > posiciones:  
                        if True:
                            acu_d3=acu_d3-(dado1+dado2)
                            print(f"Usted se encuentra en la posicion {acu_d3} de {posiciones}\n")
                            print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                            print(f"El jugador {listajugadores[2]} pierde el turno\n")

                            break

            jugador3.append(acu_d3)
            if acu_d3==posiciones or cont_par == 3:
                    fin()
            if acu_d3 < posiciones:
                key = input(".:: Presione una tecla para continuar con el siguiente turno") 
        
#JUGADOR 4

        if len(listajugadores) == 4:
            if(a):
                dado1=0
                dado2=0
                if acu_d4 >= posiciones-6:
                    dado1=randint(1,6)            
            
                    print(f"\n::.                       TURNO DE {listajugadores[3]}                      .::")
                    print("\nDado uno: ",dado1)

                    acu_d4=acu_d4+dado1
                    if acu_d4<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")

                if acu_d4 < posiciones-6:

                    dado1=randint(1,6)
                    dado2=randint(1,6)

                    print("")
                    print(f"\n::.                       TURNO DE {listajugadores[3]}                      .::")
                    print("\nDado uno: ",dado1)
                    print("Dado dos: ",dado2)    

                    acu_d4=acu_d4+(dado1+dado2)
                    if acu_d4<=posiciones and (dado1 != 1 or dado2 !=1):
                        print(f"\nEl jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")
                            
                if dado1==1 and dado2==1:
                    acu_d4=acu_d4-(dado1+dado2)
                    acu_d4=acu_d4+21 
                    if acu_d4<posiciones:
                        print(f"El jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")
                    elif acu_d4 > posiciones:
                        acu_d4=acu_d4-21
                        acu_d4=acu_d4+(dado1+dado2)
                        print(f"\nEl jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")

                if acu_d4 == acu_d1 and acu_d4 < posiciones:
                    cont_choque1=cont_choque1+1
                    acu_d1=acu_d1-acu_d1
                    print(f"\nEl jugador {listajugadores[3]} chocó con el jugador {listajugadores[0]}")
                    print(f"El jugador {listajugadores[0]} regresa a la salida\n")  

                if acu_d4 == acu_d2 and acu_d4 < posiciones:
                    cont_choque2=cont_choque2+1
                    acu_d2=acu_d2-acu_d2
                    print(f"\nEl jugador {listajugadores[3]} chocó con el jugador {listajugadores[1]}")
                    print(f"El jugador {listajugadores[1]} regresa a la salida\n")

                if acu_d4 == acu_d3 and acu_d4 < posiciones:
                    cont_choque3=cont_choque3+1
                    acu_d3=acu_d3-acu_d3
                    print(f"\nEl jugador {listajugadores[3]} chocó con el jugador {listajugadores[2]}")
                    print(f"El jugador {listajugadores[2]} regresa a la salida\n")

                while acu_d4 > posiciones:  
                    if True:
                        acu_d4=acu_d4-(dado1+dado2)
                        print(f"Usted se encuentra en la posicion {acu_d4} de {posiciones}\n")
                        print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                        print(f"El jugador {listajugadores[3]} pierde el turno\n")

                        break

                if dado1 == dado2:
                    cont_par=cont_par+1
                else:
                    cont_par=0

                while dado1 == dado2:

                    if acu_d4 >= posiciones-6:
                        dado1=randint(1,6)            

                        key = input(".:: Presione una tecla para volver a tirar ::.") 

                        print(f"\n::.                       TURNO DE {listajugadores[3]}                      .::")
                        print("\nDado uno: ",dado1)

                        acu_d4=acu_d4+dado1
                        if acu_d4<=posiciones and (dado1 != 1 or dado2 !=1):
                            print(f"\nEl jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")

                    if acu_d4 < posiciones-6:

                        dado1=randint(1,6)
                        dado2=randint(1,6)

                        key = input(".:: Presione una tecla para volver a tirar ::.") 

                        print("")
                        print(f"\n::.                       TURNO DE {listajugadores[3]}                      .::")
                        print("\nDado uno: ",dado1)
                        print("Dado dos: ",dado2)    

                        acu_d4=acu_d4+(dado1+dado2)
                        if acu_d4<=posiciones and (dado1 != 1 or dado2 !=1):
                            print(f"\nEl jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")
                    
                    if dado1 == dado2:
                        cont_par=cont_par+1
                    else:
                        cont_par=0
                                
                    if cont_par == 3 or acu_d4==posiciones:
                        fin()             
                    
                    if dado1==1 and dado2==1:
                        acu_d4=acu_d4-(dado1+dado2)
                        acu_d4=acu_d4+21 
                        if acu_d4<posiciones:
                            print(f"El jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")
                        elif acu_d4 > posiciones:
                            acu_d4=acu_d4-21
                            acu_d4=acu_d4+(dado1+dado2)
                            print(f"\nEl jugador {listajugadores[3]} ha movido {acu_d4} posiciones de {posiciones}")
                    
                    if acu_d4 == acu_d1 and acu_d4 < posiciones:
                        cont_choque1=cont_choque1+1
                        acu_d1=acu_d1-acu_d1
                        print(f"\nEl jugador {listajugadores[3]} chocó con el jugador {listajugadores[0]}")
                        print(f"El jugador {listajugadores[0]} regresa a la salida\n")  

                    if acu_d4 == acu_d2 and acu_d4 < posiciones:
                        cont_choque2=cont_choque2+1
                        acu_d2=acu_d2-acu_d2
                        print(f"\nEl jugador {listajugadores[3]} chocó con el jugador {listajugadores[1]}")
                        print(f"El jugador {listajugadores[1]} regresa a la salida\n")

                    if acu_d4 == acu_d3 and acu_d4 < posiciones:
                        cont_choque3=cont_choque3+1
                        acu_d3=acu_d3-acu_d3
                        print(f"\nEl jugador {listajugadores[3]} chocó con el jugador {listajugadores[2]}")
                        print(f"El jugador {listajugadores[2]} regresa a la salida\n")

                    while acu_d4 > posiciones:  
                        if True:
                            acu_d4=acu_d4-(dado1+dado2)
                            print(f"Usted se encuentra en la posicion {acu_d4} de {posiciones}\n")
                            print("Los dados obtenidos sobrepasan la cantidad de posiciones")
                            print(f"El jugador {listajugadores[3]} pierde el turno\n")

                            break

            jugador4.append(acu_d4)
            if acu_d4==posiciones or cont_par == 3:
                    fin()
            if acu_d4 < posiciones:
                key = input(".:: Presione una tecla para continuar con el siguiente turno")

#FINALIZACION 

def fin():
    print("")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("                         END OF THE GAME                      ")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("")
    estado=True
    while estado:

        if acu_d1==posiciones or cont_par == 3:
            print(f"GANADOR JUGADOR {listajugadores[0]}\n")

        elif acu_d2==posiciones or cont_par == 3:
            print(f"GANADOR JUGADOR {listajugadores[1]}\n")

        elif acu_d3==posiciones or cont_par == 3:
            print(f"GANADOR JUGADOR {listajugadores[2]}\n")

        elif acu_d4==posiciones or cont_par == 3:
            print(f"GANADOR JUGADOR {listajugadores[3]}\n")

        print("¿ Que desean hacer ?\n")
        print("[1] Visualizar tabla de jugadores")
        print("[2] Volver a jugar ")
        print("[3] Salir ")
        op = int(input("\n.:: Ingrese opción: "))
    
        if op == 1:
            tabla()
        elif op == 2:
            validacionjugadores()
        elif op == 3:
            print("\n::: Has salido del juego :::\n")
            quit()

# TABLA DE JUGADORES

def tabla():
    os.system("cls")
    print("\n::.                         SCORES ZONE                          .::\n")
    estado=True
    while estado :
        i = 0
        a = False
        while i < len(listajugadores):
            a = True
            i = i + 1

        if(a):
            print("--------------------------------------------------------\n")
            print(f"Jugador 1: {listajugadores[0]}\n")
            print(f"Posiciones avanzadas: {jugador1[-1]}")
            if acu_d1<posiciones:
                print(f"Posiciones que le faltaron: {posiciones-acu_d1}")
            print(f"Regresos a salida cuando fue chocado: {cont_choque1}\n")

            if acu_d1==posiciones or cont_par == 3:
                print(f"{listajugadores[0]} FUE EL GANADOR DEL JUEGO\n")

        if(a):
            print("--------------------------------------------------------\n")
            print(f"Jugador 2: {listajugadores[1]}\n")
            print(f"Posiciones avanzadas: {jugador2[-1]}")
            if acu_d2<posiciones:
                print(f"Posiciones que le faltaron: {posiciones-acu_d2}")
            print(f"Regresos a salida cuando fue chocado: {cont_choque2}\n")

            if acu_d2==posiciones or cont_par == 3:
                print(f"{listajugadores[1]} FUE EL GANADOR DEL JUEGO\n")

        if len(listajugadores) == 3 or len(listajugadores) == 4:
            if(a):
                print("--------------------------------------------------------\n")
                print(f"Jugador 3: {listajugadores[2]}\n")
                print(f"Posiciones avanzadas: {jugador3[-1]}")
                if acu_d3<posiciones:
                    print(f"Posiciones que le faltaron: {posiciones-acu_d3}")
                print(f"Regresos a salida cuando fue chocado: {cont_choque3}\n")

                if acu_d3==posiciones or cont_par == 3:
                    print(f"{listajugadores[2]} FUE EL GANADOR DEL JUEGO\n")

        if len(listajugadores) == 4:
            if(a):
                print("--------------------------------------------------------\n")
                print(f"Jugador 4: {listajugadores[3]}\n")
                print(f"Posiciones avanzadas: {jugador4[-1]}")
                if acu_d4<posiciones:
                    print(f"Posiciones que le faltaron: {posiciones-acu_d4}")
                print(f"Regresos a salida cuando fue chocado: {cont_choque4}\n")

                if acu_d4==posiciones or cont_par == 3:
                    print(f"{listajugadores[3]} FUE EL GANADOR DEL JUEGO\n")
                print("--------------------------------------------------------")
      

        print("¿ Que desean hacer ?\n")
        print("[1] Volver a jugar ")
        print("[2] Salir ")
        op = int(input("\n.:: Ingrese opción: "))
    
        if op == 1:
            validacionjugadores()
        elif op == 2:
            print("\n::: Has salido del juego :::\n")
            quit()

#INFORMACION

def info():
    os.system("cls")
    print("\n::.                     DEVELOPER INFORMATION                          .::\n")
    print("Programa:    Number Race.py")
    print("Autora  :    Diana Sofia Rosero López")
    print("Objetivo:    Juego que permite simular el comportamiento")
    print("             del juego de “Carrera numérica")

    key = input("\n... Presiona cualquier tecla para volver al menu ")
    os.system("cls")
    menu()

#AYUDA

def ayuda():
    os.system("cls")
    print("\n::.                     ASSISTANCE                          .::\n")
    print("----- Rules\n")
    print("Parámetros De Inicio:\n")
    print("- El número de jugadores debe ser: mínimo 2 y máximo 4")
    print("- Los niveles: Basic -> 50, Intermediate -> 100 y Advanced -> 200\n")
    print("Validaciones Del Juego:\n")
    print("- Si un jugador llega a la posición donde hay otro jugador [choque *],") 
    print("  el que estaba antes, regresa a salida, es decir inicia nuevamente,")
    print("  y el que llegó, queda esa posición.")
    print("- Si un jugador obtiene 3 pares consecutivos, GANA la partida")
    print("- Si un jugador obtiene par de unos (1, 1) al lanzar los dados, podrá")
    print("  avanzar simultáneamente veintiuna (21) posiciones, siempre que no")
    print("  exceda el límite a la meta")
    print("- El primer jugador que llegue a la meta es el ganador")
    
    key = input("\n... Presiona cualquier tecla para volver al menu ")
    os.system("cls")
    menu()

validacionjugadores()
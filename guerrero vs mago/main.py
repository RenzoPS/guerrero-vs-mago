from personaje import Personaje
from guerrero import Guerrero
from mago import Mago
from item import Item

import os, random, time

if __name__ == "__main__":
    

    pocion = Item("Pocion curativa", "Pocion", 20)
    arma = Item("Arma del Espartano", "Arma", 5)
    escudo = Item("Escudo de Doran", "Escudo", 5)

    eleccion = int(input("Que clase desea usar? 1- Guerrero, 2- Mago: "))
    nombre_player = str(input("Elija un nombre para su personaje: "))
    nombre_bot = str(input("Elija un nombre para su rival: "))

    if eleccion == 1:
        player1 = Guerrero(nombre_player)
        player2 = Mago(nombre_bot)
    elif eleccion == 2:
        player1 = Mago(nombre_player)
        player2 = Guerrero(nombre_bot)

    player1.inventario.extend([pocion, arma, escudo])
    player2.inventario.extend([pocion, arma, escudo])

    def usarItem(turno, pocion, arma, escudo):
        itemUsado = False
        while not itemUsado:
            os.system("cls")
            print(f"""Tienes: {[item.nombre for item in turno.inventario]}
---------------------------------------------------------------------""")
            usarItem = int(input("¿Que item desea usar? 1- Pocion; 2- Arma; 3- Escudo; (0- Salir): "))
            while usarItem < 0 or usarItem > 3:
                os.system("cls")
                print("""¡No se pudo utilizar este item!
Elija un valorr valido""")
                time.sleep(2)
                os.system("cls")
                usarItem = int(input("¿Que item desea usar? 1- Pocion; 2- Arma; 3- Escudo; (0- Salir): "))
            
            os.system("cls")
            if usarItem == 0:
                os.system("cls")
                print(f"""Intentaste abrir el inventario pero...
¡Tu enemigo se adelanto!""")
                return False
            elif usarItem == 1:
                if pocion in turno.inventario:
                    pocion.usar(turno)
                    print("---------------------------------")
                    turno.inventario.remove(pocion)
                    itemUsado = True
                else:
                    os.system("cls")
                    print("No tienes pocion!")
                    time.sleep(2)
                    os.system("cls")

            elif usarItem == 2:
                if arma in turno.inventario:
                    arma.usar(turno)
                    print("---------------------------------")
                    turno.inventario.remove(arma)
                    itemUsado = True
                else:
                    os.system("cls")
                    print("No tienes arma!")
                    time.sleep(2)
                    os.system("cls")

            elif usarItem == 3:
                if escudo in turno.inventario:
                    escudo.usar(turno)
                    print("---------------------------------")
                    turno.inventario.remove(escudo)
                    itemUsado = True
                else:
                    os.system("cls")
                    print("No tienes escudo!")
                    time.sleep(2)
                    os.system("cls")

    os.system("cls")
    print(player1.mostrarInfo())
    time.sleep(3)
    os.system("cls")
    print(player2.mostrarInfo())
    time.sleep(3)
    os.system("cls")

    ronda = 0
    print("Elijiendo quien empieza.")
    time.sleep(1)
    os.system("cls")
    print("Elijiendo quien empieza..")
    time.sleep(1)
    os.system("cls")
    print("Elijiendo quien empieza...")
    time.sleep(1)
    os.system("cls")

    turno = random.choice([player1, player2])
    print(f"¡Comienza {turno.nombre}!")
    time.sleep(2)
    os.system("cls")

    while player1.vida > 0 and player2.vida > 0:
        ronda += 1
        print(f"""Ronda: {ronda}
----------
Turno: {turno.nombre}
----------
HP: {turno.vida}
----------------------------------------------------""")
        accion = int(input("¿Que accion desea hacer? 1- Atacar; 2- Usar item: "))
        while accion < 1 or accion > 2:
            os.system("cls")
            print("""¡No se pudo realizar esta accion!
Elija un valorr valido""")
            time.sleep(2)
            os.system("cls")
            accion = int(input("¿Que accion desea hacer? 1- Atacar; 2- Usar item: "))
        
        if accion == 1: 
            os.system("cls")
            if turno == player1:
                player1.atacar(player2)
                turno = player2
            else:
                player2.atacar(player1)
                turno = player1
            time.sleep(2)
            os.system("cls")

        elif accion == 2:
            usarItem(turno, pocion, arma, escudo)
            if turno == player1:
                turno = player2
            else:
                turno = player1
            time.sleep(3)
            os.system("cls")

        
    if player1.vida > player2.vida:
        print(f"""El gandor es: {player1.name}
-----------------------
Le sobran {player1.vida} HP restantes
""")
    else:
        print(f"""El gandor es: {player2.name}
-----------------------
Le sobran {player2.vida} HP restantes
""")
            
    os.system("pause")
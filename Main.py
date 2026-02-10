import os
import random

tablero = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]

cartas = ["mono", "grulla", "tigre", "dragón", "serpiente"]
cartas = random.sample(cartas, 2)  

piezasJugadorRed = {
    "p1r": {"pos": (0, 0), "alive": True},
    "p2r": {"pos": (0, 1), "alive": True},
    "kr": {"pos": (0, 2), "alive": True},
    "p3r": {"pos": (0, 3), "alive": True},
    "p4r": {"pos": (0, 4), "alive": True},
    "cartas": cartas
}
piezasJugadorBlue = {
    "p1b": {"pos": (4, 0), "alive": True},
    "p2b": {"pos": (4, 1), "alive": True},
    "kb": {"pos": (4, 2), "alive": True},
    "p3b": {"pos": (4, 3), "alive": True},
    "p4b": {"pos": (4, 4), "alive": True}
}
EstadoPartida = ["En curso", "Gana Red", "Gana Blue"]   

def limpiarTerminal():
    os.system("cls")

def limpiarTablero():
    for fila in range(5):
        for col in range(5):
            tablero[fila][col] = " "

def armarTablero():
    limpiarTablero()
    for nombre, data in piezasJugadorRed.items():
        if data["alive"]:
            fila, col = data["pos"]
            tablero[fila][col] = nombre

    for nombre, data in piezasJugadorBlue.items():
        if data["alive"]:
            fila, col = data["pos"]
            tablero[fila][col] = nombre

def validaciones():
    if piezasJugadorRed["kr"]["pos"] == (4, 2):
        return("Gana Red")

    if piezasJugadorBlue["kb"]["pos"] == (0, 2):
        return("Gana Blue")
    

    
    return("En curso")

def imprimirTablero():
    for i in range(5):
        print(tablero[i])

def moverPieza(nombre, nueva_pos):
    if nombre in piezasJugadorRed:
        piezas = piezasJugadorRed
        rivales = piezasJugadorBlue
    elif nombre in piezasJugadorBlue:
        piezas = piezasJugadorBlue
        rivales = piezasJugadorRed
    else:
        return False

    if not piezas[nombre]["alive"]:
        return False

    fila, col = nueva_pos
    if not (0 <= fila < 5 and 0 <= col < 5):
        return False

    for enemigo, data in rivales.items():
        if data["alive"] and data["pos"] == nueva_pos:
            data["alive"] = False
            break

    piezas[nombre]["pos"] = nueva_pos
    return True


# armarTablero()
# imprimirTablero()
# moverPieza("kb", (2, 3))
# armarTablero()
# imprimirTablero()

# piezasJugadorBlue["p1b"]["alive"] = False
# armarTablero()
# imprimirTablero()

print (piezasJugadorBlue[cartas[0]])

# while True:
#     resultado = validaciones()
#     if resultado != "En curso":
#         print(resultado)
#         break


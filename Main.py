import os
import random

tablero = [[" " for _ in range(5)] for _ in range(5)]


cartasDisponibles = {
    "mono": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    "grulla": [(-1, 0), (1, -1), (1, 1)],
    "tigre": [(-2, 0), (1, 0)],
    "dragón": [(-1, -2), (-1, 2), (1, -1), (1, 1)],
    "serpiente": [(0, -1), (-1, 1), (1, 1)]
}

nombresCartas = list(cartasDisponibles.keys())
random.shuffle(nombresCartas)

cartasRed = nombresCartas[:2]
cartasBlue = nombresCartas[2:4]
cartaCentral = nombresCartas[4]

jugadorRed = {
    "piezas": {
        "p1r": {"pos": (0, 0), "alive": True},
        "p2r": {"pos": (0, 1), "alive": True},
        "kr":  {"pos": (0, 2), "alive": True},
        "p3r": {"pos": (0, 3), "alive": True},
        "p4r": {"pos": (0, 4), "alive": True},
    },
    "cartas": cartasRed
}

jugadorBlue = {
    "piezas": {
        "p1b": {"pos": (4, 0), "alive": True},
        "p2b": {"pos": (4, 1), "alive": True},
        "kb":  {"pos": (4, 2), "alive": True},
        "p3b": {"pos": (4, 3), "alive": True},
        "p4b": {"pos": (4, 4), "alive": True},
    },
    "cartas": cartasBlue
}
EstadoPartida = ["En curso", "Gana Red", "Gana Blue"]   

def limpiarTerminal():
    os.system("cls")

def limpiarTablero():
    for f in range(5):
        for c in range(5):
            tablero[f][c] = " "

def armarTablero():
    limpiarTablero()

    for nombre, data in jugadorRed["piezas"].items():
        if data["alive"]:
            f, c = data["pos"]
            tablero[f][c] = nombre

    for nombre, data in jugadorBlue["piezas"].items():
        if data["alive"]:
            f, c = data["pos"]
            tablero[f][c] = nombre

def validaciones():
    if jugadorRed["kr"]["pos"] == (4, 2):
        return("Gana Red")

    if jugadorBlue["kb"]["pos"] == (0, 2):
        return("Gana Blue")
    

    
    return("En curso")


def imprimirTablero():
    for fila in tablero:
        print(fila)

def moverPieza(jugador, rival, nombrePieza, carta, movimiento):
    pieza = jugador["piezas"].get(nombrePieza)

    if not pieza or not pieza["alive"]:
        return False

    if carta not in jugador["cartas"]:
        return False

    df, dc = movimiento
    f, c = pieza["pos"]
    nueva_pos = (f + df, c + dc)

    if not (0 <= nueva_pos[0] < 5 and 0 <= nueva_pos[1] < 5):
        return False

    if movimiento not in cartasDisponibles[carta]:
        return False

    for enemigo, data in rival["piezas"].items():
        if data["alive"] and data["pos"] == nueva_pos:
            data["alive"] = False
            break

    pieza["pos"] = nueva_pos
    return True

def intercambiarCarta(jugador, cartaUsada):
    global cartaCentral
    jugador["cartas"].remove(cartaUsada)
    jugador["cartas"].append(cartaCentral)
    cartaCentral = cartaUsada

def mostrarEstadoJugador(nombre, jugador):
    print(f"\nTurno de {nombre}")
    print("Piezas:")
    for p in jugador["piezas"]:
        if jugador["piezas"][p]["alive"]:
            print("-", p, jugador["piezas"][p]["pos"])

    print("Cartas:")
    for i, carta in enumerate(jugador["cartas"]):
        print(f"{i}: {carta}")

def mostrarMovimientosCarta(carta):
    movimientos = cartasDisponibles[carta]
    print(f"\nMovimientos de la carta {carta}:")
    for i, mov in enumerate(movimientos):
        print(f"{i}: {mov}")

def turno(jugador, rival, nombreJugador):
    mostrarEstadoJugador(nombreJugador, jugador)

    pieza = input("Pieza: ")
    carta_index = int(input("Carta (0 o 1): "))
    carta = jugador["cartas"][carta_index]

    mostrarMovimientosCarta(carta)
    mov_index = int(input("Movimiento: "))
    movimiento = cartasDisponibles[carta][mov_index]

    if moverPieza(jugador, rival, pieza, carta, movimiento):
        intercambiarCarta(jugador, carta)
        return True
    else:
        print("Movimiento inválido")
        return False

def main():
    turnoActual = "Red"

    while True:
        armarTablero()
        imprimirTablero()

        if turnoActual == "Red":
            turno(jugadorRed, jugadorBlue, "Red")
            turnoActual = "Blue"
        else:
            turno(jugadorBlue, jugadorRed, "Blue")
            turnoActual = "Red"

if __name__ == "__main__":
    main()
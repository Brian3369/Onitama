tablero = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]

jugadorRed = ["p1r", "p2r", "kr", "p3r", "p4r"]
jugadorBlue = ["p1b", "p2b", "kb", "p3b", "p4b"]
EstadoPartida = ["En curso", "Gana Red", "Gana Blue"]

def armarTablero():
    tablero[0][0] = jugadorRed[0]
    tablero[0][1] = jugadorRed[1]
    tablero[0][2] = jugadorRed[2]
    tablero[0][3] = jugadorRed[3]
    tablero[0][4] = jugadorRed[4]

    tablero[2][0] = jugadorBlue[0]

    tablero[4][0] = jugadorBlue[0]
    tablero[4][1] = jugadorBlue[1]
    tablero[4][2] = jugadorBlue[2]
    tablero[4][3] = jugadorBlue[3]
    tablero[4][4] = jugadorBlue[4]

def validaciones():
    if tablero[4][2] == jugadorRed[2]:
        return("Gana Red")

    if tablero[0][2] == jugadorBlue[2]:
        return("Gana Blue")
    
    return("En curso")

def imprimirTablero():
    for i in range(5):
        print(tablero[i])

armarTablero()
imprimirTablero()

while True:
    resultado = validaciones()
    # if resultado != "En curso":
    #     print(resultado)
    #     break


import matplotlib.pyplot as plt
import random

# Definir colores en inglés
colores_fichas = {
    "azul": "blue",
    "amarillo": "yellow",
    "verde": "green",
    "rojo": "red",
    "seguro": "saddlebrown"  # Color café para las zonas seguras
}

# Definir el circuito de movimiento de las fichas
circuito = [
    103, 104, 102, 120, 135, 134, 133, 132, 131, 130, 129, 144, 159, 174, 189, 204, 219, 218, 217, 202, 187, 172, 157, 142, 127, 126, 125, 124, 123, 122, 121, 106, 91, 92, 93, 94, 95, 96, 97, 82, 67, 52, 37, 22, 7, 8, 9, 24, 39, 54, 69, 84, 99, 100, 101, 102, 103
]

# Definir posiciones iniciales y movimientos para las fichas
movimientos = {
    "azul": [54, 69, 84, 99, 100, 101, 102, 103, 104, 102, 120, 135, 134, 133, 132, 131, 130, 129, 144, 159, 174, 189, 204, 219, 218, 217, 202, 187, 172, 157, 142, 127, 126, 125, 124, 123, 122, 121, 106, 91, 92, 93, 94, 95, 96, 97, 82, 67, 52, 37, 22, 7, 8, 9, 24, 39, 54],
    "amarillo": [133, 132, 131, 130, 129, 144, 159, 174, 189, 204, 219, 218, 217, 202, 187, 172, 157, 142, 127, 126, 125, 124, 123, 122, 121, 106, 91, 92, 93, 94, 95, 96, 97, 82, 67, 52, 37, 22, 7, 8, 9, 24, 39, 54, 69, 84, 99, 100, 101, 102, 103, 104, 102, 120, 135, 134, 133],
    "verde": [187, 172, 157, 142, 127, 126, 125, 124, 123, 122, 121, 106, 91, 92, 93, 94, 95, 96, 97, 82, 67, 52, 37, 22, 7, 8, 9, 24, 39, 54, 69, 84, 99, 100, 101, 102, 103, 104, 102, 120, 135, 134, 133, 132, 131, 130, 129, 144, 159, 174, 189, 204, 219, 218, 217, 202, 187],
    "rojo": [94, 95, 96, 97, 82, 67, 52, 37, 22, 7, 8, 9, 24, 39, 54, 69, 84, 99, 100, 101, 102, 103, 104, 102, 120, 135, 134, 133, 132, 131, 130, 129, 144, 159, 174, 189, 204, 219, 218, 217, 202, 187, 172, 157, 142, 127, 126, 125, 124, 123, 122, 121, 106, 91, 92, 93, 94]
}

# Definir las rutas finales para cada color
rutas_finales = {
    "azul": [54, 69, 84, 99, 100, 101, 102, 103, 104, 102, 120, 119, 118, 117, 116, 115, 114],
    "amarillo": [133, 132, 131, 130, 129, 144, 159, 174, 189, 204, 219, 218, 203, 188, 173, 158, 143, 128],
    "verde": [187, 172, 157, 142, 127, 126, 125, 124, 123, 122, 121, 106, 107, 108, 109, 110, 111, 112],
    "rojo": [94, 95, 96, 97, 82, 67, 52, 37, 22, 7, 8, 23, 38, 53, 68, 83, 98]
}

# Posiciones de la cárcel para cada color
posiciones_carcel = {
    "azul": [(1, 12), (1, 13), (2, 12), (2, 13)],
    "amarillo": [(13, 12), (13, 13), (14, 12), (14, 13)],
    "verde": [(13, 1), (13, 2), (14, 1), (14, 2)],
    "rojo": [(1, 1), (1, 2), (2, 1), (2, 2)]
}

# Definir zonas seguras
zonas_seguras = [106, 94, 8, 54, 120, 133, 218, 187, 106, 94, 124, 189, 52, 103]

# Crear el tablero
def crear_tablero(fichas_pos):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(range(15))
    ax.set_yticks(range(15))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', color='black', linewidth=0.5)

    # Colorear las zonas del tablero
    for x in range(15):
        for y in range(15):
            if (0 <= x <= 5 and 0 <= y <= 5):  # Zona roja
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color="red", alpha=0.2))
            elif (9 <= x <= 14 and 0 <= y <= 5):  # Zona verde
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color="green", alpha=0.2))
            elif (0 <= x <= 5 and 9 <= y <= 14):  # Zona azul
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color="blue", alpha=0.2))
            elif (9 <= x <= 14 and 9 <= y <= 14):  # Zona amarilla
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color="yellow", alpha=0.2))

    # Colorear zonas seguras
    for casilla in zonas_seguras:
        x, y = divmod(casilla - 1, 15)
        ax.add_patch(plt.Rectangle((y, x), 1, 1, color=colores_fichas["seguro"], alpha=0.5))

    # Colorear casillas grises
    casillas_grises = [
        127, 128, 129, 112, 113, 114, 97, 98, 99,
        143, 158, 173, 188, 203, 115, 116, 117, 118, 119,
        83, 68, 53, 38, 23, 111, 110, 109, 108, 107
    ]
    for casilla in casillas_grises:
        x, y = divmod(casilla - 1, 15)
        ax.add_patch(plt.Rectangle((y, x), 1, 1, color="gray", alpha=0.5))

    # Escribir "meta" en la casilla 113
    x, y = divmod(113 - 1, 15)
    ax.text(y + 0.5, x + 0.5, "META", color="black", ha="center", va="center", fontsize=8, fontweight='bold')

    # Dibujar las fichas
    for color, posiciones in fichas_pos.items():
        for idx, pos in enumerate(posiciones):
            if pos == "carcel":
                x, y = posiciones_carcel[color][idx]
            else:
                x, y = divmod(pos - 1, 15)
            ficha = plt.Circle((y + 0.5, x + 0.5), 0.3, color=colores_fichas[color], ec="black", lw=1.5)
            ax.add_patch(ficha)

    plt.title("Tablero Personalizado de Parqués")
    plt.axis("equal")
    plt.show()

# Función para verificar si un jugador ha ganado
def verificar_victoria(fichas_pos):
    for color, posiciones in fichas_pos.items():
        if all(pos == rutas_finales[color][-1] for pos in posiciones):
            return color
    return None

# Función para lanzar los dados
def lanzar_dados(modo):
    if modo == "real":
        return random.randint(1, 6), random.randint(1, 6)
    elif modo == "desarrollador":
        dado1 = int(input("Ingrese el valor del primer dado: "))
        dado2 = int(input("Ingrese el valor del segundo dado: "))
        return dado1, dado2

# Función para mover una ficha
def mover_ficha(jugador, fichas_pos, pasos, eleccion):
    ficha_elegida = fichas_pos[jugador][eleccion]
    indice_actual = movimientos[jugador].index(ficha_elegida)
    nueva_pos = movimientos[jugador][(indice_actual + pasos) % len(movimientos[jugador])]

    # Verificar bloqueos
    if any(posiciones.count(nueva_pos) > 1 for posiciones in fichas_pos.values()):
        print("Movimiento bloqueado. La casilla", nueva_pos, "está ocupada por dos fichas.")
        nueva_pos = movimientos[jugador][(indice_actual + pasos - 1) % len(movimientos[jugador])]

    # Verificar si la nueva posición está ocupada por una ficha enemiga
    for color, posiciones in fichas_pos.items():
        if color != jugador and nueva_pos in posiciones and nueva_pos not in zonas_seguras:
            print("Ficha", ficha_elegida, "captura la ficha enemiga en", nueva_pos, ".")
            fichas_pos[color][posiciones.index(nueva_pos)] = "carcel"
            pasos += 20  # Movimiento adicional por captura

    # Actualizar posición de la ficha
    fichas_pos[jugador][eleccion] = nueva_pos
    return fichas_pos, pasos

# Modificar la función de juego para incluir la verificación de victoria
def juego_parques(turnos, modo):
    fichas_pos = {
        "azul": ["carcel", "carcel", "carcel", "carcel"],
        "amarillo": ["carcel", "carcel", "carcel", "carcel"],
        "verde": ["carcel", "carcel", "carcel", "carcel"],
        "rojo": ["carcel", "carcel", "carcel", "carcel"]
    }

    pares_consecutivos = 0
    ultima_ficha_movida = None
    jugadores = ["azul", "amarillo", "verde", "rojo"]

    for turno in range(turnos):
        jugador = jugadores[turno % len(jugadores)]
        dado1, dado2 = lanzar_dados(modo)
        print("Turno", turno + 1, ": Jugador", jugador, "(Dados:", dado1, ",", dado2, ")")

        # Verificar si puede sacar una ficha de la cárcel
        if "carcel" in fichas_pos[jugador]:
            if dado1 == 5 or dado2 == 5 or dado1 + dado2 == 5:
                print("Jugador", jugador, "saca un 5 y libera una ficha de la cárcel.")
                fichas_pos[jugador][fichas_pos[jugador].index("carcel")] = movimientos[jugador][0]
            else:
                print("Jugador", jugador, "no puede mover porque no sacó un 5 para liberar fichas.")
                continue

        # Mostrar opciones de fichas
        print("Posiciones actuales de las fichas del jugador", jugador, ":", fichas_pos[jugador])
        for i, ficha in enumerate(fichas_pos[jugador]):
            print("Ficha", i + 1, ":", ficha)

        # Elegir ficha
        while True:
            try:
                eleccion = int(input("Elige la ficha a mover (1-" + str(len(fichas_pos[jugador])) + "): ")) - 1
                if 0 <= eleccion < len(fichas_pos[jugador]) and fichas_pos[jugador][eleccion] != "carcel":
                    break
                else:
                    print("Elección no válida. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingresa un número.")

        ficha_elegida = fichas_pos[jugador][eleccion]
        print("Has elegido mover la ficha en", ficha_elegida, ".")

        # Calcular nueva posición
        pasos = dado1 + dado2
        fichas_pos, pasos = mover_ficha(jugador, fichas_pos, pasos, eleccion)
        print("Ficha", eleccion + 1, "avanza de", ficha_elegida, "a", fichas_pos[jugador][eleccion], "con", pasos, "pasos.")
        crear_tablero(fichas_pos)

        # Verificar si el jugador ha ganado
        ganador = verificar_victoria(fichas_pos)
        if ganador:
            print("¡El jugador", ganador, "ha ganado el juego!")
            break

        # Verificar si los dados son iguales para turno adicional
        if dado1 == dado2:
            pares_consecutivos += 1
            if pares_consecutivos == 3 and ultima_ficha_movida:
                jugador, ficha_idx = ultima_ficha_movida
                fichas_pos[jugador][ficha_idx] = "carcel"
                print("Jugador", jugador, "obtiene tres pares consecutivos. La ficha", ficha_idx + 1, "regresa a la cárcel.")
                pares_consecutivos = 0
            else:
                print("Jugador", jugador, "obtiene un turno adicional.")
                continue
        else:
            pares_consecutivos = 0

# Solicitar al usuario que elija el modo de juego
modo = input("Elija el modo de juego (real/desarrollador): ").strip().lower()
while modo not in ["real", "desarrollador"]:
    print("Modo no válido. Intente de nuevo.")
    modo = input("Elija el modo de juego (real/desarrollador): ").strip().lower()

# Ejecutar el juego con 300 turnos
juego_parques(300, modo)

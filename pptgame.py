import random

def juego():
    opciones = ["piedra", "papel", "tijeras"]
    usuario = input("Elige piedra, papel o tijeras: ").lower()
    computadora = random.choice(opciones)

    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("Empate!")
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        print("Ganaste!")
    else:
        print("Perdiste!")

juego()

import random

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "tijeras" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

opciones = ["piedra", "papel", "tijeras"]

while True:
    jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()
    if jugador == "salir":
        print("Gracias por jugar. ¡Hasta pronto!")
        break
    if jugador not in opciones:
        print("Opción inválida, intenta de nuevo.")
        continue
    
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    resultado = determinar_ganador(jugador, computadora)
    print(resultado)


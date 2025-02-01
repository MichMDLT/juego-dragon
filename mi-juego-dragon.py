import random

def jugar_mazmorra():
    while True:
        print("\n¿Dónde está el dragón? 🏰🐉")
        print("Tienes 3 puertas frente a ti, elige una:")
        print("1️⃣ Puerta roja")
        print("2️⃣ Puerta azul")
        print("3️⃣ Puerta verde")

        # Manejo de errores para evitar que el usuario ingrese algo inválido
        try:
            response = int(input("¿Cuál eliges, 1, 2 o 3?: "))
            if response not in [1, 2, 3]:
                print("⚠️ Opción inválida. Debes elegir 1, 2 o 3.")
                continue  # Volver a pedir la entrada
        except ValueError:
            print("⚠️ Ingresa un número válido (1, 2 o 3).")
            continue

        # Generar aleatoriamente la puerta con el dragón
        puertaDragon = random.randint(1, 3)

        if response == puertaDragon:
            print("🔥🐉 ¡Mala suerte! El dragón te ha encontrado. ¡CORREEEE! 🔥🐉")
        else:
            print("🏆 ¡Has escapado con éxito! ¡BUEN TRABAJO, CABALLERO REAL! 🏆")

        # Preguntar si quiere jugar de nuevo
        jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (sí/no): ").strip().lower()
        if jugar_de_nuevo not in ["sí", "si"]:
            print("Gracias por jugar. ¡Hasta la próxima aventura! 🏰✨")
            break  # Termina el juego

# Llamar a la función para empezar el juego
jugar_mazmorra()


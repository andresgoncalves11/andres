import random

def jugar():
    # Envolvemos todo en un bucle de "repetición"
    while True:
        numero_secreto = random.randint(1, 100)
        intentos = 0
        ganado = False

        print("\n--- ¡Nueva Partida! He pensado un número del 1 al 100 ---")

        while not ganado:
            try:
                apuesta = int(input("Introduce tu número: "))
                intentos += 1

                if apuesta < numero_secreto:
                    print("Más alto...")
                elif apuesta > numero_secreto:
                    print("Más bajo...")
                else:
                    print(f"¡Felicidades! Lo lograste en {intentos} intentos.")
                    ganado = True
            except ValueError:
                print("Escribe un número válido.")

        # Aquí es donde creamos el "botón" lógico de volver a jugar
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        
        if respuesta != 's':
            print("¡Gracias por jugar! Presiona Enter para salir.")
            input() # Pausa antes de cerrar la consola
            break # Rompe el bucle principal y termina el programa

jugar()
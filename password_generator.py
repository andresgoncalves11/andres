#Generador de contraseñas
import random
import os
os.system('clear')
def generar_contrasena():
    Mayusculas = ["A", "B", "C", "D", "E", "F", "G"]
    Minusculas = ["a", "b", "c", "d", "e", "f", "g"]
    Numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Simbolos = ["!", "@", "#", "$", "%", "^", "&"]
    caracteres = Mayusculas + Minusculas + Numeros + Simbolos

    lista = []
    
    for i in range(15):
        lista.append(random.choice(caracteres))

    contrasena = "".join(lista)
    return contrasena


print("Tu contraseña es:",generar_contrasena())
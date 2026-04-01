def variable_1():
    print("Introduce tu palabra para verificar si es un palíndromo:")
    palabra = input().lower()
    palabra = palabra.replace(" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return "La palabra es un palíndromo."
    else:
        return "La palabra no es un palíndromo."

print(variable_1())

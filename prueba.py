import os
os.system ('clear')

print("Bienvenido a la prueba") 
print("Han pasado varios meses")
print("¿Quieres continuar? S/N")
respuesta = input("respuesta: ")
respuesta = respuesta.upper()
if respuesta == "N":
    print("Has decidido no continuar.")
else:
    print("Mira esta lista")
    lista = ["A", "B", "C", "D", "E", "F", "G"]
    print (lista)
    print ("Mira ahora")
    lista.append ("Hola")
    print (lista)
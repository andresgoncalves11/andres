import os
os.system('clear')
print("Bienvenido al cajero automático")
print("ingrese su saldo")
saldo = float(input("Saldo: "))
while True:
    print("--------------------------------------------------------------------")
    print("Selecciona una opción")
    print("1.Revisa tu saldo")
    print("2.Retirar dinero")
    print("3.Depositar")
    print("4.Salir")
    respuesta = int(input("Escoge una opción: "))
    if respuesta == 1:
     os.system('clear')
     print(f"este es tu saldo {saldo}$")
     continue
    elif respuesta == 2:
     print("Escoja cuánto dinero desea retirar")
     dinero = float(input("Monto: "))
     os.system('clear')
     print(f"Se ha retirado {dinero}$")
     saldo = saldo - dinero
     continue
    elif respuesta == 3:
     print("Escoja su destinatario")
     destinatario = str(input("Destinatario: "))
     print("Escoja el Monto")
     Monto_2 = float(input("Monto: "))
     os.system('clear')
     print(f"Se ha transferido {Monto_2}$ a {destinatario}")
     saldo = saldo - Monto_2
     continue
    elif respuesta == 4:
     print("Hasta luego")
     break    

    
    


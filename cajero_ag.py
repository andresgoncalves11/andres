import os
os.system('clear')
while True:
 print("Ingrese su número de cédula")
 cedula = str(input("Cédula: "))
 if cedula == "1234567890":
    break
    print("Cédula correcta")
 else:   print("Cédula incorrecta")
 continue
os.system('clear')
print("Bienvenido al cajero automático")
print("ingrese su saldo")
saldo = float(input("Saldo: "))
print("Seleccione su moneda")
print("1.USD")
print("2.Bs")
moneda = int(input("Moneda: "))
if moneda == 1:
    moneda = "USD"
elif moneda == 2:
      moneda = "Bs"
else:   print("Moneda no válida")
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
     print(f"este es tu saldo {saldo} {moneda}")
     continue
    elif respuesta == 2:
     print("Escoja cuánto dinero desea retirar")
     dinero = float(input("Monto: "))
     os.system('clear')
     print(f"Se ha retirado {dinero} {moneda}")
     saldo = saldo - dinero
     print(f"Su saldo es de {saldo} {moneda}")
     continue
    elif respuesta == 3:
     print("Escoja su destinatario")
     destinatario = str(input("Destinatario: "))
     print("Escoja el Monto")
     Monto_2 = float(input("Monto: "))
     os.system('clear')
     print(f"Se ha transferido {Monto_2} {moneda} a {destinatario}")
     saldo = saldo - Monto_2
     print(f"Su saldo es de {saldo} {moneda}")
     continue
    elif respuesta == 4:
     print("Hasta luego")
     break    

    
    


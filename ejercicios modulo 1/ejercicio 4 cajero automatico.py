print("\nCajero Automatico")

saldo = 1000.0
opciones_validas = ("1", "2", "3", "4")
historial = []
continuar = True

print("\nBIENVENIDO AL CAJERO AUTOMÁTICO")

while continuar:
    print("\nMenú de opciones:")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir")
    
    opcion = input("\nSeleccione una opción (1-4): ")

    if opcion in opciones_validas:
        
        if opcion == "1":
            print(f"Tu saldo actual es: {saldo}bs")
            historial.append("Consulta de saldo")

        elif opcion == "2":
            monto = float(input("Monto a depositar: "))
            saldo += monto 
            historial.append(f"Depósito: +{monto}bs")
            print("Depósito exitoso.")

        elif opcion == "3":
            monto = float(input("Monto a retirar: "))
            if monto <= saldo:
                saldo -= monto 
                historial.append(f"Retiro: -{monto}bs")
                print("Retiro exitoso.")
            else:
                print("Saldo insuficiente.")
                historial.append(f"Intento de retiro fallido: {monto}bs")

        elif opcion == "4":
            print("Gracias por usar nuestro cajero. Hasta pronto!")
            continuar = False  

    else:
        print("Opción no válida. Intente de nuevo.")


print("\nRESUMEN DE MOVIMIENTOS:")
if historial:
    for movimiento in historial:
        print(f"- {movimiento}")
else:
    print("No se realizaron movimientos.")
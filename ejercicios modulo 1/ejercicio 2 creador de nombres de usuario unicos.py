print("Creador de nombres de usuario")

nombres_prohibidos= ("admin", "root", "boss", "staff", "security")

nombres_rechazados= []

usuario= input("Introduce un nombre de usuario: ").lower()

while usuario in nombres_prohibidos:
    print(f"Lo siento, '{usuario}' es un nombre reservado.")
    
    nombres_rechazados.append(usuario)
    
    usuario= input("Prueba con otro nombre: ").lower()

print(f"\nFelicidades!, Tu nuevo usuario es: {usuario}")

if nombres_rechazados:
    print(f"Historial de intentos rechazados: {nombres_rechazados}")
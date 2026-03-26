print("Logica arbitral piedra/papel/tijeras")

J1= input("Jugador 1 elige 'PIEDRA/PAPEL/TIJERAS': ").lower()
J2= input("Jugador 2 elige 'PIEDRA/PAPEL/TIJERAS': ").lower()

if   (J1 == "piedra" and J2 == "piedra") or \
     (J1 == "tijeras" and J2 == "tijeras") or \
     (J1 == "papel" and J2 == "papel"):
    print(f"Empate!, los dos eligeron {J1}")
    
elif (J1 == "piedra" and J2 == "tijeras") or \
     (J1 == "tijeras" and J2 == "papel") or \
     (J1 == "papel" and J2 == "piedra"):
    print(f"Gana el jugador 1!, {J1} le gana a {J2}")

elif (J2 == "piedra" and J1 == "tijeras") or \
     (J2 == "tijeras" and J1 == "papel") or \
     (J2 == "papel" and J1 == "piedra"):
    print(f"Gana el jugador 2!, {J2} le gana a {J1}")

else:
    print("ERROR")
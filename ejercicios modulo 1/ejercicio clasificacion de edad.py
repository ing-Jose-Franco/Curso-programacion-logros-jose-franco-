print("Clasificacion de edad")

edad=int(input("Cual es tu edad?: "))

if edad >= 18 and edad <= 100:
    print(f"Tienes {edad} y eres mayor de edad")

elif edad >= 0 and edad < 18:
    print(f"Tienes {edad} y eres menor de edad")

else:
    print("ERROR")
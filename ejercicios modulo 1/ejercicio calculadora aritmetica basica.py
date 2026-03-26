print("\nCalculadora aritmetica basica\n")

num1=float(input("Elige el primer numero para la operacion: "))
num2=float(input("Elige el segundo numero para la operacion: "))

operacion=(input("\n¿QUE OPERACION DESEAS REALIZAR?\n\n SUMA\n RESTA\n MULTIPLICACION\n DIVISION\n\n")).lower

if operacion == "suma":
    sum= round((num1 + num2), 2)
    print(f"La Suma de los 2 numeros es {sum}")

elif operacion == "resta":
    rest= round((num1 - num2), 2)
    print(f"La Resta de los 2 numeros es {rest}")

elif operacion == "multiplicacion":
    multi= round((num1 * num2), 2)
    print(f"La multiplicacion de los 2 numeros es {multi}")

elif operacion == "division":
    if num1 != 0 and num2 !=0:
        div= round((num1 / num2), 2)
        print(f"La division de los 2 numeros es {div}")
    else:
        print("No se puede dividir por 0")
else:
    print("ERROR")
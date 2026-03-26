print("\nCalculadora aritmetica basica\n")

num1=float(input("Elige el primer numero para la operacion: "))
num2=float(input("Elige el segundo numero para la operacion: "))

operacion=(input("\n¿QUE OPERACION DESEAS REALIZAR?\n\n SUMA\n RESTA\n MULTIPLICACION\n DIVISION\n\n")).lower

if operacion == "suma":
    suma= round((num1 + num2), 2)
    print(f"La Suma de los 2 numeros es {suma}")

elif operacion == "resta":
    resta= round((num1 - num2), 2)
    print(f"La Resta de los 2 numeros es {resta}")

elif operacion == "multiplicacion":
    multiplicacion= round((num1 * num2), 2)
    print(f"La multiplicacion de los 2 numeros es {multiplicacion}")

elif operacion == "division":
    if num1 != 0 and num2 !=0:
        division= round((num1 / num2), 2)
        print(f"La division de los 2 numeros es {division}")
    else:
        print("No se puede dividir por 0")
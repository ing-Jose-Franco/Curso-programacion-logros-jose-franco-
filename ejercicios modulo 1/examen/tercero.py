notas=()

while True:
    entrada= input("Coloque la nota del alumno o escriba FIN para terminar: ").lower
    if entrada == "fin":
        break
        
    try:
        numero = float(entrada)
        notas.append(numero)
    except ValueError:
        print("Por favor, ingresa un número válido o la palabra 'fin'.")

if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"\nLista de números: {notas}")
    print(f"El promedio es: {promedio:.2f}")
else:
    print("\nNo se ingresaron números para calcular el promedio.")
       
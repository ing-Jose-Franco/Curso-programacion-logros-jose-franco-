import random

numero= random.randint(1, 100)
print("---ADIVINA EL NUMERO---")

while True:
    seleccion= int(input("Elige un  del 1 al 100: "))
    if seleccion > numero:
        print(f"El numero {seleccion} es mayor.")

    elif seleccion < numero:
        print(f"El numero {seleccion} es menor.")
    
    else:
        print(f"CORRECTO, El numero era {numero}")
        break
        
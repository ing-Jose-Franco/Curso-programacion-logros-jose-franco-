import random

numero= random.randint(1, 100)
booleano= True
print("---ADIVINA EL NUMERO---")

while booleano:
    seleccion= int(input("Elige un  del 1 al 100: "))
    if seleccion > numero:
        print(f"El numero {seleccion} es mayor.")

    elif seleccion < numero:
        print(f"El numero {seleccion} es menor.")
    
    else:
        print(f"CORRECTO, El numero era {numero}")
        break
        
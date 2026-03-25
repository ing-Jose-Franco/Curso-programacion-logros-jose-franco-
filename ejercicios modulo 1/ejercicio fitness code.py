print("Fitness code")

peso=float(input("Cuanto pesas: "))
altura=float(input("Cuanto mides: "))

imc=round((peso / (altura ** 2)), 2)
print(f"Tu indice de masa corporal es {imc}")
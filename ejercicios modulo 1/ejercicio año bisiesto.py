print("Año bisiesto")

año= int(input("Que año quieres investigar: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto")
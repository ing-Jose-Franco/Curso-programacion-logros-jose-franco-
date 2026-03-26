print("Calcular los lados de un triangulo")

lado1 = float(input("Introduce el lado 1: "))
lado2 = float(input("Introduce el lado 2: "))
lado3 = float(input("Introduce el lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    
    if lado1 == lado2 == lado3:
        print("El triángulo es: Equilátero")
    
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es: Isósceles")
    
    else:
        print("El triángulo es: Escaleno")

else:
    print("Las longitudes no forman un triángulo válido.")
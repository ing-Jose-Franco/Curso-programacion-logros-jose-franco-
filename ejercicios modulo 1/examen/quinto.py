texto = input("Ingrese un texto: ")

palabras = texto.lower().split()
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        
        frecuencia[palabra] += 1
    else:
        
        frecuencia[palabra] = 1

print(frecuencia)
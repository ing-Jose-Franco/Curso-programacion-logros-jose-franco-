vocales= "aeiouáéíóú"
consonantes= "bcdfghjklmnñpqrstvwxyz"
texto= input("Pon una Frase: ")
num_vocales= 0
num_consonantes= 0
for letras in texto.lower():
        if letras in vocales:
            num_vocales += 1
        elif letras in consonantes:
            num_consonantes += 1
            
print(f"En {texto} tienes un total de {num_vocales} vocales y {num_consonantes} consonantes")
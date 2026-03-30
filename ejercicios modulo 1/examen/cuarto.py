def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

palabra= input("Elige una palabra: ")
resultado= es_palindromo(palabra)

print(f"{resultado}")
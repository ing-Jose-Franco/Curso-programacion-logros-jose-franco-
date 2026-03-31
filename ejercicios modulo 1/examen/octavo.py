def comunes(lista1, lista2):
    conjunto_lista2 = set(lista2)
    comunes = [elemento for elemento in lista1 if elemento in conjunto_lista2]
    return comunes

lista_pri = [1, 2, 3, 4, 5]
lista_seg = [4, 5, 6, 7, 8]

resultado = comunes(lista_pri, lista_seg)
print("Elementos comunes:", resultado)
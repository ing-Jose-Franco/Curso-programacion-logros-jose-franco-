print("Filtrado de catalogo")

productos=[("teclado", 25.50), ("pantalla", 80), ("mouse", 20), ("mousepad", 10)]
presupuesto=float(input("Cual es tu presupuesto: "))

for i in presupuesto:
    if i >= productos[0][1] and i >= productos[1][1] and i == productos[2][1] and i == productos[3][1]

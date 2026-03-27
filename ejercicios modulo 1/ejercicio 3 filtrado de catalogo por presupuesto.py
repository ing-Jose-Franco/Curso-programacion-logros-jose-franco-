print("Filtrado de catalogo")

catalogo = [
    ("Teclado", 25.50),
    ("Mouse", 15.00),
    ("Monitor", 150.00),
    ("Audífonos", 45.90),
    ("Alfombrilla", 10.00)]

presupuesto = float(input("Introduce tu presupuesto máximo: "))

productos_comprables = []

for producto, precio in catalogo:
    if precio <= presupuesto:
        productos_comprables.append(producto)
    
print("\nResultados")

if productos_comprables:
    print(f"Con {presupuesto}€ puedes comprar: {', '.join(productos_comprables)}")
else:
    print("Lo siento, nada en el catálogo se ajusta a tu presupuesto.")
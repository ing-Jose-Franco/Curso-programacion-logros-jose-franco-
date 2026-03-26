# 1. Creamos la lista de tuplas (Producto, Precio)
catalogo = [
    ("Teclado", 25.50),
    ("Mouse", 15.00),
    ("Monitor", 150.00),
    ("Audífonos", 45.90),
    ("Alfombrilla", 10.00)
]

# 2. Pedimos el presupuesto al usuario
presupuesto = float(input("Introduce tu presupuesto máximo: "))

# 3. Lista vacía para guardar lo que podemos comprar
productos_comprables = []

# 4. Bucle for para evaluar cada producto
for producto, precio in catalogo:
    # 5. Condicional para comparar precio vs presupuesto
    if precio <= presupuesto:
        productos_comprables.append(producto)

# Resultado final
print("\n--- Resultados ---")
if productos_comprables:
    print(f"Con {presupuesto}€ puedes comprar: {', '.join(productos_comprables)}")
else:
    print("Lo siento, nada en el catálogo se ajusta a tu presupuesto.")
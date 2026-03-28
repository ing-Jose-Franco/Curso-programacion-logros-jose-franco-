print("\nCajero Automatico")

opciones_validas = ("1", "2", "3", "4", "5", "6")
cesta = []
continuar = True
producto= []
precio= []

print("\nBIENVENIDO AL CAJERO AUTOMÁTICO")

while continuar:
    print("\n" + "="*30)
    print("   🛒 MENÚ DE LA CESTA 🛒")
    print("="*30)
    print("1. AGREGAR un nuevo elemento ✔️")
    print("2. MOSTRAR la cesta          🛍️")
    print("3. ELIMINAR un elemento      ❌")
    print("4. CALCULAR el total         💲")
    print("5. RENUNCIAR / Salir         👋")
    print("="*30)
    
    opcion = input("\nSeleccione una opción (1-5): ")

    if opcion in opciones_validas:
        
        if opcion =="1":
         print("\n" + "="*30)
         print("   🛒 AGREGAR producto 🛒")
         print("="*30)
         producto_nuevo=input(f"\nNombre del producto: ")
         while True:
            precio_nuevo=float(input(f"\nPrecio del producto: "))
            if precio_nuevo > 0:
                 break
            else:
                 print("¡EL MONTO NO PUEDE SER '0' O MENOR")

         producto.append(producto_nuevo)
         precio.append(precio_nuevo)

        elif opcion == "2":
         print("\n" + "="*30)
         print("   🛒 MOSTRAR Cesta 🛒")
         print("="*30)

         if not producto:
          print("\nNo tienes nada en tu cesta todavia.")
          input("\nPresiona Enter para continuar...")

         else:
            for i in range(len(producto)):
             productos = producto[i]
             precios = precio[i]

             print(f"{i + 1}. {productos}: {precios}$")
         input("\nPresiona Enter para continuar...")

        elif opcion == "3":
         print("\n" + "="*30)
         print("   🛒 ELIMINAR producto 🛒")
         print("="*30)

         if not producto:
          print("\nNo tienes nada en tu cesta para eliminar.")
          input("\nPresiona Enter para continuar...")

         else:
            for i in range(len(producto)):
             productos = producto[i]
             precios = precio[i]

             print(f"{i + 1}. {productos}: {precios}$")

            while True:
             try:
              eliminar = int(input("\nIngrese el número del producto a eliminar: "))
              if 1 <= eliminar <= len(producto):
               break
              else:
               print("Número inválido. Intente nuevamente.")
             except ValueError:
              print("Entrada no válida. Por favor, ingrese un número.")

            del producto[eliminar - 1]
            del precio[eliminar - 1]
            print("\nProducto eliminado exitosamente.")
            input("\nPresiona Enter para continuar...")
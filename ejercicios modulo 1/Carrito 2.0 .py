print("\nCarrito de compras")

opciones_validas = ("1", "2", "3", "4", "5")
continuar = True
seguir_agregando = True
producto= ["Teclado", "Mouse", "Monitor"]
precio= [40, 30, 180]
cesta= []

print("\nBIENVENIDO AL CARRITO DE COMPRAS")

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
         while seguir_agregando == False:
            seguir_agregando = True
         while seguir_agregando == True:
             for i in range(len(producto)):
               print(f"{i + 1}. {producto[i]}: {precio[i]}$")
             try:
               seleccion= int(input("\nSeleccione el número del producto que desea agregar: "))
               indice = seleccion - 1

               if 0 <= indice < len(producto):
                 for i in range(len(producto)):
                  if i == indice:
                   entrada= [producto[i], precio[i]]
                   cesta.append(entrada)
                   print(f"\n{producto[i]} ha sido agregado a tu cesta.")
                 input("\nPresiona Enter para continuar...")
                 seguir_agregando = False
                 break
               else:
                 print("Número inválido. Intente nuevamente.")
             except ValueError:
                print("\n¡ENTRADA NO VÁLIDA! POR FAVOR, INGRESA UN NÚMERO VÁLIDO.")

        elif opcion == "2":
         print("\n" + "="*30)
         print("   🛒 MOSTRAR Cesta 🛒")
         print("="*30)

         if not cesta:
          print("\nNo tienes nada en tu cesta todavia.")
          input("\nPresiona Enter para continuar...")

         else:
              n= 1
              for producto, precio in cesta:
                print(f"{n}. {producto}: {precio}$")
                n += 1

         input("\nPresiona Enter para continuar...")

        elif opcion == "3":
         print("\n" + "="*30)
         print("   🛒 ELIMINAR producto 🛒")
         print("="*30)

         if not cesta:
          print("\nNo tienes nada en tu cesta para eliminar.")
          input("\nPresiona Enter para continuar...")

         else:
            for i in range(len(cesta)):
             producto = cesta[i][0]
             precio = cesta[i][1]

             print(f"{i + 1}. {producto}: {precio}$")

            while True:
             try:
              eliminar = int(input("\nIngrese el número del producto a eliminar: "))
              if 1 <= eliminar <= len(cesta):
               break
              else:
               print("Número inválido. Intente nuevamente.")
             except ValueError:
              print("Entrada no válida. Por favor, ingrese un número.")

            del cesta[eliminar - 1]
            print("\nProducto eliminado exitosamente.")
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
         print("\n" + "="*30)
         print("   🛒 CALCULAR total 🛒")
         print("="*30)
         total= 0
         if not cesta:
          print("\nNo tienes nada en tu cesta para calcular el total.")
          input("\nPresiona Enter para continuar...")

         else:
            for i in range(len(cesta)):
             total += cesta[i][1]
            print(f"\nEl total de tu cesta es: {total}$")
            input("\nPresiona Enter para continuar...")
        elif opcion == "5":
         print("\n¡Gracias por usar nuestro servicio! ¡Hasta luego!")
         continuar = False
         
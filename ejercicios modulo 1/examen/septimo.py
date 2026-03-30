contactos = {}
    
while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Listar todos los contactos")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            nombre = input("Introduce el nombre: ").capitalize()
            telefono = input("Introduce el número de teléfono: ")
            contactos[nombre] = telefono
            print(f"¡Contacto {nombre} guardado con éxito!")

            input("Presiona Enter para continuar...")  # Pausa para que el usuario vea el mensaje

        elif opcion == "2":
            nombre = input("Nombre a buscar: ").capitalize()
            if nombre in contactos:
                print(f"El teléfono de {nombre} es: {contactos[nombre]}")
                input("Presiona Enter para continuar...")  # Pausa para que el usuario vea el mensaje
            else:
                print("Ese contacto no existe en la agenda.")
                input("Presiona Enter para continuar...")  # Pausa para que el usuario vea el mensaje

        elif opcion == "3":
            if not contactos:
                print("La agenda está vacía.")
                input("Presiona Enter para continuar...")  # Pausa para que el usuario vea el mensaje
            else:
                print("\n--- Lista de Contactos ---")
                for nombre, telefono in contactos.items():
                    print(f"Nombre: {nombre} | Teléfono: {telefono}")
                input("Presiona Enter para continuar...")  # Pausa para que el usuario vea cada contacto

        elif opcion == "4":
            print("Saliendo de la agenda... ¡Hasta luego!")
            break  # Rompe el bucle while para finalizar el programa

        else:
            print("Opción no válida, por favor intenta de nuevo.")
            input("Presiona Enter para continuar...")  # Pausa para que el usuario vea el mensaje
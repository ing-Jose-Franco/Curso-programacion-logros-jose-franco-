def juego_aventura():
    print("\nBIENVENIDO A DARK SOULS")
    print("\nDespiertas en una celda mal holiente y oscura con solo una rejilla que te encierra, una ventana en el techo alumbrando tenuemente")
    print("\nTal parece que la rejilla que te encierra se encuentra debil y oxidada, tambien hay parece que hay un agujero en la esquina de tu celda que conecta\nhacia abajo, pero mientras escuchas que alguien se acerca desde el techo a la ventana.")
    
    # NIVEL 1: Tres opciones (Mínimo 3 opciones solicitado)
    eleccion1 = input("\n¿Qué decides hacer? [GOLPEAR LA REJILLA], [ESPERAR] o [ESCAPAR POR EL AGUJERO]: ").lower().strip()

    if eleccion1 == "golpear la rejilla":
        print("\nGolpeas la rejilla con los vestijios de fuerza que todavia te quedan, ¡FUNCIONA! la reja a caido y eres libre, huyes rapidamente pero hay dos caminos,\na tu derecha escuchaste pisadas cercanas y sonidos de sollozos, a tu izquierda escuchaste un rugido al final del camino")
        # NIVEL 2
        eleccion2 = input("\n¿Prefieres ir por la [DERECHA] o por la [IZQUIERDA]? ").lower().strip()
        
        if eleccion2 == "derecha":
            print("\nCaminas ")
            # NIVEL 3: Tres opciones
            eleccion3 = input("El camino se divide. ¿Hacia dónde vas? [IZQUIERDA], [DERECHA] o [ARRIBA]: ").lower().strip()
            
            if eleccion3 == "izquierda":
                print("\nLlegas a la sala de servidores. Está llena de cables sueltos con electricidad.")
                # NIVEL 4
                eleccion4 = input("¿Intentas [SALTAR] los cables o [CORTAR] la energía? ").lower().strip()
                
                if eleccion4 == "saltar":
                    print("\n¡Éxito! Llegas a la terminal central.")
                    # NIVEL 5: Tres opciones
                    eleccion5 = input("La terminal pide un comando: [DESBLOQUEAR], [BORRAR DATOS] o [AUTODESTRUCCIÓN]: ").lower().strip()
                    
                    if eleccion5 == "desbloquear":
                        print("\nLas puertas del hangar se abren.")
                        # NIVEL 6
                        eleccion6 = input("Ves una nave de escape. ¿[ENTRAR] o [BUSCAR SUPERVIVIENTES]? ").lower().strip()
                        if eleccion6 == "entrar":
                            print("\nFINAL: Logras escapar de la base antes de que colapse. ¡Eres libre!")
                        elif eleccion6 == "buscar supervivientes":
                            print("\nFINAL: Encuentras a un robot de carga. Juntos escapan en la última nave.")
                        else:
                            print("Opción no válida. El sistema colapsa mientras dudas.")
                    else:
                        print("Comando erróneo. Los sistemas de seguridad te neutralizan.")
                else:
                    print("Cortaste el cable equivocado. La sala explota.")
            else:
                print("Te pierdes en el laberinto de ventilación. El oxígeno se agota.")

        elif eleccion2 == "pasillo principal":
            print("\nUn dron de seguridad te detecta y te apunta con un láser.")
            # NIVEL 3
            eleccion3 = input("¿Qué haces? [CORRER], [ESCONDERSE] o [NEGOCIAR]: ").lower().strip()
            if eleccion3 == "negociar":
                print("\nEl dron reconoce tu rango de ingeniero. Te permite pasar al Laboratorio de Química.")
                # NIVEL 4
                eleccion4 = input("En la mesa hay una fórmula incompleta. ¿La [COMPLETAR] o la [IGNORAR]? ").lower().strip()
                if eleccion4 == "completar":
                    print("\nCreas un gas que neutraliza a las criaturas de la base.")
                    # NIVEL 5
                    eleccion5 = input("¿Vas al [MUELLE DE CARGA] o a la [SALA DE COMUNICACIONES]? ").lower().strip()
                    if eleccion5 == "muelle de carga":
                        # NIVEL 6
                        eleccion6 = input("Hay un traje espacial. ¿[PONERSE TRAJE] o [USCAR VEHÍCULO]? ").lower().strip()
                        if eleccion6 == "ponerse traje":
                            print("\nFINAL: Caminas por la superficie lunar hasta la base aliada. ¡Salvado!")
                        else:
                            print("El vehículo no tiene combustible. Estás atrapado.")
                    else:
                        print("La señal está bloqueada. Los enemigos te encuentran.")
                else:
                    print("Sin el gas, las criaturas te rodean rápidamente.")
            else:
                print("El dron no acepta esa acción y abre fuego.")

    elif eleccion1 == "forzar escotilla":
        print("\nLa puerta se abre violentamente y caes a un nivel inferior inundado.")
        # NIVEL 2
        eleccion2 = input("El agua sube. ¿Intentas [NADAR] hacia la luz o [TREPAR] por las tuberías? ").lower().strip()
        if eleccion2 == "trepar":
            print("\nLlegas a la armería. Todo está bajo llave, excepto un lanzallamas.")
            # NIVEL 3: Tres opciones
            eleccion3 = input("Escuchas rugidos. ¿Qué buscas primero? [MUNICIÓN], [MAPA] o [LINTERNA]: ").lower().strip()
            if eleccion3 == "mapa":
                print("\nEl mapa muestra una salida de emergencia secreta.")
                # NIVEL 4
                eleccion4 = input("Para llegar debes pasar por el nido. ¿[SIGILO] o [ATAQUE FRONTAL]? ").lower().strip()
                if eleccion4 == "sigilo":
                    print("\nPasas sin despertar a las criaturas. Llegas a la puerta secreta.")
                    # NIVEL 5
                    eleccion5 = input("La puerta tiene un código. ¿Pruebas [0000], [1234] o [9999]? ").lower().strip()
                    if eleccion5 == "1234":
                        print("\n¡Abierta! Es un túnel que lleva directamente a la superficie.")
                        # NIVEL 6
                        eleccion6 = input("Ves un rover lunar. ¿[CONDUCIR] o [CAMINAR]? ").lower().strip()
                        if eleccion6 == "conducir":
                            print("\nFINAL: Conduces hasta el amanecer lunar. Estás a salvo.")
                        else:
                            print("El camino es demasiado largo. Te quedas sin aire.")
                    else:
                        print("Código incorrecto. La alarma atrae a la horda.")
                else:
                    print("El lanzallamas se encalla. No fue una buena idea.")
            else:
                print("Sin el mapa, das vueltas en círculos hasta que es tarde.")
        else:
            print("El agua está demasiado fría y pierdes las fuerzas.")

    elif eleccion1 == "escapar por el agujero":
        print("\nNo mediste correctamente la altura en la que estaba el agujero a comparacion de piso de abajo y te rompiste las piernas al contacto con el piso\nel piso de abajo esta en total oscuridad y solo escuchas No-muertos justo a tu lado")
        # Aquí continuarían otros caminos siguiendo la misma lógica...
        print("\¡HAS MUERTO! fuiste devorado en la profundidades del recinto")
        
    else:
        print("\nOpción no válida.")

juego_aventura()
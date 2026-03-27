print("\nBIENVENIDO A DARK SOULS")
print("\nDespiertas en una celda mal holiente y oscura con solo una rejilla que te encierra, una ventana en el techo alumbrando tenuemente")
print("\nTal parece que la rejilla que te encierra se encuentra debil y oxidada, tambien hay parece que hay un agujero en la esquina de tu celda que conecta\nhacia abajo, pero mientras escuchas que alguien se acerca desde el techo a la ventana.")
    
eleccion1 = input("\n¿Qué decides hacer? [GOLPEAR LA REJILLA], [ESPERAR] o [ESCAPAR POR EL AGUJERO]: ").lower().strip()

if eleccion1 == "golpear la rejilla":
        print("\nGolpeas la rejilla con los vestijios de fuerza que todavia te quedan, ¡FUNCIONA! la reja a caido y eres libre, huyes rapidamente pero hay dos caminos,\na tu derecha escuchaste pisadas cercanas y sonidos de sollozos, a tu izquierda escuchaste un rugido al final del camino")
 
        eleccion2 = input("\n¿Prefieres ir por la [DERECHA] o por la [IZQUIERDA]? ").lower().strip()
        
        if eleccion2 == "derecha":
            print("\nCaminas entre pasillos oscuros y escuchas una voz al final del pasillo, parece ser un caballero agonizando")
            
            eleccion3 = input("¿Que deseas hacer? [HABLAR], [ATACARLE] o [ROBARLE]: ").lower().strip()
            
            if eleccion3 == "hablar":
                print("\nEL CABALLERO:'(Nota que eres cosciente)Por los santos de Lordran, pensaba que eras otro No-Muerto mas en busca de devorarme, lamento la confusion\nMe llamo Oscar De Astora, desperte aqui tambien por alguna razon, trate de buscar alguien desde los techos del recinto pero solo vi celdas vacias\nahora estoy mal herido y al borde de la muerte por la cantidad de No-Muertos con los que combati antes de estar aqui\nse ve que eres fuerte, toma mi armadura, mi armas, mis pociones y esta llave, es para escapar de este recinto, pero ten cuidado\nantes de salir te encontraras con el jefe del recinto, solo lo vi de lejos pero parece ser muy fuerte, te lo encomiendo'")
                print("\nOSCAR A MUERTO")
                print("\n'Haz Recibido [LA ARMADURA CABALLERO DE ASTORA], [EL ESPADON CLAYMORE], [ESTUS/POCIONES], [LLAVE DEL RECINTO]'")

                print("\nCaminas en la direccion que Oscar te indico en busca de la salida. Ves una puerta al final de una habitacion gigantesca, caminas para llegar a la puerta y ¡PUM!\nUna bestia con la forma de un demonio con un mazo cae desde el techo de esa habitacion bloqueando el camino, tiene un grabado en el pecho que dice 'CARCELERO'")
                
                eleccion4 = input("\n¿Que piensas hacer? [ESPERAR Y ATACAR] o [ATACAR ANTES]: ").lower().strip()
                
                if eleccion4 == "esperar y atacar":
                    print("\nLa bestia parece no pensar y atacar al instante de verte, gracias a que esperaste lograste evadir su ataque y contraatacas justo en su brazo\nLa bestia ya no puede usar su brazo derecho para su mazo, te golpea con su otro brazo para alejarte de el")
                    
                    eleccion5 = input("\nVuelas unos pocos metros lejos de el, quedas malherido por el golpe, ¿Que haces? [ATACARLE RAPIDO], [ESPERAR Y ATACAR] o [USAR POCION]: ").lower().strip()
                    
                    if eleccion5 == "usar pocion":
                        print("\n¡FUNCIONA! Te sientes revitalizado y con tus fuerzas devuelta, la bestia viene corriendo sin su mazo en tu direccion, te engaña con un golpe falso\n y logra encajarte un golpe que pudo ser letal, pero parece que la bestia se canso luego de ese golpe")
                        
                        eleccion6 = input("¿Que haras? ¿[ATACAR CABEZA] o [ATACAR PECHO]?: ").lower().strip()
                        if eleccion6 == "atacar cabeza":
                            print("\nFINAL: Le cortas la cabeza a la bestia, su cuerpo cae sin vida y la victoria es tuya ¡Eres libre!")
                        elif eleccion6 == "atacar pecho":
                            print("\nFINAL: ¡HAS MUERTO! Le atraviezas el pecho a la bestia, ella ruge de dolor y te da un golpe con las ultimas fuerzas que le quedan, caes en el piso inconsciente y sin fuerzas para respirar")
                        else:
                            print("¡HAS MUERTO! Parece que te quedaste en shock y la bestia lo noto, recupero su aliento y corrio hacia ti, te asesto un golpe con todas sus fuerzas, volaste y quedaste como una pintura rupestre en el techo")
                    else:
                        print("¡HAS MUERTO! La bestia ahora que no puede usar su mazo se volvio mas precavida, decidio correr y engañarte con un golpe falso para luego darte uno de verdad, no pudiste resistir el impacto.")
                else:
                    print("\n¡HAS MUERTO! La bestia ataca al instante con su mazo mientras tu tratas de atacarle, su fuerza es descomunal, terminas despedazado por su golpe")
            else:
                print("\n¡HAS MUERTO! El caballero nota tus intenciones mientras te acercas, lanza un cuchillo rapidamente con las pocas fuerzas que le quedan y te corta la garganta")

        elif eleccion2 == "izquierda":
            print("\nCaminas por unos pasillos totalmente a ciegas y ves una luz atraves de una puerta")
            
            eleccion3 = input("¿Qué haces? [PASAR], [VOLVER] o [INVESTIGAR]: ").lower().strip()
            if eleccion3 == "pasar":
                print("\nAtraviesas la puerta y la cierras detras de ti, pero ahora estas en una habitacion gigantesca con cadaveres de guerreros alrededor, hay una puerta al final que parece ser la salida")
                
                eleccion4 = input("\n¿Que haces? [BUSCAR ARMA] o [SALIR]: ").lower().strip()
                if eleccion4 == "buscar arma":
                    print("\nEntre las armas destruidas de los cadaveres encuentras una [ESPADA CORTA], en el instante que haces ruido al recogerla se escucha un estruendo en el camino hacia la puerta\nUna bestia con forma de demonio y un mazo gigante cayo desde el techo, te esta mirando fijamente.")
                    
                    eleccion5 = input("¿Que haces? [HABLARLE A LA BESTIA] o [ESPERAR]: ").lower().strip()
                    if eleccion5 == "esperar":
                        
                        eleccion6 = input("\nLa bestia corre en tu direccion listo para asestarte un golpe devastador. ¿Que haces? [ESQUIVAR] [RESISTIR]").lower().strip()
                        if eleccion6 == "esquivar":
                            print("\nFINAL:¡HAS MUERTO! Logras esquivar el golpe de la bestia por milimetros, atacas con tu [ESPADA CORTA], pero la espada no es lo suficiente como para hacerle daño, la bestia te toma por tus brazos y te estrella contra el piso.")
                        else:
                            print("¡HAS MUERTO! Tratas de resistir el golpe pero su fuerza es tan descomunal que sientes como parte todos tus huesos con el mazo, vuelas como una pluma")
                    else:
                        print("¡HAS MUERTO! Decidiste tratar de comunicarte con la bestia, parece no entender nada de lo que le dices asi que corre en tu direccion y de un golpe te hace atravesar la pared detras de ti")
                else:
                    print("\n¡HAS MUERTO! Te acercas a la puerta y notas que esta bloqueada, de la nada sientes que algo gigantesco cayo detras de ti, no te da tiempo a voltear cuando fuiste despedazado por un golpe descomunal")
            elif eleccion3 == "investigar":
                print("\n¡HAS MUERTO! Te pones a ojear antes de abrir la puerta para estar seguro y no te das cuenta de los No-Muertos que te venian siguiendo, eres arrastrado por ellos a la oscuridad del recinto")
            else:
                print("\n¡HAS MUERTO! Te devuelves por tus pasos, pero al estar tan oscuro te pierdes en los pasillos, terminas sumido en la oscuridad del recinto")

elif eleccion1 == "esperar":
        print("\nDecides esperar en tu celda, el sonido del techo se acerca hasta al punto que puedes divisar a alguien asomandose a tu ventada")
        
        eleccion2 = input("\n¿Que haces? [ESCONDERSE] o [LLAMAR]: ").lower().strip()
        if eleccion2 == "llamar":
            print("\nLa silueta nota tu pescencia y acerca mas a la ventana, parece ser un caballero, con su espada rompe las barras de tu ventana\n entra a tu celda desde el techo")
            print("\nEL CABALLERO: Por los santos de Lordran, pensaba que eras otro No-Muerto mas encerrado aqui, lamento la confusion\nMe llamo Oscar De Astora, desperte aqui tambien por alguna razon, trate de buscar alguien desde los techos del recinto pero solo vi celdas vacias\nhasta que encontre la tuya, me alegra ver a alguien consciente aqui, tratemos de salir juntos")
            
            eleccion3 = input("\n¿Que decides? [ESCAPAR JUNTOS] [ROBARLE]: ").lower().strip()
            if eleccion3 == "escapar juntos":
                print("\nOscar: Buena eleccion mi decrepito amigo, salgamos de aqui.\n\nSalen de tu celda mientras atraviesan pasillos oscuros siguiendo una tenue luz. \n\nTu solo sigues a Oscar")
                print("\nLlegan a una sala gigantesca con una puerta al final.\n\nOscar: Esa es la puerta para salir de aqui, yo tengo la llave pero antes de llegar a esa puerta hay que enfrentarnos a eso.\n\nTu: ¿A que? \n\n ¡PUM! miras a enfrente y vez a una bestia con forma de demonio y un mazo gigante en sus manos\n\nOscar: Esa cosa...El es el Carcelero.")
                eleccion4 = input("\n¿Que haces? [ENCONTRAR ARMA] o [SEGUIR A OSCAR]").lower().strip()
                if eleccion4 == "encontrar arma":
                    print("\nEncuentras una [ESPADA CORTA] entre los cadaveres que habian en la sala, Oscar se lanza en contra de la bestia")
                    
                    eleccion5 = input("¿Que haces? [SEGUIR A OSCAR] o [SEGUIR BUSCANDO]").lower().strip()
                    if eleccion5 == "seguir a oscar":
                        print("\nSigues a Oscar a la pelea, la bestia ve que son dos enemigos asi que tiene su atencion dividida, ataca al enemigo mas cercano.\n\n La pelea se alarga, todos estan cansados, estas cara a cara con la bestia mientras que Oscar esta apunto de atacarla por la espalda\nPero la bestia lo noto y esta mirando hacia atras apunto de voltearse para atacarle")
                
                        eleccion6 = input("¿Que haces? [AVISARLE] o [LANZAR TU ESPADA]: ").lower().strip()
                        if eleccion6 == "lanzar tu espada":
                            print("\nFINAL: Lanzas la espada directo a los ojos de la bestia...\n\n ¡DAS EN EL BLANCO! \n\nLa Bestia grita de dolor y queda totalmente ciega de un ojo, Oscar ataca desde su punto ciego y cercena su cabeza de su torso.\n\n ¡VICTORIA! La bestia cae muerta en el suelo, Oscar y tu han escapado.")
                        else:
                            print("¡HAS MUERTO! Gritas con todas tus fuerzas para avisarle a Oscar las intenciones de la bestia, pero por el ruido la bestia posa toda su atencion en ti y te aplasta con su mazo apenas empiezas a gritar")
                    else:
                        print("¡HAS MUERTO! Sigues buscando otra arma o algun equipamiento, alzas la mirada por un momento y solo ves a oscar desangrandose en el piso, la bestia viene hacia ti.")
                else:
                    print("¡HAS MUERTO! Tratas de seguir a Oscar sin un arma, la bestia nota que no tienes un arma asi que enfoca toda su atencion en Oscar\nOscar no es rival para la bestia, sale volando de un golpe y el siguiente fuiste tu")
            else:
                print("\n¡HAS MUERTO! Tratas de robarle Oscar mientras esta distraido pero se da cuenta\n\nOSCAR: Parece que eres cosciente pero no inteligente.\n\nOscar te atraviesa con su espada y se va de tu celda")
        else:
            print("\n¡HAS MUERTO! Te escondes detras de un barril en la esquina de tu celda, la silueta se asoma a tu celda y al no ver nada se va\nduras mucho tiempo sin encontrar una forma de salir y mueres deshidratado")

elif eleccion1 == "escapar por el agujero":
        print("\nNo mediste correctamente la altura en la que estaba el agujero a comparacion de piso de abajo y te rompiste las piernas al contacto con el piso\nel piso de abajo esta en total oscuridad y solo escuchas No-muertos justo a tu lado")
        # Aquí continuarían otros caminos siguiendo la misma lógica...
        print("\n¡HAS MUERTO! fuiste devorado en la profundidades del recinto")
        
else:
        print("\nOpción no válida.")


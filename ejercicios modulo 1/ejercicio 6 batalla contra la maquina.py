print("\nBatalla contra la maquina")

import random

vida = [100, 100]

daños = (30, 15, 5)

print("\n    INICIO")

while vida[0] > 0 and vida[1] > 0:
    print(f"\n Tu Vida: {vida[0]} | Vida Máquina: {vida[1]}")

    print("\nElige tu ataque: (1) Fuerte, (2) Normal, (3) Débil")
    
    eleccion = input("\nTu turno: ")

    if eleccion == "1":
        golpe = daños[0]
        print(f"\nCausas {golpe} de daño.")
    elif eleccion == "2":
        golpe = daños[1]
        print(f"\nCausas {golpe} de daño.")
    else:
        golpe = daños[2]
        print(f"\nCausas {golpe} de daño.")
        
    vida[1] -= golpe
    
    golpe_maquina = random.choice(daños)

    vida[0] -= golpe_maquina

    print(f"\nLa máquina te da un golpe de {golpe_maquina} de daño.")

# --- Resultado Final ---
print("\nEL COMBATE HA TERMINADO")
if vida[0] > 0:
    print(f"\nVICTORIA! Te sobraron {vida[0]} puntos de vida")
else:
    print("\nHAS SIDO DERROTADO")
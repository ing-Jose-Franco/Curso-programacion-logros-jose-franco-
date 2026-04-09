import random

class Personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def recibir_dano(self, cantidad):
        self.salud -= cantidad
        # Si la salud baja de 0, la reseteamos a 0
        if self.salud < 0:
            self.salud = 0
        print(f"{self.nombre} recibe {cantidad} de daño. Salud: {self.salud}")

class Guerrero(Personaje):
    def ataque_pesado(self, objetivo):
        # 50% de probabilidad (1: éxito, 0: falla)
        if random.randint(0, 1) == 1:
            print(f"¡{self.nombre} lanza un ataque pesado crítico!")
            objetivo.recibir_dano(self.ataque * 2)
        else:
            print(f"¡{self.nombre} falló el ataque pesado!")

class Curandero(Personaje):
    def accion_turno(self, objetivo):
        # Lógica de curación o ataque
        if self.salud < 20:
            self.salud += 15
            print(f"{self.nombre} se cura. Salud actual: {self.salud}")
        else:
            print(f"{self.nombre} ataca.")
            objetivo.recibir_dano(self.ataque)

# --- Ejecución ---

# Instanciar personajes
g = Guerrero("Draven", 100, 15)
c = Curandero("Soraka", 80, 10)

# Bucle de batalla
while g.salud > 0 and c.salud > 0:
    g.ataque_pesado(c)
    
    if c.salud > 0:
        c.accion_turno(g)
    
    print("-" * 25)

# Resultado final
if g.salud > 0:
    print(f"🏆 ¡El ganador es {g.nombre}!")
else:
    print(f"🏆 ¡El ganador es {c.nombre}!")
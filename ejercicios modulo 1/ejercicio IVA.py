print("Calculo de IVA")
precio_base= 325
IVA= 21

IVA_aplicado= (precio_base * IVA) / 100
precio_con_IVA= precio_base + IVA_aplicado

print(f"Ese producto vale {precio_con_IVA} con el IVA incluido")
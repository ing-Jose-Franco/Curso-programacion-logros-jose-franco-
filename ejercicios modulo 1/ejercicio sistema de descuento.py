print("Sistema de descuentos")
harina= 425.35
descuento= 15
cantidad= float(input("La harina esta a 425.35bs, cuantas deseas comprar?: "))

resultado= round((cantidad * harina), 2)

if resultado > 1000:
    descuento_operacion= (resultado * descuento) / 100
    descuento_aplicado= round((resultado - descuento_operacion), 2)
    print(f"El monto a pagar es {descuento_aplicado}bs con descuento aplicado")

else:
    print(f"El monto a pagar es {resultado}bs sin el descuento por compra mayor a 1000")
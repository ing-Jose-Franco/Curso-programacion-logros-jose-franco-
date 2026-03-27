print("\nVerificador de contraseñas")

rango_longitud = (8, 20)
caracteres_especiales = ("!", "@", "#", "$", "%", "*", ".")

contraseñas= input("Introduce contraseñas separadas por comas (ej: 123!, admin., CarlitosElPro777#): ")
lista_passwords = contraseñas.split(",")

contraseñas_seguras = []

for contra in lista_passwords:
    contra = contra.strip()
    largo = len(contra)
    
    tiene_especial = False
    for especial in caracteres_especiales:
        if especial in contra:
            tiene_especial = True
            break
            
    if (largo >= rango_longitud[0] and largo <= rango_longitud[1]) and tiene_especial:
        contraseñas_seguras.append(contra)
    else:
        print(f"La contraseña '{contra}' ha sido rechazada.")

print("\n--- Registro de Contraseñas Seguras ---")
if  contraseñas_seguras:
    print(f"Válidas: {contraseñas_seguras}")
else:
    print("Ninguna contraseña cumplió con los estándares de seguridad.")
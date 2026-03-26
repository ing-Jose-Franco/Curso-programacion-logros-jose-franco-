print("Creador de nombre de usuarios")

tupla=("admin", "root")
intentos_rechazados=[]
usuario=input("Que nombre de usuario deseas usar: ")
while usuario in tupla:
    if usuario in tupla:
        intentos_rechazados.append(usuario)
        print(f"El usuario {usuario} no puede ser usado, por favor introduzca otro")
        break
else:
        print("Usuario accesible")
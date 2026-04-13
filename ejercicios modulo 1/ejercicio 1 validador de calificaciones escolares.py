print("Validador de calificaciones")

nota1=float(input("Dime la nota 1: "))
nota2=float(input("Dime la nota 2: "))
nota3=float(input("Dime la nota 3: "))
nota4=float(input("Dime la nota 4: "))

lista1= [nota1, nota2, nota3, nota4

tupla= (6.0, 10.0

for i in lista1:
    if i >= tupla[0] and i <= tupla[1]:
        print(f"Tu nota es {i} y estas aprobado")
    elif i < tupla[0] and i > 0:
        print(f"Tu nota es {i} y estas reprobado")
    else:
        print("ERROR")
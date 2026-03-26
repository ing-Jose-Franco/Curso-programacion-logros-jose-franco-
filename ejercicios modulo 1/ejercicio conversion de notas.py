print("Conversion de notas")

nota=float(input("\nCuantos puntos saco el alumno?: "))

if nota >= 90 and nota <= 100:
    print(f"El estudiante saco 'A'")
elif nota >= 80 and nota <= 89:
    print(f"El estudiante saco 'B'")
elif nota >= 70 and nota <= 79:
    print(f"El estudiante saco 'C'")
elif nota >= 60 and nota <= 69:
    print(f"El estudiante saco 'D'")
elif nota >= 0 and nota <= 59:
    print(f"El estudiante saco 'F'")
else:
    print(f"ERROR")
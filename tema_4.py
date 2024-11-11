# Crear una lista de 9 semestres
semestres = [[] for _ in range(9)]

# Llenar los semestres con materias
for i in range(9):
    print(f"\nIngresando materias para el semestre {i+1}:")
    while True:
        nombre = input("Nombre de la materia (o 'salir' para terminar): ").strip()
        
        if nombre.lower() == "salir":
            break
        
        # Validar que el nombre no esté vacío
        if nombre == "":
            print("Nombre de la materia no válido. Inténtalo de nuevo.")
            continue

        # Validar que la calificación sea un número y esté en el rango 0-10
        calificacion_input = input("Calificación de la materia: ").strip()
        
        # Verificar que la calificación sea numérica
        if calificacion_input.replace(".", "", 1).isdigit():
            calificacion = float(calificacion_input)
        else:
            print("Calificación inválida. Debe ser un número.")
            continue

        if not (0 <= calificacion <= 10):
            print("Calificación fuera del rango permitido (0-10). Inténtalo de nuevo.")
            continue

        # Determinar el estado de la materia (A o N/A)
        estado = "A" if calificacion >= 7 else "N/A"
        
        # Agregar la materia al semestre actual
        materia = [nombre, calificacion, estado]
        semestres[i].append(materia)

# Imprimir los datos en la consola y hacer un recuento de materias por semestre
for i, semestre in enumerate(semestres, start=1):
    print(f"\nSemestre {i}:")
    if not semestre:
        print("  No hay materias registradas.")
    else:
        print(f"  Total de materias: {len(semestre)}")
        for materia in semestre:
            print(f"  Materia: {materia[0]}, Calificación: {materia[1]}, Estado: {materia[2]}")

# Preguntar si se quiere consultar un semestre específico
consulta_semestre = input("\n¿Te gustaría consultar un semestre específico? (sí/no): ").strip().lower()

if consulta_semestre == "sí":
    num_semestre_input = input("Ingresa el número del semestre (1-9): ").strip()
    
    # Verificar si el número de semestre es un entero válido
    if num_semestre_input.isdigit():
        num_semestre = int(num_semestre_input) - 1
        if 0 <= num_semestre < 9:
            print(f"\nSemestre {num_semestre + 1}:")
            if not semestres[num_semestre]:
                print("  No hay materias registradas.")
            else:
                for materia in semestres[num_semestre]:
                    print(f"  Materia: {materia[0]}, Calificación: {materia[1]}, Estado: {materia[2]}")
                
                # Preguntar si quiere buscar una materia en ese semestre
                consulta_materia = input("\n¿Te gustaría buscar una materia en este semestre? (sí/no): ").strip().lower()
                
                if consulta_materia == "sí":
                    nombre_materia = input("Ingresa el nombre de la materia: ").strip()
                    encontrado = False
                    for materia in semestres[num_semestre]:
                        if materia[0].lower() == nombre_materia.lower():
                            print(f"  Materia encontrada: {materia[0]}, Calificación: {materia[1]}, Estado: {materia[2]}")
                            encontrado = True
                            break
                    if not encontrado:
                        print("  La materia no fue encontrada en este semestre.")
        else:
            print("Número de semestre fuera de rango.")
    else:
        print("Entrada inválida, debes ingresar un número entero.")
else:
    print("Consulta finalizada.")

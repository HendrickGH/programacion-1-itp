# Crear una lista vacía de 9 semestres
semestres = [list() for _ in range(9)]

# Llenar los semestres con materias
for i in range(9):
    print(f"\nIngresando materias para el semestre {i+1}:")
    
    while len(semestres[i]) < 6:
        nombre = input("Nombre de la materia (o 'salir' para terminar el ingreso de este semestre): ").strip()
        
        if nombre.lower() == "salir":
            break
        
        # Validar que el nombre no esté vacío
        if nombre == "":
            print("Nombre de la materia no válido. Inténtalo de nuevo.")
            continue
        
        # Pedir calificación y validar que sea un número en el rango de 0 a 10
        while True:
            calificacion_input = input("Calificación de la materia: ").strip()
            
            # Verificar que la calificación sea numérica
            es_numero = calificacion_input.replace(".", "", 1).isdigit()
            calificacion = float(calificacion_input) if es_numero else None

            if es_numero and 0 <= calificacion <= 10:
                break
            else:
                print("Calificación inválida. Debe ser un número entre 0 y 10. Inténtalo de nuevo.")

        # Determinar el estado de la materia (A o N/A)
        estado = "A" if calificacion >= 7 else "N/A"
        
        # Agregar la materia al semestre actual
        materia = [nombre, calificacion, estado]
        semestres[i] = semestres[i] + [materia]  # Añadir la materia como nueva lista sin 'append'
        
        # Si se alcanzan 6 materias en el semestre, avanzar automáticamente
        if len(semestres[i]) == 6:
            print(f"Se ha alcanzado el límite de 6 materias en el semestre {i+1}. Pasando al próximo semestre...")
            break

# Imprimir los datos en la consola y hacer un recuento de materias por semestre
for i, semestre in enumerate(semestres, start=1):
    print(f"\nSemestre {i}:")
    if not semestre:
        print("  No hay materias registradas.")
    else:
        print(f"  Total de materias: {len(semestre)}")
        for materia in semestre:
            print(f"  Materia: {materia[0]}, Calificación: {materia[1]}, Estado: {materia[2]}")

# Consulta de semestres específicos
while True:
    consulta_semestre = input("\n¿Te gustaría consultar un semestre específico? (si/no): ").strip().lower()
    
    if consulta_semestre != "si":
        print("Consulta finalizada.")
        break

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
                
                # Bucle para buscar varias materias en el mismo semestre
                while True:
                    nombre_materia = input("\nIngresa el nombre de la materia que quieres buscar (o 'salir' para salir): ").strip()
                    
                    if nombre_materia.lower() == "salir":
                        print("Saliendo de la búsqueda de materia...")
                        break
                    
                    encontrado = False
                    for materia in semestres[num_semestre]:
                        if materia[0].lower() == nombre_materia.lower():
                            print(f"  Materia encontrada: {materia[0]}, Calificación: {materia[1]}, Estado: {materia[2]}")
                            encontrado = True
                            break
                    
                    if encontrado:
                        # Preguntar si quiere buscar otra materia en el mismo semestre
                        otra_materia = input("\n¿Te gustaría buscar otra materia en este semestre? (si/no): ").strip().lower()
                        if otra_materia != "si":
                            break
                    else:
                        print("  La materia no fue encontrada en este semestre. Inténtalo de nuevo o escribe 'salir' para salir.")
        else:
            print("Número de semestre fuera de rango.")
    else:
        print("Entrada inválida, debes ingresar un número entero.")

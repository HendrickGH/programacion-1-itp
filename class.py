arreglo_principal = [[], [], [], [], []]

for i in range(len(arreglo_principal)): 
    subarreglo = [0] * (i + 1)
    print("Rellenando la primera posición: ", subarreglo)
    for j in range(i + 1): 
        subarreglo[j] = j + 1 
        print("subarreglo: ", subarreglo)
    arreglo_principal[i] = subarreglo 



print(arreglo_principal)
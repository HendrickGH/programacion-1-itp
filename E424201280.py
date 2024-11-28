# 24201280 Hendrick Adelaido Galarza Hernandez 

arreglo = [[180,775,300],[560,150,650],[50,500,50],[200,800,250]]


for i in range(len(arreglo)):
    for j in range(len(arreglo[i])):
        # punto numero 1 hecho
        if (arreglo[i][j] > 500):
            arreglo[i][j] = 400

for i in range(2, len(arreglo)):
    for j in range(1, len(arreglo[i])):
        # punto numero 2 hecho
        if(arreglo[i][j] < 400):
            arreglo[i][j] = 400

producto = 0

while (True):
    producto = int(input("Ingrese el numero de producto (1-4) que le interesa: "))
    # punto numero 3, validando la entrada de datos
    if not (producto < 0 or producto > 4):
        break

for i in range(producto - 1, len(arreglo)):
    # punto numero 3, a partir del producto seleccionado y unicamente para el tercer almacen
    if ((arreglo[i][2] - 100) < 0):
        arreglo[i][2] = 0
    else: 
        print("valor: ", arreglo[i][2], "nuevo: ", arreglo[i][2] - 100)
        arreglo[i][2] = arreglo[i][2] - 100

almacen1 = 0
almacen2 = 0
almacen3 = 0


for i in range(len(arreglo)):
    for j in range(len(arreglo[i])):
        # punto numero 4, almacenando las unidades por almacen
        if (j == 0):
            almacen1 += arreglo[i][j]
        elif (j == 1):
            almacen2 += arreglo[i][j]
        elif (j == 2):
            almacen3 += arreglo[i][j] 
print(arreglo)
print("El total de unidades por almacen para el primer almacen es de: ", almacen1, " el segundo almacen: ", almacen2, " y el tercer almacen: ", almacen3)
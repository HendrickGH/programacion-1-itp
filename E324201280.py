#hendrick adelaido galarza hernandez

#elabora una aplicacion que para n clientes de un estacionamiento, calcule el importe a pagar 
#que le corresponde a cada cliente por estacionar el automovil
#la aplicacion debe de pedir por cada cliente, un numero de carro, validar que sea mayor que 0 y menor o igual que 50 y las horas que se estaciono, mayor que 0 y menor o igual a 12

# calcular el pago por estacionamiento y desplegarlo a la consola, para ello hay que considerar que la tarifa minima es de $15 hasta por 2 horas, luego cobra $5 extra por cada hora adicional despues de las 2 primeras horas

# al final procesar los n clientes y desplegar en consola
#desplegar numero de clientes totales sin pago adicional a las 2 horas, junto con el porcentaje de clientes que represente frente al resto de clientes

#numero total de clientes con pago adicional a las 2 horas y el importe total de los pagos

n = int(input("Ingrese el número de clientes: "))
clientes_sin_pago_adicional = 0
clientes_con_pago_adicional = 0
importe_total = 0
i = 1
pago = 0
horas_estacionado = 0

while i <= n:
    # Validar el número del carro
    while True:
        numero_carro = int(input(f"Ingrese el número del carro para el cliente {i} (1-50): "))
        if 0 < numero_carro <= 50:
            break
            #asi se termina un bucle
        else:
            print("Número de carro inválido. Debe estar entre 1 y 50.")
            #se repite
    # Validar el número de horas
    while True:
        horas_estacionado = int(input(f"Ingrese el número de horas para el cliente {i} (1-12): "))
        if 0 < horas_estacionado <= 12:
            break
        else:
            print("Número de horas inválido. Debe estar entre 1 y 12.")
    # Calcular el pago
    tarifa_minima = 15
    tarifa_adicional = 5
    if horas_estacionado <= 2:
        pago = tarifa_minima
    else:
        pago = tarifa_minima + (horas_estacionado - 2) * tarifa_adicional
        importe_total += pago
    print("El pago del vehiculo será de: " , pago , " y las horas estacionadas fueron: " ,horas_estacionado)
    # lugar equivocado para colocar, ya que solo queremos el importe total de los que pagaronmas de 2 horas
    # importe_total += pago 
    if horas_estacionado > 2:
        clientes_con_pago_adicional += 1
    else:
        clientes_sin_pago_adicional += 1

    i += 1  # Incrementar el contador de clientes

# Calcular porcentaje de clientes sin pago adicional
porcentaje_sin_pago_adicional = (clientes_sin_pago_adicional / n) * 100 if n > 0 else 0

# Mostrar resultados
print("Número total de clientes sin pago adicional:", clientes_sin_pago_adicional)
print("Porcentaje de clientes sin pago adicional:", round(porcentaje_sin_pago_adicional, 2))
print("Número total de clientes con pago adicional:", clientes_con_pago_adicional)
print("Importe total de los pagos con cargo adicional a las 2 horas:", round(importe_total, 2))
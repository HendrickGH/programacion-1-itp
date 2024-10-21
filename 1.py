# Una tienda departamental de ropa desea automatizar el cálculo de salarios de sus empleados y el registro de ventas mensuales de su negocio.
# Donde el salario de cada empleado se calcula por las siguientes condiciones:
# -Salario base por mes empleado es de $2000
# -El costo de la ropa es de $200 c/u
# -Si un empleado tiene ventas mayores a 10,000 al mes, se le otorga una comisión del 5% sobre el total de ventas 
# si tiene ventas mayores a 20,000 la comisión será de 7%
# -El impuesto se calcula como el 10% del salario bruto 
# -La seguridad social es un descuento fijo de $100 
# -La jornada diaria es de 8 horas, cada hora extra se paga $20 c/u y solo se pueden trabajar máximo 4hrs extra
# a) Si el salario bruto (antes de descuentos) es menor o igual a $3,000, se aplica una tasa del 10%.
# b) Si es mayor a $3,000 y menor o igual a $6,000, la tasa de impuestos es del 15%.
# c) Si el salario bruto supera $6,000, se aplica una tasa de impuestos del 20%.
# Mostrar el total de trabajadores procesados 
# Mostrar el total de prendas vendidas en total y por cada trabajador 
# Mostrar el salario neto de cada empleado
# Mostrar el promedio de los salarios calculados
# Mostrar los trabajadores con ventas mayores a 20000
# Agregar el total de impuestos pagados por cada empleado y el total de horas extra trabajadas
# Agregar el total de ventas de cada empleado y cuánto le faltó para alcanzar el bono por vender más de X prendas
# Mostrar de cuánto fue la comisión cuando alcanzaron el bono.

trabajadores = 0
salarios = 0
m20k = 0
tprendas = 0
r = "s"
x = "s"
total_ventas = 0
total_horas_extra = 0
empleado_max_horas_extra = None
max_horas_extra = 0
total_dinero_horas_extra = 0
salario_base = 2000
limite_bono = 10000  # Límite para alcanzar el bono de productividad

while r == "s":
    trabajadores += 1
    nombre = input("Nombre del trabajador: ")

    x = input("¿El trabajador laboró horas extra? <s/n> ")
    if x == "s":
        ext = int(input("¿Cuántas horas extra laboró? "))
        while ext < 1 or ext > 4:
            print("Ingrese las horas extra adecuadas (entre 1 y 4)")
            ext = int(input("¿Cuántas horas extra laboró? ")) 
        total_horas_extra += ext
        total_dinero_horas_extra += ext * 20  # Suma el dinero por horas extra
        if ext > max_horas_extra:
            max_horas_extra = ext
            empleado_max_horas_extra = nombre
        ext = ext * 20
    else:
        ext = 0

    prenda = int(input("¿Cuántas prendas vendió el trabajador? "))
    while prenda < 1 or prenda > 1000:
        print("Da un valor correcto de prendas (1 mínimo, 1000 máximo)")
        prenda = int(input("¿Cuántas prendas vendió el trabajador? "))
    
    tprendas += prenda
    venta = prenda * 200
    total_ventas += venta

    if venta > 10000 and venta <= 20000:
        comis = venta * 0.05
    elif venta > 20000:
        comis = venta * 0.07
        m20k += 1
    else:
        comis = 0

    salbrut = salario_base + ext + comis

    # Cálculo de impuestos y seguridad social
    if salbrut <= 3000:
        impuesto = salbrut * 0.10
    elif salbrut > 3000 and salbrut <= 6000:
        impuesto = salbrut * 0.15
    else:
        impuesto = salbrut * 0.20

    salnet = salbrut - impuesto - 100  # Restar el seguro social
    salarios += salnet

    # Mensaje de por qué el salario subió si supera lo establecido
    if salbrut > salario_base:
        if venta > 10000:
            print("El salario subió porque el trabajador vendió más de ", venta, " en prendas.")
    
    # Mostrar el total de impuestos pagados por el empleado
    print("\nEl salario bruto del empleado ", nombre, " fue ", round(salbrut, 2))
    print("El empleado pagó un total de impuestos de ", round(impuesto, 2))
    print("El coste del seguro social es de $100MXN")
    print("El salario neto del trabajador fue ", round(salnet, 2))
    print("El total de prendas vendidas por el trabajador fue de ", prenda)
    print("El total de ventas del trabajador fue de $", venta, "MXN")

    # Calcular cuánto le faltó para alcanzar el bono de productividad
    if venta < limite_bono:
        diferencia = limite_bono - venta
        print("Al trabajador ", nombre, " le faltaron $", diferencia, " para alcanzar el bono de productividad por ventas.")
    else:
        print("El trabajador ", nombre, " alcanzó el bono de productividad.")
        print("La comisión que ganó fue de $", round(comis, 2), "MXN.")  # Mostrar la comisión con 2 decimales

    r = input("¿Desea realizar otro cálculo <s/n>? ")

prom = salarios / trabajadores
prom_horas_extra = total_horas_extra / trabajadores if trabajadores > 0 else 0

print("\nEl total de prendas vendidas por todos los empleados es ", tprendas)
print("El total de ventas por todas las iteraciones es ", total_ventas)
print("El promedio de salarios calculados es ", round(prom, 2))
print("El promedio de horas extra trabajadas por empleado es ", round(prom_horas_extra, 2))
print("El empleado que más horas extra trabajó fue ", empleado_max_horas_extra, " con ", max_horas_extra, " horas")
print("El total de horas extra trabajadas fue ", total_horas_extra)
print("El total de dinero en horas extra fue ", total_dinero_horas_extra)
print("Trabajadores con ventas mayores a $20,000: ", m20k)
print("Trabajadores procesados: ", trabajadores)

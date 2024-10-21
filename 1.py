#Una tienda departamental de ropa desea automatizar el cálculo de salarios de sus empleados y el registro de ventas mensuales de su negocio.
#Donde el salario de cada sempleado se calcula por las siguientes condiciones:
#-Salario base por mes empleado es de $2000
#-El costo de la ropa es de $200 c/u
#-Si un empleado tiene ventas mayores a 10,000 al mes, se le otorga una comisión del 5% sobre el total de ventas 
#si tiene ventas mayores a 20,000 la comision sera de 7%
#-El impuesto se calcula como el 10% del salario burto 
#-La seguridad social es un descuento fijo de $100 
#-La jornada diaria es de 8 horas cada hora extra se paga $20 c/u y solo se pueden trabajar maximo 4hrs extra
# a) Si el salario bruto (antes de descuentos) es menor o igual a $3,000, se aplica una tasa del 10%.
# b) Si es mayor a $3,000 y menor o igual a $6,000, la tasa de impuestos es del 15%.
# c) Si el salario bruto supera $6,000, se aplica una tasa de impuestos del 20%.
#Mostrar el total de trabajadores procesados 
#Mostrar el total de prendas vendidas en total y por cada trabajador 
#Mostrar el salario neto de cada empleado
#Mostrar el promedio de los salarios calculados
#Mostrar los trabajadores con ventas mayores a 20000

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

while r == "s":
    trabajadores += 1
    nombre = input("Nombre del trabajador: ")

    x = input("¿El trabajador laboro horas extra? <s/n> ")
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
    while prenda < 1 or prenda > 200:
        print("Da un valor correcto de prendas (1 mínimo, 200 máximo)")
        prenda = int(input("¿Cuántas prendas vendió el trabajador? "))
    
    tprendas += prenda
    venta = prenda * 200
    total_ventas += venta

    if venta > 10000 and venta < 20000:
        comis = venta * 0.05
    elif venta > 20000:
        comis = venta * 0.07
        m20k += 1
    else:
        comis = 0

    salbrut = salario_base + ext + comis

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
            print(f"El salario subió porque el trabajador vendió más de {venta} en prendas.")
    
    print(f"El salario bruto del empleado {nombre} fue {salbrut}")
    print("El coste del seguro social es de $100MXN")
    print(f"El salario neto del trabajador fue {salnet}")
    print(f"El total de prendas vendidas por el trabajador fue de {prenda}")
    r = input("¿Desea realizar otro cálculo <s/n>? ")

prom = salarios / trabajadores
prom_horas_extra = total_horas_extra / trabajadores if trabajadores > 0 else 0

print(f"\nEl total de prendas vendidas por todos los empleados es {tprendas}")
print(f"El total de ventas por todas las iteraciones es {total_ventas}")
print(f"El promedio de salarios calculados es {prom}")
print(f"El promedio de horas extra trabajadas por empleado es {prom_horas_extra}")
print(f"El empleado que más horas extra trabajó fue {empleado_max_horas_extra} con {max_horas_extra} horas")
print(f"El total de horas extra trabajadas fue {total_horas_extra}")
print(f"El total de dinero en horas extra fue {total_dinero_horas_extra}")
print(f"Trabajadores con ventas mayores a $20,000: {m20k}")
print(f"Trabajadores procesados: {trabajadores}")

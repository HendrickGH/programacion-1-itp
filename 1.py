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

trabajadores=0
salarios=0
m20k=0
tprendas=0
r="s"
x="s"
while r=="s":
    trabajadores+=1
    x= input ("¿El trabajador laboro horas extra? <s/n> ")
    if x == "s":
        ext = int(input("¿Cuántas horas extra laboró? "))
        while ext < 1 or ext > 4:
            print("Ingrese las horas extra adecuadas (entre 1 y 4)")
            ext = int(input("¿Cuántas horas extra laboró? ")) 
        ext = ext * 20
    else:
        ext = 0

    prenda=int(input("¿Cuantas prendas vendio el trabajador? "))
    while prenda<1 or prenda>200:
        print ("Da un valor correcto de prendas (1 minimo, 200 maximo)")
        prenda=int(input("¿Cuantas prendas vendio el trabajador? "))
   
    tprendas+=prenda
    venta=prenda*200

    if venta>10000 and venta <20000:
        comis=venta*0.05
    elif venta>20000:
        comis=venta*0.07
        m20k+=1
    else:
        comis=0
    
    salbrut= 2000 + ext + comis 
    
    if salbrut <=3000:
        impuesto= salbrut * 0.10
        salnet= salbrut - impuesto - 100
    elif salbrut >3000 and salbrut<=6000:
        impuesto= salbrut * 0.15
        salnet= salbrut - impuesto - 100
    else:
        impuesto= salbrut * 0.20
        salnet= salbrut - impuesto - 100

    salarios+=salnet
    print ("El salario bruto del empleado fue ", salbrut)
    print ("El coste del seguro social es de $100MXN")
    print ("El salario neto del trabajador fue ", salnet)
    print ("El total de prendas vendidas por el trabajador fue de ", prenda)
    r = input ("Desea realizar otro calculo <s/n> ")

prom=salarios/trabajadores
print ("El promedio de los salarios fue de ", prom) 
print ("Trabajadores con ventas mayores a $20,000 ", m20k)   
print ("Trabajadores procesados ", trabajadores)   
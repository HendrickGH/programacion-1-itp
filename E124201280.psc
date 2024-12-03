Algoritmo Examen
	// 1.- solicitar al usuario el numero de horas laboradas por el trabajador
	// entero validar que este entre 10 y 60 horas
	// 2.- calcular el salario semanal el cual se obtiene de 40 o menos se paga 16 por hora
	// si trabaja mas de 40 horas se paga las primeras 40 a 16, el resto 10 pesos por
	// hora extra
	// despliega a la consola el sueldo obtenido
	// preguntar si quiere calcular otro usuario
	// 3.- cuando ya no quiera nada mas el usuario, preguntar cuantos trabajadores 
	// se calcularon, cuantos mas de 40 horas, cuantos 40 horas exactas, la suma 
	// total de todos los trabajadores que no rebasaron 40 horas 
	Definir horasTrabajadas, salario, horasExtra, totalTrabajadores, trabajadoresMas40, trabajadores40Exactas, sumaSalarios40Menos Como Entero
		Definir calcularOtro Como Caracter
		
		// Inicializar contadores
		totalTrabajadores = 0
		trabajadoresMas40 = 0
		trabajadores40Exactas = 0
		sumaSalarios40Menos = 0
		
		Repetir
			// 1. SSolicitar horas laboradas trabajadas y que este entre 10 y 60
			Escribir "Ingresa el n�mero de horas trabajadas (entre 10 y 60):"
			Leer horasTrabajadas
			Mientras horasTrabajadas < 10 O horasTrabajadas > 60 Hacer
				Escribir "Error: Ingresa un n�mero de horas entre 10 y 60."
				Leer horasTrabajadas
			FinMientras
			
			// 2. Calcular el salario
			Si horasTrabajadas <= 40 Entonces
				salario = horasTrabajadas * 16
				Si horasTrabajadas = 40 Entonces
					trabajadores40Exactas = trabajadores40Exactas + 1
				Sino
					sumaSalarios40Menos = sumaSalarios40Menos + salario
				FinSi
			Sino
				horasExtra = horasTrabajadas - 40
				salario = (40 * 16) + (horasExtra * 10)
				trabajadoresMas40 = trabajadoresMas40 + 1
			FinSi
			
			// Mostrar el salario calculado
			Escribir "El salario del trabajador es: ", salario
			
			totalTrabajadores = totalTrabajadores + 1
			
			// Preguntar si se desea calcular otro trabajador
			Escribir "Presiona cualquier letra para continuar calculando trabajadores, si deseas parar escribe no"
			Leer calcularOtro
			
		Hasta Que calcularOtro = "no" O calcularOtro = "No" O calcularOtro = "NO" O calcularOtro = "nO" O calcularOtro = "no." O calcularOtro = "No." O calcularOtro = "NO." O calcularOtro = "nO."
		
		// 3. Mostrar el resumen final
		Escribir "Total de trabajadores calculados: ", totalTrabajadores
		Escribir "Trabajadores con m�s de 40 horas: ", trabajadoresMas40
		Escribir "Porcentaje de rabajadores con 40 horas exactas: ", trabajadores40Exactas / totalTrabajadores, "%"
		Escribir "Suma total de los salarios de los trabajadores que trabajaron menos de 40 horas: ", sumaSalarios40Menos

FinAlgoritmo

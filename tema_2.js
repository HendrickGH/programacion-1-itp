a = 80;
b = 625.75;
c = 356.42;
d = false;

// ejercicio #1
c = a * b - 7.6 + c / 2.4;
// primero ejecuta la multiplicacion -> 80 * 625.75
// luego ejecuta la division -> 356.42 / 2.4
// queda c = (a*b) - 7.6 + (c/2.4)
// osea c = 50060 - 7.6 + 148.5
// resultado c = 50200.9

// ejercicio #2
b = a - b * ((4.5 + c) / 2);
// primero ejecutamos los parentesis internos -> 4.5 + 50200.9
// luego dividimos el resultado entre 2 -> 50205.4 / 2
// luego el resultado lo multiplicamos por b -> 25102.7 * 625.75
// luego el resultado le restamos a -> 80 - 15708014.525
// resultado b = -15707934.525

// ejercicio #3
a = a + c ** 2 * (b - c + 10);
// primero los parentesis, de izquierda a derecha -> -15707934.525 - 50200.9 + 10
// luego la potencia -> 50200.9 ** 2
// resolvemos -> a + 2520130360.81 * -15758125.425
// resolvemos -> 80 + -39712530312994490
// a = -39712530312994410

// ejercicio #4
d = a <= b || b >= c;
// evaluamos la expresion
// -39712530312994410 <= -15707934.525 => es true ya que el primer numero es true, no es necesario evaluar el resto de la expresion

// ejercicio #5
d = (c < b && b == a) || c >= b;
// evaluamos la expresion
// 50200.9 < -15707934.525 esto es false, por tanto ni siquiera necesitamos verificar el and
// pasamos al or
// 50200.9 >= -15707934.525 esto es true, un numero positivo siempre sera mayor a uno negativo
// respuesta final d = true

// ejercicio #6
c = a / 8 + b * 3.5 - c;
// reemplazamos valores (division y multiplicacion tienen la misma jerarquia, se considera de izquierda a derecha)
// -39712530312994410 / 8 + b * 3.5 - c
// luego hacemos la multiplicacion
// -4964066289124301 + -15707934.525 * 3.5 - c
// sustituimos valores del resultado de la multiplicacion, y sustituimos el valor de c
// -4964066289124301 + -54977770.8375 - 50200.9
// ejecutamos directamente la operacion
// respuesta final c = -4964066344152273

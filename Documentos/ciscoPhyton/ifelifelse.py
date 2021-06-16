año = int(input("Introduzca un año:"))

if año < 1582:
    print ("No esta dentro del período del calendario gregoriano, este se instauro en 1582.");

if año%4 == 0:
    print("Año bisiesto");

elif año%4 != 0:
    print("Año normal");


#Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

#Si el número del año no es divisible entre cuatro, es un año común.
#De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
#De lo contrario, si el número del año no es divisible entre 400, es un año común.
#De lo contrario, es un año bisiesto.

#Observa el código en el editor: solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.

#El código debe mostrar uno de los dos mensajes posibles, que son Año bisiesto o Año común, según el valor ingresado.

#Sería bueno verificar si el año ingresado cae en la era gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario gregoriano. Consejo: utiliza los operadores != y %.

#Prueba tu código con los datos que hemos proporcionado.
#Datos de prueba

#Entrada de muestra: 2000

#Resultado esperado: Año bisiesto

#Entrada de muestra: 2015

#Resultado esperado: Año común 

#Entrada de muestra: 1999

#Resultado esperado: Año común 

#Entrada de muestra: 1996

#Resultado esperado: Año bisiesto 

#Entrada de muestra: 1580

#Resultado esperado: No dentro del período del calendario gregoriano 
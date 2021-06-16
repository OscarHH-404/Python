#ejemplos if, if else, if elif else

#Una única declaración if, por ejemplo:
x = 10

if x == 10: # condición
    print("x es igual a 10") # ejecutado si la condición es verdadera


#Una serie de declaraciones if, por ejemplo:
x = 10

if x > 5: # condición uno
    print("x es mayor que 5") # ejecutado si la condición uno es verdadera

if x <10: # condición dos
    print("x es menor que 10") # ejecutado si la condición dos es verdadera

if x == 10: # condición tres
     print("x es igual a 10") # ejecutado si la condición tres es verdadera


#Una declaración de if-else, por ejemplo:
x = 10

if x < 10: # condición
    print ("x es menor que 10") # ejecutado si la condición es Verdadera

else:
    print ("x es mayor o igual a 10") # ejecutado si la condición es False


#Una serie de declaraciones if seguidas de un else, por ejemplo:
x = 10

if x > 5: # Verdadero
    print("x > 5")

if x > 8: # Verdadero
    print("x > 8")

if x > 10: # Falso
    print("x > 10")

else:
    print("Se ejecutará el else")


#La declaración  if-elif-else, por ejemplo:
x = 10

if  x == 10: # Verdadero
    print("x == 10")

if x > 15: # Falso
    print("x > 15")

elif x > 10: # Falso
    print("x > 10")

elif x > 5: # Verdadero
    print("x > 5")

else:
    print("No se ejecutará el else")


#Declaraciones condicionales anidadas, ejemplo:
x = 10

if x > 5: # Verdadero
    if x == 6: # Falso
        print("anidado: x == 6")
    elif x == 10: # Verdadero
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")
numeroSecreto = 777;

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""");

numero  = int(input("Dime ¿Cuál será el número que escogeras?"));

while numero != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!" )
    numero  = int(input("Dime ¿Cuál será el número que escogeras ahora?"));    

print ("¡Bien hecho, muggle! Eres libre ahora");


#Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada númeroSecreto. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quienes no adivinen el número quedarán atrapados en un ciclo sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

#Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

#    Pedirá al usuario que ingrese un número entero.
#    Utilizará un ciclo while.
#    Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el 
# número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje 
# "¡Ja, ja! ¡Estás atrapado en mi ciclo!" y se le solicitará que ingrese un número nuevamente. Si 
# el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en 
# la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora".

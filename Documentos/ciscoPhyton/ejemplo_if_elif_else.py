#ejemplo if elif else

x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int (x)> 1:
        print("dos")
    elif int (x) < 1:
        print("tres")
    else:
        print("cuatro")
if int (x) == 1:
    print("cinco")
else:
    print("seis") 


#Ejemplo 2
x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
if y == int (z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro") 
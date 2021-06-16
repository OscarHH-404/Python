hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
convdura = int(dura/60);
conv = int(dura % 60);
sumamin = int (min + conv);
print("EL evento termina" + " " + str((hora + convdura)) + ":" + str((min + conv)));

ingreso=float(input("Ingrese el ingreso anual:"));
exfiscal = 85528;


if ingreso <= 3090:
    impuesto = 0.0;
    
else:
    impuesto = ((ingreso * 18) / 100) - 556.2;

if ingreso > exfiscal:
    impuesto = (((ingreso - exfiscal) * 32) /100) + 14839.2 ;

impuesto=round(impuesto, 0);
print("El impuesto es: ", impuesto, "pesos");


#    Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).
#   Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.

#Tu tarea es escribir una calculadora de impuestos.

#    Debe aceptar un valor de punto flotante: el ingreso.
#    A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti, la encontrarás en el código de esqueleto del editor.

#Nota: Este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

#Observa el código en el editor: solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes.

#Prueba tu código con los datos que hemos proporcionado.
#Datos de prueba

#Entrada de muestra: 10000

#Resultado esperado: El impuesto es: 1244.0 pesos

#Entrada de muestra: 100000

#Resultado esperado: El impuesto es: 19470.0 pesos

#Entrada de muestra: 1000

#Resultado esperado: El impuesto es: 0.0 pesos

#Entrada de muestra: -100

#Resultado esperado: El impuesto es: 0.0 pesos




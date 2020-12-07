resultado = 0
valor1 = int (input("Ingrese el primer valor la operación"))
valor2 = int (input("Ingrese el segundo valor la operación"))
op = int(input("Selecciones la operación que desea realizar \n "
            + "Ingrese 1 para sumar \n "
            + "Ingrese 2 para restar \n "
            + "Ingrese 3 para multiplicar"))
if (op == 1):
    resultado = valor1 + valor2
else :
    if (op == 2):
        resultado = valor1 - valor2
    else :
        if (op == 3):
            resultado = valor1 * valor2
        else :
            print("mensaje incorrecto")
print ("El resultado de la operación es : %d\n" % resultado)

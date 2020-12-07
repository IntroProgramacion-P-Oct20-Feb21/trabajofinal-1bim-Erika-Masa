limite_inferior = 10
limite_superior = 20
contador = 10
suma = 0
while (contador >= limite_inferior) and (contador <= limite_superior):
    suma = suma + contador
    print("contador %d \n "% contador )
    contador = contador + 5
    print ("la suma final es: %d \n"% suma )
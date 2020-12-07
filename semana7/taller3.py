numero = 1
contador1 = 3
i = 2
bandera = "true"
while (bandera):
    print ("% d"% (i))
    i = i + contador1
    contador1 = contador1 + 2
    numero = numero + 1
    if (numero >= 7):
        bandera = "false"

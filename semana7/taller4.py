numero = 1
contador = 4
i = 2
bandera = "true"
while(bandera):
    print ("% d"% (i))
    i = i + contador
    contador = contador + 2
    numero = numero + 1
    if numero >= 11:
        bandera = "false"

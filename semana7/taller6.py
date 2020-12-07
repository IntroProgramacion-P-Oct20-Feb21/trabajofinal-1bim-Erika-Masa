numerador = 1
denominador = 1
contador = 1
bandera= "true"
while (bandera):
    if(contador% 2) == 0:
        print ("% s% d /% d"% ("-", numerador, denominador))
    else:
        print ("% s% d /% d"% ("+", numerador, denominador))
    contador = contador + 1
    denominador = denominador + 2
    if contador >= 6:
        bandera= "true"
print()
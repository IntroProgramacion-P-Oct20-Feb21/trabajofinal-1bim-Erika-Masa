tabla= int(input("ingrese el numero de tablas que desea generar \n" ))
for contador in range(1, 10, 1):
    operacion= tabla * contador
    print("%d x %d = %d\n" %( tabla,contador,operacion))
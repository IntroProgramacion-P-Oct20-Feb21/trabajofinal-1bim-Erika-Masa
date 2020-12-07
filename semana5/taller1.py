porcentaje = 10
costohora = int(input("Ingrese el valor de costo por kilovatio/hora \n "))
kilovatiosConsumidos = float(input("Ingrese el número de kilovatios consumidos en el mes.\n"))
edad= float(input("ingrese la edad del cliente\n"))
costo_total = costohora *  kilovatiosConsumidos
if(edad >= 65 ):
    descuento = costo_total * porcentaje/ 100
    costo_total = costo_total - descuento
    print("el costo total es:  % 2.f \n" % (costo_total))
porcentaje1 = 10
porcentaje2 = 15
porcentaje3 = 20

numeroDias = int(input("ingrese el numero de dias que se hospedara"))
valorDia = int(input("ingrese el valor diario de la habitacion"))

if (numeroDias > 5 ) and (numeroDias <= 10):
        subtotal = numeroDias * valorDia
        descuento = (porcentaje1 * subtotal)/100
        valorTotal = subtotal - descuento
else:
    if (numeroDias >10) and (numeroDias <= 15):
        subtotal = numeroDias * valorDia
        descuento = (porcentaje2 * subtotal) / 100
        valorTotal = subtotal - descuento

if (numeroDias > 15):
        subtotal = numeroDias * valorDia
        descuento = (porcentaje3 * subtotal) / 100
        valorTotal = subtotal - descuento
else:
        subtotal = numeroDias * valorDia
        descuento = 0
        valorTotal = subtotal - descuento
print("El valor subtotal es: %.2f\n" % subtotal
                + "El descuento es: %.2f\n" % descuento
                + "El valor total a pagar es: %.2f\n" % valorTotal)























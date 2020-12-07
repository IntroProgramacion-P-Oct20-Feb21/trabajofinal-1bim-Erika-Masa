porcentaje = 15
descripcion = input("ingrese la descripcion del articulo \n " )
articulos = int(input("ingrese la cantidad que se requiere de articulo \n"))
precioUnitario = float(input("ingrese el precio unitario del articulo \n"))
costo = precioUnitario * articulos
if (articulos >50 ):
    descuento = (costo * precioUnitario) / 100
    costo = costo - descuento
    print("El costo a pagar es:% .2f $" % (costo))
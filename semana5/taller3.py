porcentajeAl  =   20
porcentajeJap  =   30
porcentajeIta  =  15
porcentajeUs  =   8
marca  =  input ( "Ingresar la marca del automóvil:\n" )
origen  =  input ( "Ingresar el origen del automóvil:\n" )
costo  =  float ( input ( "Ingresar el costo del automóvil:\n" ))

if  origen  ==  "Japon" :
    impuesto  = ( costo  *  porcentajeJap ) / 100
    total  =  costo  +  impuesto
else :
    if  origen  ==  "Italia" :
        impuesto  = ( costo  *  porcentajeIta ) / 100
        total  =  costo  +  impuesto
    else:
        if  origen  ==  "USA" :
            impuesto  = ( costo  *  porcentajeUs ) / 100
            total  =  costo  +  impuesto
        else :
            print ( "El origen del vehículo no es válido \n " )

print ( "El valor del impuesto total a pagar:% .2f \n El valor total de venta es:% .2f"  % ( impuesto , total ))



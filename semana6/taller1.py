netflix  = 10
disney  =  6
Apple  =   5
amazon  =  4.50
bandera  =  "true"
nombre  = input ( "Ingresar el nombre del usuario \n " )
while (bandera) :
    empresa  =  input ( "Ingrese el nombre de la empresa: \n Netflix \n "
    + "Disney \n "
    + "Apple \n "
    +  "Amazon \n " )
    if  empresa  ==  "Netflix" :
        iva_netflix,  = ( netflix  *  10 ) / 100
        total_netflix  =  netflix  +  iva_netflix
        print (("Usuario:%s\n"
               +"Empresa: Netflix\n"
               + "Precio base: $%.2f\n"
               +"Impuesto: $%.2f\n"
               +"Total a cancelar: $%.2f\n",
               nombre,
               netflix,
               iva_netflix,
               total_netflix))
    elif  empresa  ==  "Disney" :
        iva_disney  = ( disney  *  10 ) / 100
        total_disney  =  disney  +  iva_disney
        print ( "Usuario:%s\n"
               +"Empresa: disney\n"
               + "Precio base: $%.2f\n"
               +"Impuesto: $%.2f\n"
               +"Total a cancelar: $%.2f\n",
               nombre,
               disney,
               iva_disney,
               total_disney)
    elif  empresa  ==  "Apple" :
        iva_apple  = ( Apple  *  10 ) / 100
        total_apple  =  Apple  +  iva_apple
        print ( "Usuario:%s\n"
               +"Empresa: apple\n"
               + "Precio base: $%.2f\n"
               +"Impuesto: $%.2f\n"
               +"Total a cancelar: $%.2f\n",
               nombre,
               Apple,
               iva_apple,
               total_apple)
    elif  empresa  ==  "Amazon" :
        iva_amazon  = ( amazon  *  10 ) / 100
        total_amazon  =  amazon  +  iva_amazon
        print ( "Usuario:%s\n"
               +"Empresa: amazon\n"
               + "Precio base: $%.2f\n"
               +"Impuesto: $%.2f\n"
               +"Total a cancelar: $%.2f\n",
               nombre,
               amazon,
               iva_amazon,
               total_amazon)
    negacion =  int ( input ( "Ingrese -1 para salir de la secuencia:" ))
    if  negacion  ==  - 1 :
        bandera  =  "False"

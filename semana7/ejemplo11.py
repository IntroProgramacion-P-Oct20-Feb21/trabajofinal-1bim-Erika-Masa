cadenaF  =  ""
bandera = "true"
while(bandera):
    nota  =  float ( input ( "Ingrese calificaciones:" ))
    cadenaF  =  "% s% .2f \ n "  % ( cadenaF , nota )

    salida  =  int ( input ( "Ingrese (-111) para salir del ciclo:" ))
if  (salida  ==  - 111 ):
     bandera="false"
print ( "Listado de Notas\n%s\n"% cadenaF )
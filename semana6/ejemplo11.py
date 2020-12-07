suma_total = 0
bandera =" true"

while (bandera):
    calificacion = float(input("ingrese calificacion \n "))
    suma_total = suma_total + calificacion
    salir = int(input("Ingrese -1 para salir del ciclo \n "))
    if(salir == - 1):
        bandera = "Falso"
        print("suma de calificaciones es : %d \n " % suma_total )
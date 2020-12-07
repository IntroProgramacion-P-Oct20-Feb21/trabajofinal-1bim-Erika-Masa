suma_total = 0
bandera = "true"
contador = 0
print("ingrese las notas de lo estudiantes de su materias")
while(bandera):
    calificacion = float(input("ingrese calificacion \n "))
    suma_total = suma_total + calificacion
    cantador = contador + 1
    temporal = int(input("Ingrese -1 para salir del ciclo \n "))
    if (temporal == "-1"):
            bandera = "Falso"
            promedio = ("suma_total / contador")
print("el promedio final es : % . 2f \n " % promedio)


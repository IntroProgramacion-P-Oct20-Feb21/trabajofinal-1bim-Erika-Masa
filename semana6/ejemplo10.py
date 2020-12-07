limite = 3
contador = 1
suma_total = 0
print ("ingrese las notas del estudiante")
while (contador <= limite):
    calificacion = float (input("ingrese calificacion numero %d \n "% contador ))
    suma_total= suma_total +  calificacion
    contador = contador + 1
    promedio = suma_total / limite
    print (  "El promedio final es: %d \n "% promedio )
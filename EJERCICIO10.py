def Ejercicio10():
    a = int(input("Ingrese la calificación de exámen parcial."))
    b = int(input("Ingrese la calificación por TPs."))
    c = int(input("Ingrese la calificación del exámen integrador."))

    calificacionA = a * 0.3
    calificacionB = b * 0.2
    calificacionC = c * 0.5

    notafinal = calificacionA + calificacionB + calificacionC
    print("El promedio del estudiante es: "+ notafinal)
#Ejercicio10

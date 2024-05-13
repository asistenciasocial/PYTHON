def Ejercicio9():
    fecha = int(input("Ingrese la fecha en formato DDMMAAAA."))

    dia = fecha//1000000
    mes = (fecha//10000) % 100
    año = fecha % 10000

    print("Día: ", dia)
    print("Mes: ", mes)
    print("Año: ", año)
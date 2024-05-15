def ej5():
    horas = int(input("Ingresa las horas: "))
    minutos = int(input("Ingresa los minutos: "))
    segundos = int(input("Ingresa los segundos: "))


    totalsegundos = horas * 3600 + minutos * 60 + segundos


    print("El resultado expresado en segundos es:", totalsegundos)

ej5()
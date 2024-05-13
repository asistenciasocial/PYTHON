def Ejercicio11():

    autos = []
    inputUser = ""
    while inputUser != "SALIR":
        inputUser = input("ingrese el valor del auto vendido o SALIR")
        if inputUser != "SALIR":
            inputUser = float(inputUser)
            autos.append(inputUser)

    AUx = sum(autos)
    comision = AUx * 0.05

Ejercicio11()
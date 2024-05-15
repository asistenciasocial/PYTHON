def eje11():

    autos = []
    inputUser = ""
    while inputUser != "SALIR":
        inputUser = input("ingrese el valor del auto vendido o salir: ")
        if inputUser != "SALIR":
            inputUser = float(inputUser)
            autos.append(inputUser)

    AUx = sum(autos)
    comision = AUx * 0.05
    salario = len(autos) * 200
    cobrar = 5500 + salario + comision

    print("el salario es de ", cobrar, " pesos.")

eje11()
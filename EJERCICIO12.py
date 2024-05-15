dia_nacimiento_p1 = int(input("Persona 1, ingrese su día de nacimiento: "))
mes_nacimiento_p1 = int(input("Persona 1, ingrese su mes de nacimiento: "))
año_nacimiento_p1 = int(input("Persona 1, ingrese su año de nacimiento: "))


dia_nacimiento_p2 = int(input("Persona 2, ingrese su día de nacimiento: "))
mes_nacimiento_p2 = int(input("Persona 2, ingrese su mes de nacimiento: "))
año_nacimiento_p2 = int(input("Persona 2, ingrese su año de nacimiento: "))


if año_nacimiento_p1 < año_nacimiento_p2:
  print("Persona 1 es mayor")
elif año_nacimiento_p1 > año_nacimiento_p2:
  print("Persona 2 es mayor")
else:
  
  if mes_nacimiento_p1 < mes_nacimiento_p2:
    print("Persona 1 es mayor")
  elif mes_nacimiento_p1 > mes_nacimiento_p2:
    print("Persona 2 es mayor")
  else:

    if dia_nacimiento_p1 < dia_nacimiento_p2:
      print("Persona 1 es mayor")
    elif dia_nacimiento_p1 > dia_nacimiento_p2:
      print("Persona 2 es mayor")
    else:
      print("Ambas personas tienen la misma edad")


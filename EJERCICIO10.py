def calcular_nota_final(examenesparciales, trabajospracticos, examenintegrador):

    if not (0 <= examenesparciales <= 10 and 0 <= trabajospracticos <= 10 and 0 <= examenintegrador <= 10):
        return "Las notas deben estar en el rango de 0 a 10."

    nota_final = (examenesparciales * 0.3) + (trabajospracticos * 0.2) + (examenintegrador * 0.5)
    return nota_final


examenesparciales = float(input("Ingrese la calificación de los exámenes parciales (0-10): "))
trabajospracticos = float(input("Ingrese la calificación de los trabajos prácticos (0-10): "))
examenintegrador = float(input("Ingrese la calificación del examen integrador (0-10): "))


nota_final = calcular_nota_final(examenesparciales, trabajospracticos, examenintegrador)
print(f"La calificación final del estudiante es: {nota_final}")
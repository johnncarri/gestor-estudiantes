def registrar_estudiantes():
    estudiantes = {}
    while True:
        nombre = input("Nombre de estudiante ( o fin para salir)").capitalize()
        if nombre == 'Fin':
            break
        nota = float(input(f"Introduzca la nota de {nombre}: "))
        if nombre in estudiantes:
            estudiantes[nombre].append(nota)
        else:
            estudiantes[nombre] = [nota]
    return estudiantes
def mostrar_promedios(estudiantes):
    print("\n Promedios de estudiantes:")
    for nombre, notas in estudiantes.items():
        if notas:
            promedio = sum(notas) / len(notas)
            print (f"{nombre}: {promedio:.2f}")
        else:
            print (f"{nombre}: No tiene notas registradas.")

def estudiante_con_mejor_promedio(estudiantes):
    mejor_estudiante = ""
    mejor_promedio = -1
    for nombre, notas in estudiantes.items():
        if notas:
            promedio = sum(notas) /len(notas)
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_estudiante = nombre
    print(f"\n El estudiante con el mejor promedio es {mejor_estudiante} con {mejor_promedio:.2f}")

def estudiante_con_peor_promedio(estudiantes):
    peor_estudiante = ""
    peor_promedio = float('inf')

    for nombre, notas in estudiantes.items():
        if notas:
            promedio = sum(notas) / len(notas)
            if promedio < peor_promedio:
                peor_promedio = promedio
                peor_estudiante = nombre
    if peor_estudiante:
        print(f"\n El estudiante con el peor promedio es {peor_estudiante} con {peor_promedio:.2f}")
    else:
        print("No hay estudiantes con notas.")

def guardar_en_archivo(estudiantes, nombre_archivo="registro_estudiantes.txt"):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("📋 Registro de estudiantes y notas:\n\n")

        mejor_est = ""
        mejor_prom = -1
        peor_est = ""
        peor_prom = float("inf")

        for nombre, notas in estudiantes.items():
            promedio = sum(notas) / len(notas) if notas else 0
            archivo.write(f"{nombre}: notas = {notas}, promedio = {promedio:.2f}\n")

            # Actualizar mejor/peor
            if promedio > mejor_prom:
                mejor_prom = promedio
                mejor_est = nombre
            if promedio < peor_prom:
                peor_prom = promedio
                peor_est = nombre

        archivo.write("\n🏆 Mejor estudiante:\n")
        archivo.write(f"{mejor_est} con promedio {mejor_prom:.2f}\n")

        archivo.write("\n📉 Peor estudiante:\n")
        archivo.write(f"{peor_est} con promedio {peor_prom:.2f}\n")

    print(f"\n✅ Datos guardados correctamente en '{nombre_archivo}'")

registro = registrar_estudiantes()
print(registro)
mostrar_promedios(registro)
estudiante_con_mejor_promedio(registro)
estudiante_con_peor_promedio(registro)
guardar_en_archivo(registro)
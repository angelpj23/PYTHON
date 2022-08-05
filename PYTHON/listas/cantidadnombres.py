try:
    saludos = []
    
    numero = int(input("Introduzca la cantidad de saludos:\n "))
    otro = range(1, numero +1)

    for o in otro:
        saludos.append(input(f"Introduzca el nombre {o}: " ))

    for s in saludos:
        print(f"Buenas tardes: {s}" )
except ValueError:
    print("Solo se aceptan numeros")
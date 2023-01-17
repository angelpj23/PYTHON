print("Evaluacion de calificaciones")
try:
    while True:
        nombre = input("Nombre del estudiante:\n")
        puntos = float(input('Ingrese puntuacion:'))
 
        if puntos < 0.0 or puntos > 10.0:
            print('Fuera de rango!!. Debe ser entre 0.0 y 10.0')
        else:
            if puntos >= 9.5:
                print(nombre + ' es Sobresaliente')
            elif puntos >= 8.0 and puntos < 9.4:
                print(nombre + ' es Notable')
            elif puntos >= 7.0 and puntos < 8.0:
                print(nombre + ' esta Bien')
            elif puntos >= 6.0 and puntos < 7.0:
                print(nombre + ' tiene Suficiente')
            else:
                print(nombre + ' reprobo')
except ValueError:
    print("solo se aceptan numeros y que esten dentro del rango")
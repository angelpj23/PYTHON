
try:
    while True:
        print ("1-SUMA")
        print ("2-RESTA")
        print ("3-MULTIPLICACION")
        print ("4-DIVISION")
        print ("5-POTENCIAR")
        print ("6-RADICAL")
        print ("7-SALIR")
        opcion = int(input("Selecciona una opcion numerica disponible:\n"))
        if opcion > 0 and opcion <=7:
            if opcion > 0 and opcion <=5:
                n1 = int(input("Introduzca primer numero:\n "))
                n2 = int(input("Introduzca segundo numero:\n "))

            elif opcion == 6:            
                n1 = int(input("Introduzca un numero:\n "))

        if opcion == 1:
            SUMA = (n1) + (n2)
            print("El resultado es", SUMA)
                    
        elif opcion == 2:
            RESTA = (n1) - (n2)
            print("El resultado es", RESTA)

        elif opcion == 3:
            MULTIPLICACION = (n1) * (n2)
            print("El resultado es", MULTIPLICACION)
                
        elif opcion == 4:
            try:
                DIVISION = (n1) / (n2)
                print("El resultado es", DIVISION)
            except:
                print ("no se puede dividir entre 0")
                    
        elif opcion == 5:
            POTENCIAR = (n1) ** (n2)
            print("El resultado es", POTENCIAR)
                    
        elif opcion == 6:            
            #n1 = int(input("Introduzca un numero:\n "))
            from math import sqrt
            RADICAL = sqrt(n1) 
            print("El resultado es", RADICAL)
                    
        elif opcion == 7:
            print("Hasta luego!")
            break
except ValueError:
    print("solo acepta numeros") 
  
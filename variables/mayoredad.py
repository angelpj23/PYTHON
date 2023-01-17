try:        
    person = int(input("Digite la edad:\n "))

    if person < 18:
        print("menor de edad")

    elif person > 18:
        print("mayor de edad")

    if person < 0:
        print("no ha nacido")

    if person > 105:
        print("probablemente murio")
except ValueError:
    print("solo se aceptan numeros enteros")





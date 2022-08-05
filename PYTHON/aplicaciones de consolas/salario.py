try:
    print("Calculo de Nominas")
   
    empleado = input("Nombre del empleado:\n")    
           
    horas = int(input("Horas trabajadas\n"))

    if horas >= 32:
        salario = horas * 2000
    elif horas <= 0:
        salario = horas * 0
        print("Usted no trabajo!")
    else:
        salario = (2000*horas) 
        print("El empleado:", empleado)
        print("Tiene un salario de: ", salario)
except ValueError:
    print("solo se aceptan numeros enteros")
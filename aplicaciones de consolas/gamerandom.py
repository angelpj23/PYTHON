import random

print("Bienvenid@ a mi juego, como te llamas?:\n")
nombre = input()
seleccion = random.randint(1, 101)
print("Ok! " + nombre + " Tengo en mente un numero entre 1 y 100, adivinalo en 5 intentos\n")
intentos = 0
try:
    while True:
        numero = int(input("Adivina el numero:\n"))
        intentos = intentos +1
        
        if numero == seleccion:
            intentos = str(intentos) #se convierte el numero (int) a cadena (str) para que se pueda imprimir junto
            seleccion = str(seleccion)
            print("Ganaste esta vez! " + nombre + " en " + intentos + " intentos!")
            print("El numero si era " + seleccion)
            break
        if seleccion > numero:
            print("Es un numero Mayor, sigue intentando")
        else: 
            print ("Es un numero Menor, sigue intentando") 
        if intentos == 5:
            intentos = str(intentos)
            seleccion = str(seleccion)
            print("Jajaja " + nombre + " Perdiste, se te acabaron los " + intentos + " intentos")
            print("el numero era " + seleccion)
            break   
     
except ValueError:
    print("No valido, solo numeros")
    
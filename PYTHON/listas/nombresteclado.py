#Se debe pedir por teclado 2 nombres, insertarlos en 
# una lista y mostrarlos en consola.

lista = []
nombre1 = input("Introduzca el primer nombre por favor:\n ")
nombre2 = input("Introduzca el segundo nombre por favor:\n ")

lista.append(nombre1)
lista.append(nombre2)

print("nombres agregados a la lista")
for l in lista:
    print(l)
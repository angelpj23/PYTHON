class objeto:
    valor1 = "Soy el valor del objeto"
# la variable recibe el o los valores del objeto
saludo = objeto()
# se imprime un string y se agrega un valor del objeto
print("hola", saludo.valor1)


# ----------------------------------------------------
class jugador:
    def __init__(self, nombre, dorsal):
        self.nombre = nombre
        self.dorsal = dorsal

j1 = jugador("Ja Morant", "12")
j2 = jugador("Jason Tatum", "0")

print("Base: ", j1.nombre, " Dorsal: ",j1.dorsal)
print("Alero: ", j2.nombre, " Dorsal: ",j2.dorsal)
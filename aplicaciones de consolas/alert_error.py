a = 5; b = 0
try:
    c = a/b
# ZeroDivisionError viene de python no es un nombre asignado por el desarrollador
except ZeroDivisionError: 
    print("No se ha podido realizar la división")


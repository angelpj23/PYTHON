Esta funcion lee el archivo completo, si el archivo es muy grande va a consumir mucha
memoria:
  contenido = mi_archivo.read()
  print(contenido)

  --------------------------------------------------------------------------------------

Leer un fichero línea a línea

with open('ruta_del_fichero') as f:
    for linea in f:
        # Tu código aquí

  --------------------------------------------------------------------------------------
¿Qué significa la palabra with al principio del bloque?
Python nos ayuda a abstraernos del código repetitivo introduciendo 
lo que se conocen como «Manejadores de contexto» a través de la sentencia with

En el caso de los ficheros, with nos asegura de que el fichero se cerrará 
correctamente después de ejecutarse el código en el interior del bloque, 
incluso si ocurre alguna excepción.

De manera que el siguiente código

with open('hola.txt', 'r') as f:
    for linea in f:
        ...
sería equivalente a este

f = open('hola.txt', 'r')
try:
    for linea in f:
        ...
finally:
    f.close()
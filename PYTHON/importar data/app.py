#llamar datos del archivo json desde python
#imprimir todos los salarios que superen los 3000
import json
with open('./db/data.json') as json_file:
    people = json.load(json_file) #people declara el nombre que va llevar el diccionario
    for person in people:
        number_balance = float(person["balance"][1:].replace(",", "")) #replace es una funcion 
        #para reemplazar por ser funcion lleva ()
        if number_balance >= 3000:
            print(number_balance)


#imprimir los nombres de las personas que les gusten las manzanas
# import json

# with open('./db/data.json') as json_file:
#     people = json.load(json_file)
#     for person in people:
#         favorite_fruits = person['favoriteFruit']
#         if favorite_fruits == 'apple':
#             print(person['name'])

#imprime los nombres de los empleados activos
#para buscar inactivos solo hay que agregar not despues del if
# import json

# with open('./db/data.json') as json_file:
#     people = json.load(json_file)
#     for person in people:
#         if person['isActive']:
#             print(person['name'])
     

# imprimir los nombres de las personas que tengan un telefono terminando en 0
# import json

# with open('./db/data.json') as json_file:
#     people = json.load(json_file)
#     for person in people:
#         phone_number = person['phone']
#         last_number = phone_number[-1]
#         if int(last_number) == 0:
#             print(person['name'])



# imprimir las edades mayores de 18 de todos los nombres
# import json

# with open('./db/data.json') as json_file:
#     people = json.load(json_file) 
#     for person in people:
#         if person["age"] >= 18:
#             print(person['age'])

#         else:
#             print(f"{person['age']} = menor de edad")

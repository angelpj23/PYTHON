#para buscar en un modelo que no estoy, me traslado con env = [""]
#Si estoy en modulo de contactos
list = env = ["sale_order"]

list = model.search([], limit = 100)
user = []
for l in list:
    user.append(l.name)
raise Warning(user)
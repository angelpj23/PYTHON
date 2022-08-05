#facturas de contactos con sus vendedores y precios
list = model.search([], limit = 100)
user = []
for l in list:
    user.append(l.partner_id.name + "--su vendedor es--" + str(l.user_id.name) + "--con un total de--" + str(l.amount_total) +"\n")
raise Warning(user)
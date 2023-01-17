# #100 primeros contactos
contacts = model.search([], limit = 100)
raise Warning(contacts)

#----------------------------------------------------------------------------------------------------------
#contactos que tienen telenofos
client = model.search([], limit = 15)
list = []


for cl in client:
  if cl.phone:
    list.append("Client: " + cl.commercial_name + "\n" +"Tel.: "+ str(cl.phone)+ "\n"+ "\n")

raise Warning (list)

#----------------------------------------------------------------------------------------------------------
#numeros de los contactos
contacts = model.search([], limit = 5)
tel = []
for c in contacts:
  tel.append(c.phone)
raise Warning(tel)

#----------------------------------------------------------------------------------------------------------
#llamar emails con limite de 100
list = model.search([], limit = 100)
user = []
for l in list:
    user.append(l.email)
raise Warning(user)
#----------------------------------------------------------------------------------------------------------
#llamar 2 contactos especificos
list = model.search([('id','=', 412) and ('id','=', 212)]).name
raise Warning(list)
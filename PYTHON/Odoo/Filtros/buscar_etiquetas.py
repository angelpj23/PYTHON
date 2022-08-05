# buscar por etiqueta sales desde otro modelo
employees = env["hr.employee"].search([])
tags_contacts = employees.filtered(lambda A: A.category_ids.filtered(lambda B: B.name == "Sales"))
result = []
for tg in tags_contacts:
  result.append(tg.name)
raise Warning(result)
#----------------------------------------------------------------------------------------------------------
# buscar por etiqueta sales
contacts = model.search([])
tags_contacts = contacts.filtered(lambda l: l.category_ids.filtered(lambda m: m.name == "Sales"))
result = []
for tg in tags_contacts:
  result.append(tg.name)
raise Warning(result)
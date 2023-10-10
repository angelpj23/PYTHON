users = model.search([('active', 'in', [True, False])])
for u in users:
  u.write({'lang': 'es_ES'})
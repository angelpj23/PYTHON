lines = model.search([('id','=', 665)])

for l in lines:
  # l.write({'name': l.product_id.name})
  l.write({'quantity': 1})
records= model.search([('id', '=', 5)])
for record in records:
  record.write({'state': 'draft'})
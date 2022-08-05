list= model.search([('id', '=', 5)])

for l in list:
  l.write({'state': 'generated'})

# raise Warning(list)
conduce = model.search([('id', '=',1759)])
# raise Warning(conduce)
for c in conduce:
  for line in c.move_dest_ids:
      line.write({'state': 'draft'})
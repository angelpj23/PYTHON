product = model.search([('id', '=', 1716)])
# raise Warning(product)
for p in product:
  p.write({'rental_status': 'rented'})
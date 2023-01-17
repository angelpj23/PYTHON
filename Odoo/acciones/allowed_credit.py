client = model.search([('id', '=', 4412)])
# raise Warning(product)
for credit in client:
  credit.write({'allowed_credit': True})
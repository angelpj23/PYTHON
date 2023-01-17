compra = model.search([('id', '=', 1879)])
for c in compra:
  for line in c.order_line:
    impuesto = env['account.tax'].search([('id', '=', 6)])
    line.write({'taxes_id': impuesto})
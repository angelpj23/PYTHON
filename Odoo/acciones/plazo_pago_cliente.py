venta = model.search([('partner_id', '=', 'DOMINITRANS EIRL')])

for v in venta:
  v.write({'payment_term_id': 6})
  # el 6 es la posicion de la opcion en el campo tipo selection.
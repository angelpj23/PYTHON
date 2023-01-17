factura = model.search([('id','=',13047)])
# raise Warning(factura)
factura.write({'payment_state': 'not_paid'})
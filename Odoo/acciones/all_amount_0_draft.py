invoices = model.search([('move_type', '=', 'in_invoice'), ('amount_total', '=', 0)])
for i in invoices:
  i.write({'state': 'draft'})
# raise Warning(invoices)

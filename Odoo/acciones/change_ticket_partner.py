tickets = model.search([('partner_id', '=', 170331)])

for t in tickets:
  t.write({'partner_id': 80084})
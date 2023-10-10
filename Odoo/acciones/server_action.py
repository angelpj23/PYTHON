odoobot = record.env.ref('base.user_root')
orders = []
for rec in records:
  if rec.state == 'draft' and rec.workorder_done_count == rec.workorder_count:
    orders.append(rec)
    
if orders:
  for order in orders:
    order.with_user(odoobot).write({'state': 'done'})
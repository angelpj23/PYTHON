# subs = model.search([('id', '=', 63580)])
# for r in subs:
#   for line in r.recurring_invoice_line_ids:
#     line.write({'discount': round(line.discount)})

subs = model.search([]).filtered(lambda x: x.recurring_total > 0.0)
res = []
for s in subs:
  integer, decimal = str(s.recurring_total).split(".")
  if decimal > "0":
    res.append(s)
raise UserError(res)
# for r in res:
#   for line in r.recurring_invoice_line_ids:
#     line.write({'discount': round(line.discount)})
#     line.write({'price_subtotal': round(line.price_subtotal)})
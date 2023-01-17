purchase= model.search([('id', '=', 1515)])
for p in purchase:
  for edit in p.order_line:
    if edit.product_qty == 5:
      edit.write({'qty_received': 5})
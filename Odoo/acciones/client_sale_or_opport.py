clients = model.search([])
sales = []
for c_s in clients:
  if c_s.sale_order_count >= 1 or c_s.opportunity_count >= 1:
    sales.append(c_s.name)
raise Warning(sales) 
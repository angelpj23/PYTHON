sales = model.search([('name', 'like', 'PV/2023%')])
total_sales = []
total_lines = []
for s in sales:
  for ol in s.order_line:
    if not ol.billing_start_date:
      total_sales.append(s)
      total_lines.append(ol)
raise Warning("El total de ventas es: " + str(len(set(total_sales))) + "\n" + "El total de lineas es: " + str(len(set(total_lines))))
#Set para no repetir valores
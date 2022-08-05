#imprimir las compa;ias que tienen ventas
company = model.search([], limit = 500)
sales = []
for c_s in company:
  if c_s.subscr_id:
    sales.append(c_s.commercial_name + "---------" + str(c_s.subscr_id)+"\n")
raise Warning(sales) 

#----------------------------------------------------------------------------------------------------------
#100 empresas que tengan ventas mayor a 50,000
sales = model.search([("amount_total", ">=", 50000)], limit = 100)
names = []
for s in sales:
  names.append(s.partner_id.name + "------" + str(s.amount_total) +"\n")
raise Warning(names)

#----------------------------------------------------------------------------------------------------------

#100 compañias con por lo menos 1 venta. De estas ventas, conseguir los productos que se le vendieron
sales = env["res.partner"].search([])
companies = sales.filtered(lambda client: client.subscr_id and client.sale_order_count)

list = []
bills = []

for s in sales:
  if s["client"] >= 100:
    s.append(bills)
    
for client in companies:
  list.append({
    'company': client.name, 
    'product': client.sale_order_ids[0]
})
  
for l in list:
  join = "////// CLIENT = " + l['company'] + ': \n'

  for line in l['product'].order_line:
    join += "** " + line.product_id.name + " - - - " + "RD$" + str(line.price_subtotal) +'\n'
  
  join += "Total: RD$" + str(l['product'].amount_total) + "\n" + "<--------------------------------------------------------------------------------------------------------------------------------------------------------->" + "\n" + "\n"
  
  bills.append(join)

raise Warning (bills)

#----------------------------------------------------------------------------------------------------------
# 1- Obtener desde el modelo de contactos, limite de 100 compañias con por lo menos 1 venta.
# 2- De estas ventas, conseguir los productos que se le vendieron.
# 3- Listar en el siguiente formato:
#       1 - JUMBO
#           DIAMATE  - 400
#           BANNER CUADRADO - 600
#           Total vendido: 1,000
companies = env['res.partner'].search([], limit = 100)
companies_with_sale = companies.filtered(lambda company: company.subscr_id and company.sale_order_count)
list = []
sale = []

for company in companies_with_sale:
  list.append({
    'company': company.name,
    'product': company.sale_order_ids[0]
  })
for l in list:
  label = "- CLIENTE = " + l['company'] + ': \n'
  
  for line in l['product'].order_line:
    label += "** " + line.product_id.name + " - - - " + "RD$" + str(line.price_subtotal) +'\n'
  
  label += "Total: RD$" + str(l['product'].amount_total) + "\n" +"<--------------------------------------------------------------------------------------------------------------------------------------------------------->" + "\n" + "\n"
  
  sale.append(label)

raise Warning(sale)
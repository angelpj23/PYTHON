manager = model.env["res.users"].search([('id', '=', 222)])
odoobot = model.env["res.users"].search([('id', '=', 1),('active', '=', False)])
bajo_pedido = model.env["stock.location.route"].search([('id', '=', 1)])
fabricar = model.env["stock.location.route"].search([('id', '=', 6)])
products = model.search([]).filtered(lambda x: "Impreso" in x.categ_id.display_name)

for p in products:
  p.with_user(odoobot).write({"purchase_ok": False})
  p.with_user(odoobot).write({"fulfillment_managers": manager})
  p.with_user(odoobot).write({"sale_ok": True})
  p.with_user(odoobot).write({"recurring_invoice": True})
  p.with_user(odoobot).write({"subscription_template_id": 1})
  
for bp in bajo_pedido:
  bajo_pedido_nuevos = list(products.mapped("id"))
  bajo_pedido_existentes = list(bp.product_ids.mapped("id"))
  bajo_pedido_existentes.extend(bajo_pedido_nuevos)
  bp.write({"product_ids":bajo_pedido_existentes})
  
for f in fabricar:
  fabricar_nuevos = list(products.mapped("id"))
  fabricar_existentes = list(f.product_ids.mapped("id"))
  fabricar_existentes.extend(fabricar_nuevos)
  f.write({"product_ids":fabricar_existentes})
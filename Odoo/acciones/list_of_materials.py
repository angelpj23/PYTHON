for record in records:
  if record.bom_count:
    raise UserError("Ya existe una lista de materiales")
  ref = record.default_code or ""
  if ref:
    ref = ref+" - "
  bom = record.env["mrp.bom"].create({"product_tmpl_id": record.id, 
  "product_id": record.product_variant_id.id, 
  "type": "normal", 
  "product_qty": 1
  })
  
  routingworkcenter1 = record.env["mrp.routing.workcenter"].create({
    "name":"{name1}".format(name1=ref+"Creación de Arte Print"),
    "bom_id": bom.id,
    "workcenter_id": 2,
    "time_mode": "auto",
    })
    
  routingworkcenter2 = record.env["mrp.routing.workcenter"].create({
      "name":"{name2}".format(name2=ref+"Auditoría de Anuncio"),
      "bom_id": bom.id,
      "workcenter_id": 11,
      "time_mode": "auto",
      })   
      
  routingworkcenter3 = record.env["mrp.routing.workcenter"].create({
      "name":"{name3}".format(name3=ref+"Validación Cliente"),
      "bom_id": bom.id,
      "workcenter_id": 23,
      "time_mode": "auto",
      })   
  
  routingworkcenter4 = record.env["mrp.routing.workcenter"].create({
      "name":"{name4}".format(name4=ref+"Publicación"),
      "bom_id": bom.id,
      "workcenter_id": 2,
      "time_mode": "auto",
      })
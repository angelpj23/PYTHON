contacts = model.search([('contact_status', '=', 'closed'), ('category_id', '=', 43), ('create_uid', '!=', [1, 2]), 
('sale_order_count', '=', 0), ('active', '=', 0)])
to_delete = []
for rec in contacts:
  rec.new(rec.read([])[0])
  if rec.total_publications == 0:
    raise Warning(rec)
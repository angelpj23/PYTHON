# Etapa: En Seguimiento, Equipo: Account Coordinator Ticket
tickets = model.search([('stage_id.id', '=',16), ('team_id.id', '=',10)])
# Etapa: Resuelto
new_stage = env['helpdesk.stage'].search([('id', '=', 3)])
# Etiqueta de identificacion: Test - IT
tag = env['helpdesk.tag'].search([('id', '=', 178)])
# res = []
for rec in tickets.filtered(lambda ticket: ticket.sale_order_id and not ticket.sale_order_id.billing_active):
  # res.append(rec.id)
# raise Warning(len(res))
    rec.update({'tag_ids': tag})
    rec.write({'stage_id': new_stage.id})
    rec.activity_ids.action_done()
tickets = model.search([('submotive_id.is_lead', '=', True)])
for t in tickets:
  dest_lead_users = t.submotive_id.state_notification_ids.filtered(lambda sni: sni.state_id == t.state_id).mapped('user_ids')
  usuarios_con_ticket = env['res.users'].search([('id', 'in', dest_lead_users.ids)], order='helpdesk_extended_ticket_active_count asc')
  if usuarios_con_ticket: 
    t.write({
      'state_id': t.partner_id.state_id.id, 
      'user_id': usuarios_con_ticket[0].id or t.user_id.id,
    })
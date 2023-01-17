tickets = model.search([])
for ticket in tickets:
  create_uid = ticket.create_uid
  user_team = env['helpdesk.ticket.team'].search([('user_ids', 'in', create_uid.id)])
  if user_team:
    ticket.write({'create_team_id': user_team[0].id})
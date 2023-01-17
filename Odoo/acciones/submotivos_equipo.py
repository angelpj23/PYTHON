team_ids = model.browse([1,2,4,5])
submotive_ids = env['helpdesk.ticket.submotive'].search([])
for team in team_ids:
  team.write({'submotive_ids': [(6, 0, submotive_ids.ids)]})
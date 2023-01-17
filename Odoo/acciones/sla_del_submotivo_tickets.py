tickets = model.search([('submotive_sla', '=', 0.0)])


for t in tickets:
  team_sla = t.submotive_id.submotive_team_sla_ids.filtered(lambda stli: stli.team_id == t.create_team_id)
  t.write({'submotive_sla': (team_sla and len(team_sla) == 1) and team_sla.sla or 0.0})

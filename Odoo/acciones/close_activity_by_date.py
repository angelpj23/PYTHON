activities = model.search([('create_date', '<=', '2022/02/15')])
for act in activities:
  if act.res_id in crm_active:
    act.action_done()
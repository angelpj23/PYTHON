# date of activity
get_date = "2022/03/15"
date_to_clear = dateutil.parser.parse(get_date).date()

activities = model.search([])
for a in activities:
  if a.create_date.date() <= date_to_clear:
    a.unlink()
    
# date of the register
activities = model.search([('create_date', '<=', '2022/02/15')])
for act in activities:
  if act.res_id in crm_active:
    act.action_done()
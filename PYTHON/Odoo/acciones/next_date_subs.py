subscr = model.search([('id', '=', 2)])
# raise Warning(subscr)
for s in subscr:
  s.write({'recurring_next_date': '2022-08-01'})


# %Y-%m-%d
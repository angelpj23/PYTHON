act_account = env = ["account.asset"]
act_account = model.search([('id', '=', 160)])

for act in act_account:
  # act.write({'account_asset_id': '1359'})
  # act.write({'account_depreciation_id': '1395'})
  act.write({'account_depreciation_expense_id': '1574'})
  
  # Id activo 1359
  # Id depreciacion 1395
  # Id gastos 1574
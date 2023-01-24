sales = model.search([('state', 'in', ['draft','sent']), ('name', '>=', 'PV/2023')])
raise Warning(sales)
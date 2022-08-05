# imprimir los contactos que son empresas usando funciones
company = model.search([], limit = 500)
def select_company_only(contact):
  return contact.subscr_id
companies = company.filtered(lambda l: l.subscr_id).mapped('name')
raise Warning(companies) 
#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------
#empresas que tienen ventas con funciones
companies = model.search([], limit=100)

companies = companies.filtered(lambda company: company.subscr_id and company.sale_order_count).mapped('sale_order_ids')

raise Warning(companies)
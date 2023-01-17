partners = env['res.partner'].search([('id', 'in', [4380, 4428])])
raise Warning(partners.mapped('name'))
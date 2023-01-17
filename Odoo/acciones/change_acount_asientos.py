duarte = env['account.analytic.account'].browse([1])

env['sale.subscription'].search([]).write({'analytic_account_id': duarte.id})
env['sale.order'].search([]).write({'analytic_account_id': duarte.id})
lines = env['account.move.line'].search([('move_id.move_type', 'in', ['out_invoice', 'out_refund', 'in_refund', 'in_invoice'])])
lines.write({'analytic_account_id': duarte.id})
# moves = list(set(lines.mapped('move_id')))
# for m in moves:
#   m.mapped('line_ids').create_analytic_lines()
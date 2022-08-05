# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class asignar(models.Model):
    _name = 'asignar.asignar'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100





#  return {
#             'type': 'ir.actions.act_window',
#             'name': '',
#             'view_type': 'form',
#             'view_mode': 'form',
#             'res_model': 'product.input.wizard',
#             'target': 'new',
#             'res_id': wizard_id.id,
#         }

    def act_asignar(self):
        raise ValidationError("funciona!")


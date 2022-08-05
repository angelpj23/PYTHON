from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AsignacionesWizard(models.TransientModel):
    _name = 'asignar.asignar.wizard' #name of the object
    _description = 'Asignar Wizard'

 
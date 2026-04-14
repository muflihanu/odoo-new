from odoo import api,fields,models,tools

class ResUser(models.Model):
    _inherit = "res.users"

    menu_to_hide=fields.Many2many('ir.ui.menu',string='menu')



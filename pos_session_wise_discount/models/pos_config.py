from odoo import api, fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_limit=fields.Float(string="Discount Limit")


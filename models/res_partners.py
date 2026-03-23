from  odoo import api, fields, models

class ResPartners(models.Model):
    _inherit='res.partner'

    restricted_line=fields.Boolean(string="Restricted", default=False)
    restricted_count=fields.Integer(string="Restricted Count")

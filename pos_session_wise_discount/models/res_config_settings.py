from odoo import fields, models,api

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    discount_limit = fields.Float(string="Session Discount Limit",related="pos_config_id.discount_limit",readonly=False)


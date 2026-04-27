from odoo import fields, models, api

class ResPartners(models.Model):
    _inherit='res.partner'

    activate_purchase_limit=fields.Boolean(string="Activate Purchase Limit",default=False)
    purchase_limit=fields.Float(string="Purchase Limit")

    @api.model
    def _load_pos_data_fields(self, config_id):
        data = super()._load_pos_data_fields(config_id)
        data += ['activate_purchase_limit','purchase_limit']
        return data
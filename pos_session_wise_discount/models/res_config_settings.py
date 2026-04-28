from odoo import fields, models,api

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    discount_limit = fields.Float(string="Session Discount Limit")

    @api.model
    def _load_pos_data_fields(self, config_id):
        data = super()._load_pos_data_fields(config_id)
        data += ['discount_limit']
        return data


    @api.model
    def get_values(self):
        """Get the values from settings."""
        res = super(ResConfigSettings, self).get_values()
        limit_sudo = self.env['ir.config_parameter'].sudo()
        discount_limit = limit_sudo.get_param('res.config.settings.discount_limit')
        res.update(discount_limit=discount_limit)
        return res

    def set_values(self):
        """Set the values. The new values are stored in the configuration parameters."""
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'res.config.settings.discount_limit', self.discount_limit)

        return res
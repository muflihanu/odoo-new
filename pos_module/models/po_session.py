from odoo import fields,models,api
class PoSSession(models.Model):
    _inherit = 'pos.session'

    @api.model
    def _load_pos_data_models(self, config):
        data = super()._load_pos_data_models(config)
        if config.module_pos_hr:
            data += ['product.template']
        return data
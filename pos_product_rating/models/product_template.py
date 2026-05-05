from odoo import api, fields, models
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    rating = fields.Selection(selection=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],string="Rating")
    



    @api.model
    def _load_pos_data_fields(self, config_id):
        data = super()._load_pos_data_fields(config_id)
        data += ['rating']
        return data
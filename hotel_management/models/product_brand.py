from odoo import api, fields, models
class ProductBrand(models.Model):
    _name = 'product.brand'
    _inherit = ['pos.load.mixin']
    _description = 'Product Brand'

    name = fields.Char(string='Brand Name')
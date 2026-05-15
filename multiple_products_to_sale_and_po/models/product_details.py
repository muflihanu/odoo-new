from odoo import api, fields, models

class ProductDetails(models.Model):
    _name = "product.details"

    product_id = fields.Many2one('product.product',string="Product")
    product_qty = fields.Float(string="Quantity",default=1)
    select_check=fields.Boolean(string="Select" ,default=False)

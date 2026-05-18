from odoo import fields, models, api
class ProductLines(models.Model):
    _name = "product.liness"
    _description = "Product Lines"
    product_id = fields.Many2one('product.product', string="Product")
    product_image=fields.Image(string="Product Image",related="product_id.image_1920")
    product_qty = fields.Float(string="Quantity",default=1)
    select_check=fields.Boolean(string="Select" ,default=False)
    product_details_id=fields.Many2one('product.details',string="details")

    @api.onchange('product_id')
    def add_qty(self):
        if self.product_id:
            self.product_qty +=1

    @api.onchange('product_id')
    def minus_qty(self):
        if self.product_id:
            self.product_qty -= 1
            if self.product_qty<0:
                self.product_qty = 1

    @api.onchange('product_id')
    def select_product(self):
        if self.product_id:
            self.select_check = True
        return False
from odoo import fields,models,api

class SaleProductWizard(models.TransientModel):
    _name = "sale.product.wizard.line"

    product_id = fields.Many2one('product.product', string="Product")
    product_qty = fields.Float(string="Quantity", default=1.0)
    select_check = fields.Boolean(string="Select", default=False)
    product_image = fields.Image(string="Product Image", related="product_id.image_1920")
    sale_product_wizard_id = fields.Many2one('sale.product.wizard', string="Wizard")

    @api.onchange('product_id')
    def add_qty(self):
        if self.product_id:
            self.product_qty += 1

    @api.onchange('product_id')
    def minus_qty(self):
        if self.product_id:
            self.product_qty -= 1
            if self.product_qty < 0:
                self.product_qty = 1

    @api.depends('product_id')
    def select_product(self):
        if self.product_id:
            self.select_check = True

        return {}


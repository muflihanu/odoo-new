from odoo import api, fields, models

class ProductDetails(models.Model):
    _name = "product.details"
    _description = "Product Details"
    _rec_name = "id"

    purchase_order_id = fields.Many2one('purchase.order',string="Purchase Order")
    product_line_ids=fields.One2many('product.liness','product_details_id',string="Product Lines")





    def add(self):
        if self.product_line_ids:
            for line in self.product_line_ids:
                if line.select_check == True:
                   order=self.env['purchase.order.line'].create({'order_id':self.purchase_order_id.id,'product_id':line.product_id.id,'product_qty':line.product_qty})

        return {
            'type': 'ir.actions.act_window',
            'name': 'purchase_order',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'res_id': self.purchase_order_id.id,
        }

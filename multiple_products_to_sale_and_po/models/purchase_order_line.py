from odoo import fields, models,api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order.line"

    @api.model
    def get_products(self):
        """Retrieving all  the products"""
        products_values = []
        product = self.env["product.product"].search([])
        for pro in product:
            products_values.append(
                {'image': pro.image_1920,'product_id': pro.name, 'pro_id': pro.id, 'product_qty': 0,'price':pro.lst_price,})
        return {'product_values': products_values,}





    def add_product(self):
      """"redirecting to the product details page"""

      return {
        'type': 'ir.actions.client',
        "tag": "purchase_product_details_tag",
        "params": {'order_id':self.env.context.get('order_id') , },
    }



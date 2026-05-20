from odoo import api,fields,models
from odoo import Command

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def get_products(self):
        """Retrieving all  the products"""
        products_values=[]
        product = self.env["product.product"].search([])
        for pro in product:
            products_values.append({'image':pro.image_1920,'product_id': pro.name,'pro_id':pro.id,'product_qty':0,'price':pro.lst_price,})
        return {'product_values': products_values,}


    def add_sale_product(self):
        """"redirecting to the product details page"""
        return {
            'type': 'ir.actions.client',
            "tag": "product_details_tag",
            "params": {'sale_order_id': self.env.context.get('sale_order_id'),},
        }
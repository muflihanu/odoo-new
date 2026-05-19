from odoo import api,fields,models
from odoo import Command

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def get_products(self):
        products_values=[]
        product = self.env["product.product"].search([])
        for pro in product:
            products_values.append({'image':pro.image_1920,'product_id': pro.name,'pro_id':pro.id,'product_qty':0})
        return {'product_values': products_values,}


    def add_sale_product(self):

        print('hello this is client action')
        order = self.env["sale.order"].browse(self.env.context.get('sale_order_id'))


        return {
            'type': 'ir.actions.client',
            "tag": "product_details_tag",
            "params": {'sale_order_id': order.id,},
        }
from odoo import fields, models
from odoo import Command

class PurchaseOrder(models.Model):
    _inherit = "purchase.order.line"




    def add_product(self):
        pro=[]
        order=self.env["purchase.order"].browse(self.env.context.get('order_id'))
        product=self.env["product.product"].search([])
        product_details=self.env['product.details'].create({
            'purchase_order_id':order.id,
            'product_line_ids':[Command.create({
                'product_id':pr.id,
                 'product_qty':0,
                  'select_check':False,
            })for pr in product] })
        return {
        'type': 'ir.actions.act_window',
        'name': 'product',
        'view_mode': 'form',
        'res_model': 'product.details',
        'res_id': product_details.id,
        'target': 'current'
    }



from odoo import fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order.line"




    def add_product(self):
        order=self.env["purchase.order"].browse(self.env.context.get('order_id'))
        print('helloooo',order)
        print('wwww',self.read())

    def action_add_from_catalog(self):
        order = self.env['purchase.order'].browse(self.env.context.get('order_id'))
        print('catalog',order.id)
        return super(PurchaseOrder,self).action_add_from_catalog()

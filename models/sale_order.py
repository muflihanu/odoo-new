from odoo import fields,models,api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit='sale.order'

    state=fields.Selection(selection_add=[('open','Open'),('close','Close'),('cancel','Cancel')],string='status')


    def close_record(self):
            self.state='close'

    def open_record(self):
         delivery_qty=0
         product_qty=0
         for qty in self.order_line:
             delivery_qty+=qty.qty_delivered
             product_qty+=qty.product_uom_qty

         if self.state=='close' and product_qty!=delivery_qty:
             self.state='open'
         else:
            raise UserError('all the products are delivered.')


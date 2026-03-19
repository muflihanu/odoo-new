from odoo import api, fields, models
from odoo import Command

class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "Account Move"

    # partner_id=fields.Many2one('res.partner',string='vendor')
    # date=fields.Date( default=fields.Date.context_today)



    def purchase_order(self):
       self.ensure_one()
       if self.move_type != 'in_invoice':
           return False

       vals={
           'bill_id':self.id,
           'partner_id':self.partner_id.id,
           'date_order':fields.Date.today(),
           'order_line':[Command.create({
               'product_id':line.product_id.id,
               'product_qty':line.quantity,
               'price_unit':line.price_unit,

           })for line in self.invoice_line_ids]
       }


       orders=self.env['purchase.order'].create(vals)
       return {

        'type': 'ir.actions.act_window',
        'move_type': 'in_invoice',
        'name': 'order',
        'view_mode': 'form,list',
        'res_model': 'purchase.order',
        'res_id': orders.id,
    }



    def pet_purchase_order(self):
       self.ensure_one()
       print("ds", self.id)
       purchase_id=self.env['purchase.order'].search([('bill_id','=',self.id),('state','=','purchase')])
         # print(purchase_id.read())
       # print(self.read())
       # p=self.env['purchase.bill.line.match'].search([('partner_id','=',self.partner_id.id)])
       # print(p.read())
       return {
           'type': 'ir.actions.act_window',
           'name': 'order',
           'view_mode': 'form,list',
           'res_model': 'purchase.order',
           'res_id': purchase_id.id,

       }







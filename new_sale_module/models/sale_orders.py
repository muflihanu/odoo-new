from odoo import api,fields,models
from odoo.exceptions import UserError

class SaleOrders(models.Model):

    _inherit = 'sale.order'

    delivery_remark=fields.Text(string="Delivery Remark" ,copy=False)
    is_urgent_delivery=fields.Boolean(string="Is Urgent Delivery",default=False,copy=False)
    preferred_delivery_time=fields.Selection(selection=[('morning','Morning'),('afternoon','Afternoon'),('evening','Evening')])
    discount_approved=fields.Boolean(string="Discount Approved",default=False,copy=False)
    discount_approved_by=fields.Many2one('res.users',string="Discount Approved By",copy=False)
    flag=fields.Boolean(string="Flag",default=False,copy=False)


    def discount_approved_sale(self):
        if self.order_line:
            for r in self.order_line:
                if r.discount>0:
                    self.flag=True

            if self.flag==True:
                self.discount_approved = True
                self.discount_approved_by = self.env.user.id
                self.message_post(
                        body=f'discount_approved {self.discount_approved_by.name}')
            else:
                raise UserError("must have discount")
        else:
            raise UserError("must have order_line")


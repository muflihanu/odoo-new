from odoo import api,fields,models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    state=fields.Selection(selection_add=[('approve','Approve'), ('sale', "Sales Order")])



    def action_confirm(self):
        for record in self:
            if  record.amount_total>1000:
                     record.write({'state': 'approve'})
                     print(record.state)
                     self.env.cr.commit()
                     raise ValidationError('this sale order  need approval!!')

        return super(SaleOrder,self).action_confirm()








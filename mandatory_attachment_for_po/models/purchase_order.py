from odoo import fields,models,api
from odoo.exceptions import ValidationError
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
     """mandatory attachment for Purchase Order"""
     for rec in self:
         flag = False
         if rec.company_id.mandatory_attachment_for_po:
             attach_val=self.env['ir.attachment'].search([('res_model','=','purchase.order'),('res_id','=',rec.id)])
             if attach_val:
                 for attach in attach_val:

                    if attach.mimetype =='image/jpg' or attach.mimetype =='application/pdf' :
                        flag = True
                        break

                 if flag == False:
                      raise ValidationError('Mandatory Attachment for Purchase Order not found')
             else:
                raise ValidationError('Mandatory Attachment for Purchase Order not found')
     return super(PurchaseOrder, self).button_confirm()


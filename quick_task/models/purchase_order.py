from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    restricted_count=fields.Integer("Restricted Count",related="partner_id.restricted_count")
    restricted_lines=fields.Boolean("Restricted Lines",related="partner_id.restricted_line")



    @api.onchange('order_line','restricted_count')
    def onchange_order_line(self):
        if self.restricted_count!=0:
            if len(self.order_line)>self.restricted_count and len(self.order_line)!=0:
                raise ValidationError('order lines limit reached!!')


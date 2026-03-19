from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    bill_id=fields.Many2one('account.move',string="Bill_id")
    # bill_id=fields.Integer(string="Bill ID")

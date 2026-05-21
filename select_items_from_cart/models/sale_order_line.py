from odoo import  fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    select_check=fields.Boolean(string="Check",default=False)
from odoo import api,fields,models

class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.price_subtotal', 'currency_id', 'company_id', 'payment_term_id','order_line.select_check')
    def _compute_amounts(self):

        return super(sale_order,self)._compute_amounts()

    def _get_priced_lines(self):

        return self.order_line.filtered(lambda x: not x.display_type and x.select_check)
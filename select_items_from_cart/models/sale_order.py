from odoo import api,fields,models

class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.price_subtotal', 'currency_id', 'company_id', 'payment_term_id','order_line.select_check')

    def _compute_amounts(self):
        """compute total amount with selected orders"""
        return super(sale_order,self)._compute_amounts()

    def _get_priced_lines(self):
        prices=[]
        for line in self.order_line:
            if line.select_check:
                prices.append(line)
        return prices



    def _is_cart_ready(self):
        """check if cart is ready"""
        flag=False
        if self.order_line:
            for rec in self.order_line:
                if rec.select_check == True:
                    flag=True
            if flag == True:
                return True
            else:
                return False
        return super(sale_order,self)._is_cart_ready()

from odoo.http import request, route
from odoo import http

class ProductCheck(http.Controller):
 @http.route('/selected_orders' ,type='jsonrpc' ,auth='public' ,website=True)
 def product_check(self ,check,order_id):
    sale_order = request.cart
    untaxed_amount = sale_order.amount_untaxed
    print('untaxed_amount',untaxed_amount)
    print(check)
    print(order_id)
    order =self.env['sale.order.line'].browse(int(order_id))
    order.write({'select_check':check})
    print('check',order.select_check)
    # untaxed_amount += order.price_subtotal
    # sale_order.write({'amount_untaxed':untaxed_amount, 'amount_tax': 0, 'amount_total': 0})

    # sale_order.write({})
    print('amount',sale_order.amount_untaxed)


 @http.route('/select/all' ,type='jsonrpc' ,auth='public' ,website=True)
 def select_all(self):
     select=request.cart
     print('cart',select.website_order_line.read())
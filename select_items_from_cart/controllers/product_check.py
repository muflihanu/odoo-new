from odoo.http import request, route
from odoo import http

class ProductCheck(http.Controller):
 @http.route('/selected_orders' ,type='jsonrpc' ,auth='public' ,website=True)
 def product_check(self ,check,order_id):
    print('mm',request)
    print(check)
    print(order_id)
    order =self.env['sale.order.line'].browse(int(order_id))
    order.write({'select_check':check})
    print(order.read())
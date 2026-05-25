from odoo.http import request, route
from odoo import http

class ProductCheck(http.Controller):
 @http.route('/selected_orders' ,type='jsonrpc' ,auth='public' ,website=True)
 def product_check(self ,check,order_id):
    """retrieving selected order lines"""
    order =self.env['sale.order.line'].browse(int(order_id))
    order.write({'select_check':check})

 @http.route('/select/all' ,type='jsonrpc' ,auth='public' ,website=True)
 def select_all(self,order_line_ids):
     """retrieving all  selected order lines"""
     for line in order_line_ids:
         order = self.env['sale.order.line'].browse(int(line))
         order.write({'select_check':True})
         print (order.select_check,order)

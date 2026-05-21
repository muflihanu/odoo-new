from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route
from odoo import Command
class WebCartController(WebsiteSale):



    @route()
    def shop_checkout(self, try_skip_step=False, **query_params,):
        order_sudo = request.cart
        print('request',request.cart)
        order_lines=[]
        print('hello this is checkout func', **query_params )
        for order in order_sudo.website_order_line:
            if order.select_check==True:
                  sale_order = order.order_id
                  order_lines.append({'product_id':order.product_id.id,'product_qty':order.product_qty,'price_unit':order.price_unit,})
                  print(sale_order)
                  # print(order.read())
        # new_order=self.env['sale.order'].create({'partner_id':order_sudo.partner_id.id,'website_order_line':[Command.create({
        #     'product_id': order.product_id,
        #     'product_qty': order.product_qty,
        #      'price_unit': order.price_unit,
        # }) for order in order_lines]})
        # if redirection := self._check_cart_and_addresses(new_order):
        #             return redirection


        return super().shop_checkout(try_skip_step=try_skip_step, query_params=query_params)


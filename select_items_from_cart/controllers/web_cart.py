from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route
from odoo import Command

class WebCartController(WebsiteSale):



    @route()
    def shop_checkout(self, try_skip_step=False, **query_params,):
        unchecked_orders=[]
        selected_order = request.cart
        print('before',request.cart.read())
        for order in selected_order.website_order_line:
            print('order',order.read())

            if order.select_check!=True:
                    unchecked_orders.append(order)
                    order.unlink()

        print('deleted orders',unchecked_orders)

        print('after',request.cart.read())


        return super().shop_checkout(try_skip_step=try_skip_step, query_params=query_params)


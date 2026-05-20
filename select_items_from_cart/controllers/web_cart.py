from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route
class WebCartController(WebsiteSale):

    @route()
    def shop_checkout(self, try_skip_step=False, **query_params,):
        order_sudo = request.cart
        print('hello this is checkout func', order_sudo.read())
        for order in order_sudo.order_line:
            print(order.name)

        return super().shop_checkout(try_skip_step=try_skip_step, query_params=query_params)
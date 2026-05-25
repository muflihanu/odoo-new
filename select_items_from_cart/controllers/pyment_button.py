from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.controllers import portal as payment_portal
from odoo.addons.sale.controllers import portal as sale_portal
from odoo.tools.translate import LazyTranslate, _
from odoo import Command
from odoo.http import request, route


class PymentButton(payment_portal.PaymentPortal):



    def _get_shop_payment_values(self,order, **kwargs):
        """create the next sale order with ecxisting order lines"""
        selected_order = request.cart
        result=super(PymentButton,self)._get_shop_payment_values(selected_order, **kwargs)
        unchecked_orders=[]
        for order in selected_order.website_order_line:
            if order.select_check!=True:
                    unchecked_orders.append(Command.create({'product_id':order.product_id.id}))
                    print(order.product_id.name)
                    order.unlink()
        if unchecked_orders:
          cart = request.website._create_cart()
          cart.order_line=unchecked_orders
        return result
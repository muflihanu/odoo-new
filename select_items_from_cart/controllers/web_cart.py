from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route
from odoo import Command
from odoo.tests import result


class WebCartController(WebsiteSale):


    @route()
    def shop_checkout(self, try_skip_step=False, **query_params,):
        result = super(WebCartController,self).shop_checkout(try_skip_step=try_skip_step, query_params=query_params)
        return result

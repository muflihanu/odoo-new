
from odoo.http import request, route
from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.controllers.portal import PaymentPortal
from odoo.addons.sale.controllers.portal import CustomerPortal
from odoo.addons.website_sale.controllers.main import WebsiteSale

class Cart(PaymentPortal):


  @route(route='/shop/cart', type='http', auth='public', website=True, sitemap=False)
  def cart(self, id=None, access_token=None, revive_method='', **post):


      return super().cart(id, access_token, revive_method, **post)

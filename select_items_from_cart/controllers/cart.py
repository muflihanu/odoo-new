from werkzeug.exceptions import NotFound

from odoo import fields
from odoo.exceptions import UserError
from odoo.http import request, route
from odoo.tools import consteq
from odoo.tools.image import image_data_uri
from odoo.tools.translate import _

from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.controllers.portal import PaymentPortal
from odoo.addons.sale.controllers.portal import CustomerPortal
from odoo.addons.website_sale.controllers.main import WebsiteSale

class Cart(PaymentPortal):


  @route(route='/shop/cart', type='http', auth='public', website=True, sitemap=False)
  def cart(self, id=None, access_token=None, revive_method='', **post):
      print('heeeellooo')
      total=0
      if request.cart:
          sale_order=request.cart
          for cart in sale_order.website_order_line:
              if cart.select_check==False:
                  print(sale_order.read())
                  sale_order.write({'amount_untaxed':0,'amount_tax':0,'amount_total':0})
              # else:
              #    total+=cart.price_subtotal
              #    sale_order.write({'amount_untaxed': total, 'amount_tax': 0, 'amount_total': 0})

              print('totals',cart.price_subtotal)
      else:
            print('no cart')
      return super().cart(id, access_token, revive_method, **post)

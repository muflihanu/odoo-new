from odoo import http
from odoo.http import request


class hotelAccommodationWebpage(http.Controller):
    """hotel accommodation webpage controller making room booking"""

    @http.route('/hotel_accommodations', type='http', auth='user', website=True)
    def hotel_accommodation_webpage(self):
        print("djg")
        user_name=request.env.user.name if request.env.user.id else 'Guest'
        return request.render('hotel_management.hotel_accommodation_webpage_snippet'
       )
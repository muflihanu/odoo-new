from odoo import http
from odoo.http import request


class hotelAccommodationWebpage(http.Controller):
    """hotel accommodation webpage controller making room booking"""

    @http.route('/hotel_accommodations', type='http', auth='user', website=True)
    def hotel_accommodation_web_form(self):
        print('hello')

        return request.render('hotel_management.hotel_accommodation_booking_template')

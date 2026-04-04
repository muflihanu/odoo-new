from odoo import http
from odoo.http import request


class hotelAccommodationWebpage(http.Controller):
    """hotel accommodation webpage controller making room booking"""

    @http.route('/hotel_accommodations', type='http', auth='user', website=True)
    def hotel_accommodation_web_page(self):
        print('hello')

        return request.render('hotel_management.hotel_accommodation_booking_template')

    @http.route('/hotel_form', type='jsonrpc', auth='user', website=True)
    def hotel_accommodation_web_form(self,data):
        print('data', data)
        self.env['hotel.accommodation'].create({
            'check_in':data['check_in'],
            'expected_days':data['expected_days'],
            'bed_type':data['bed_type'],
        })
        return request.render('hotel_management.room_booking_success_template')

    @http.route('/room_booking_success_page', type='http', auth='user', website=True)
    def room_booking_success_page(self):
        return request.render('hotel_management.room_booking_success_template')
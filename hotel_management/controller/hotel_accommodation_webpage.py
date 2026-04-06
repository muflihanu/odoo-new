from odoo import http
from odoo.http import request
import base64


class hotelAccommodationWebpage(http.Controller):
    """hotel accommodation webpage controller making room booking"""

    @http.route('/hotel_accommodations', type='http', auth='user', website=True)
    def hotel_accommodation_web_page(self):
        print('hello')

        return request.render('hotel_management.hotel_accommodation_booking_template')

    @http.route('/hotel_form', type='jsonrpc', auth='user', website=True)
    def hotel_accommodation_web_form(self,data_value,attachment_value):
        print('data', data_value)
        print('attachment_value', attachment_value)
        booking_id=self.env['hotel.accommodation'].create({
            'check_in':data_value['check_in'],
            'expected_days':data_value['expected_days'],
            'bed_type':data_value['bed_type']
        })
        print(attachment_value)
        print(booking_id.id,'booking id')
        file=self.env['ir.attachment'].create({'res_model':'hotel.accommodation','res_id':booking_id.id,'type': 'binary','name': attachment_value['name'],'datas':attachment_value['data'],})
        print(file.read())
        return {'result':True}
    @http.route('/room_booking_success_page', type='http', auth='user', website=True)
    def room_booking_success_page(self):
        return request.render('hotel_management.room_booking_success_template')
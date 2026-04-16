from xxlimited_35 import Null

from odoo import http
from odoo.http import request
from odoo import Command
import base64


class hotelAccommodationWebpage(http.Controller):
    """hotel accommodation webpage controller making room booking"""

    @http.route('/hotel_accommodations', type='http', auth='user', website=True)
    def hotel_accommodation_web_page(self):

        return request.render('hotel_management.hotel_accommodation_booking_template')




    @http.route('/hotel_form', type='jsonrpc', auth='user', website=True)
    def hotel_accommodation_web_form(self,data_value,attachment_value):

        guests=[]
        if data_value['other_guest']!=False:
           for val in data_value['other_guest']:
            guests.append(int(val))
           booking_id = self.env['hotel.accommodation'].create({
               'guest_id': data_value['partner'],
               'check_in': data_value['check_in'],
               'expected_days': data_value['expected_days'],
               'bed_type': data_value['bed_type'],
               'guest_no': data_value['count'],
               'other_guest_ids': [Command.create({'Guest_name': int(rec)}) for rec in guests],
           })
        else:
            booking_id = self.env['hotel.accommodation'].create({
                'guest_id': data_value['partner'],
                'check_in': data_value['check_in'],
                'expected_days': data_value['expected_days'],
                'bed_type': data_value['bed_type'],
                'guest_no': data_value['count'],
            })


        print(attachment_value)
        print(booking_id.id,'booking id')
        file=self.env['ir.attachment'].create({'res_model':'hotel.accommodation','res_id':booking_id.id,'type': 'binary','name': attachment_value['name'],'datas':attachment_value['data'],})
        print(file.read())
        return {'result':True}
    @http.route('/room_booking_success_page', type='http', auth='user', website=True)
    def room_booking_success_page(self):
        return request.render('hotel_management.room_booking_success_template')
from odoo import http
from odoo.http import request
from odoo import Command

class RoomBookingThroughRooms(http.Controller):
    @http.route('/types_rooms', type='jsonrpc', auth='user', website=True)
    def available_rooms_settings(self, room_type):
        rooms_list = []
        print('room yty', room_type)
        rooms = self.env['hotel.rooms'].search([('bed', '=', room_type)])
        for room in rooms:
            rooms_list.append(room.room_no)
        print(rooms_list)
        return rooms_list

    @http.route('/facilityss_rooms', type='jsonrpc', auth='user', website=True)
    def facility_based_rooms(self, facility, room_type):
        facility_rooms_list = []
        print('room yty', facility)
        rooms = self.env['hotel.rooms'].search([('facility_id', '=', int(facility)), ('bed', '=', room_type)])
        print(rooms)
        for room in rooms:
            facility_rooms_list.append(room.room_no)
        return facility_rooms_list

    @http.route('/room_booking_through_rooms_template/<int:room_id>/<string:room_type>/<string:room_facility>/<int:facility_id>', type='http', auth='user', website=True)
    def hotel_accommodation_web_page_room(self,room_id,room_type,room_facility,facility_id):
        """room default values"""
        room_no=self.env['hotel.rooms'].browse([room_id])
        print(room_no.room_no)

        return request.render('hotel_management.room_booking_through_rooms_template',{'type':room_type,'room_facility':room_facility,'room_no':room_no.room_no,'facility_id':int(facility_id),'room_id':room_id})



    @http.route('/hotel_form_rooms', type='jsonrpc', auth='user', website=True)
    def hotel_accommodation_web_form(self, data_value, attachment_value):
        facility_val=[]
        facility_num=0
        room_id=0
        for facility in data_value['facilities_ids']:
            facility_num=int(facility)
        for room in data_value['room_id']:
            room_id=int(room)

        print('facilities',data_value['facilities_ids'])
        for val in   self.env['hotel.facility'].browse(facility_num):
            facility_val.append(val.id)

        guests = []
        if data_value['other_guest'] != False:
            for val in data_value['other_guest']:
                guests.append(int(val))
            booking_id = self.env['hotel.accommodation'].create({
                'guest_id': data_value['partner'],
                'check_in': data_value['check_in'],
                'expected_days': data_value['expected_days'],
                'bed_type': data_value['bed_type'],
                'guest_no': data_value['count'],
                'facilities_ids':[Command.create({'facility': rec}) for rec in facility_val],
                'room_id': room_id,
                'other_guest_ids': [Command.create({'Guest_name': int(rec)}) for rec in guests],
            })
        else:
            booking_id = self.env['hotel.accommodation'].create({
                'guest_id': data_value['partner'],
                'check_in': data_value['check_in'],
                'expected_days': data_value['expected_days'],
                'bed_type': data_value['bed_type'],
                'guest_no': data_value['count'],
                'facilities_ids':facility_val,
                'room_id':room_id,
            })

        print(attachment_value)
        print(booking_id.id, 'booking id')
        file = self.env['ir.attachment'].create(
            {'res_model': 'hotel.accommodation', 'res_id': booking_id.id, 'type': 'binary',
             'name': attachment_value['name'], 'datas': attachment_value['data'], })
        print(file.read())
        return {'result': True}
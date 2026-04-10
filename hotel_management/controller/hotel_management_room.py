from odoo import http
from odoo.http import request

class HotelManagementRoom(http.Controller):

  @http.route('/rooms',type='http',auth="user",website=True)
  def hotel_rooms(self):
        return request.render("hotel_management.hotel_rooms_template")
  @http.route('/hotel_management_room', type='jsonrpc', auth='user', website=True)
  def hotel_management_room_sp(self):
     
      available_rooms=request.env['hotel.rooms'].search([('state','in','available')])
      values=[]
      for room in available_rooms:
               values.append(({'room_no':room.room_no,'room_type':room.bed,'room_rent':room.rent,'room_facility':room.facility_id.facility,'image':room.room_image}))
      return values
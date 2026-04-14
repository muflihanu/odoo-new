from odoo import http
from odoo.http import request

class HotelManagementRoom(http.Controller):
  """fetching available rooms"""
  @http.route('/rooms',type='http',auth="user",website=True)
  def hotel_rooms(self):
        return request.render("hotel_management.hotel_rooms_template")
  @http.route('/hotel_management_room', type='jsonrpc', auth='user', website=True)
  def hotel_management_room_sp(self):
     
      available_rooms=request.env['hotel.rooms'].search([('state','in','available')])
      values=[]
      for room in available_rooms:
               values.append(({'room_no':room.room_no,'room_type':room.bed,'room_rent':room.rent,'room_facility':room.facility_id.facility,'image':room.room_image,'room_id':room.id}))
      return values

  @http.route('/details/<int:room_id>', type='http', auth="user", website=True)
  def hotel_rooms_details(self,room_id):
      """specific room images attached to the chatter"""
      room_images=[]
      room_details=request.env['ir.attachment'].search([('res_model','=','hotel.rooms'),('res_id','=',room_id)])
      print('room',room_id)
      for img in room_details:
          room_images.append(img)
          print(img)

      return request.render("hotel_management.hotel_roomdetails_template",{'room_id':room_id,'room_images':room_images})
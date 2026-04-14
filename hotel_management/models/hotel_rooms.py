from email.policy import default

from odoo import fields,models,api

class HotelRooms(models.Model):
    _name='hotel.rooms'
    _description='hotel rooms'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name ='room_no'

    room_no=fields.Integer(string='Room Number')
    bed=fields.Selection(selection=[('single','Single'),('double','Double'),('dormitory','Dormitory')],string='Bed')
    available_beds=fields.Integer(string='Available Beds')
    rent=fields.Float(string='Rent')
    state=fields.Selection(selection=[('available','Available'),('not available','Not Available')],string='State',store=True,default='available')
    facility_id=fields.Many2one('hotel.facility',string='Facility')
    # hotel_accommodation_ids=fields.One2many('hotel.accommodation','room_id',string='Accommodations')
    user_id = fields.Many2one( 'res.users',string='User', default=lambda self: self.env.user.id)
    company_id = fields.Many2one('res.company', string='user', default=lambda self: self.env.company.id)
    room_image=fields.Image(string='Room Image')






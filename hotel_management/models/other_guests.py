from odoo import api,fields,models

class OtherGuests(models.Model):
    _name='other.guests'
    _description = 'Other Guests'

    Guest_name=fields.Many2one('res.partner',string='Guest')
    gender=fields.Selection(selection=[('male','Male'),('female','Female')],string='Gender')
    age=fields.Integer(string='Age')
    accommodation_id=fields.Many2one('hotel.accommodation')

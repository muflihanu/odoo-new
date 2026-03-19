from odoo import api,fields,models

class HotelGuests(models.Model):
    _inherit = 'res.partner'

    hotel_guests=fields.Boolean(string="Hotel Guests", default=False)
    # partners=fields.Boolean(string="Hotel Guests")

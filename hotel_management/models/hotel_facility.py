from odoo import fields,models,api

class HotelFacility(models.Model):
    _name='hotel.facility'
    _description='hotel facility'
    _rec_name='facility'

    facility=fields.Char(string='Facility')
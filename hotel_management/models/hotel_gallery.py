from odoo import fields,models,api


class HotelGallery(models.Model):
    _name = 'hotel.gallery'
    _description = 'Hotel Gallery'
    _rec_name = 'gallery_images'

    gallery_images=fields.Image(string='Hotel Image')


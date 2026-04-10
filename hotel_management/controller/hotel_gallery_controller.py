from odoo import http
from odoo.http import request

class HotelGalleryController(http.Controller):
    @http.route('/gallery',type='jsonrpc',auth='user',website=True)
    def get_gallery(self):
        img=[]
        images=request.env['hotel.gallery'].sudo().search([])
        for image in images:
            img.append({'image':image.gallery_images})
        print('image>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',img)

        return img
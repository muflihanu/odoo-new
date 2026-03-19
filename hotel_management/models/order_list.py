from odoo import api,fields,models

class OrderList(models.Model):
    _name='order.list'
    _description='Order List'



    order_name=fields.Char(string='Order Name')
    order_description=fields.Char(string='Order Description')
    quantity=fields.Integer(string='Quantity')
    order_food_id=fields.Many2one('order.food',string='Order Food')
    subtotal=fields.Float(string='Sub Total')
    unit_price=fields.Float(string='Unit Price')
    total_p=fields.Float(string='Total Price',compute='_compute_total')

    # room_rent_id=fields.Many2one('hotel.room',string='Room Rent')
    # accommodation_id=fields.Many2one('hotel.accommodation',string='Accommodation')
    # order_food_id=fields.Char(string='Order Food')
    @api.depends('subtotal')
    def _compute_total(self):
        for record in self:
            if record.subtotal:
                 record.total_p+=record.subtotal

            else:
               record.total_p=None

    @api.depends('subtotal')
    def _compute_total(self):
        for record in self:
            if record.subtotal:
                record.total_p+=record.subtotal




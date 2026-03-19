from odoo import api, fields, models
from datetime import datetime
from datetime import timedelta


def default_datetime():
    date = fields.Datetime.now()
    return date

class OderFood(models.Model):
    _name = 'order.food'
    _description = 'Order Food'
    _rec_name = 'accommodation_id'



    accommodation_id=fields.Many2one('hotel.accommodation',string='Accommodation',ondelete='cascade')
    # accommodation_room_id=fields.Many2one('hotel.rooms',string='Room',related='accommodation_id.room_id')
    # accommodation_guests_ids=fields.Many2many('',string='Guests',related='accommodation_id.guest_id')
    # accommodation_room=fields.Char(string='Room',compute='_compute_accommodation_room_id')
    accommodation_room=fields.Many2one('hotel.rooms',string='Room',compute='_compute_accommodation_room_id')
    accommodation_guest=fields.Char(string='Guest',compute='_compute_accommodation_guest')
    order_time = fields.Datetime(string='Order Time',default=default_datetime())
    food_related_category_ids=fields.Many2many('food.category',string='Category')
    # food_items_idssss=fields.Many2many('food.items',string='Food Items')
    food_items_menus_ids=fields.Many2many('food.items',string='Food Items',store=True)
    # food_items_menus_ids=fields.One2many('food.items','food_order_id',string='Menus Items',)
    order_list_ids=fields.One2many('order.list','order_food_id',string='Order List')
    total_price=fields.Float(string='Total',compute='_compute_total_price')
    # food_expense=fields.Float(string='Expense',compute='_compute_food_expense')
    # rent_total=fields.Float(string='Rent',compute="_compute_rent_total")
    # payment_id=fields.Many2one('food.payment',string='Payment')
    order_reference_number=fields.Char(string='Order Reference',default='New')
    # expence_name=fields.Char(string='Order Description',default='food expense')
    # order_qty=fields.Integer(string='Order Quantity')
    state=fields.Selection(selection=[('draft','Draft'),('confirm','Confirm')],default='draft')
    user_id = fields.Many2one('res.users', string='user',default=lambda self: self.env.user.id)
    company_id = fields.Many2one('res.company', string='user', default=lambda self: self.env.company.id)

    @api.depends('accommodation_id')
    def _compute_rent_total(self):
        for record in self:

            if record.accommodation_id.state == 'check-out':
                check_in = record.accommodation_id.check_in.day
                check_out = record.accommodation_id.check_out.day
                total_days = check_out - check_in
                if total_days == 0:
                    record.rent_total = record.accommodation_id.room_id.rent
                else:
                    record.rent_total = total_days * record.accommodation_id.room_id.rent
            else:
                record.rent_total = 0

    @api.depends('order_list_ids', )
    def _compute_total_price(self):
        for record in self:
            total = 0
            for i in record.order_list_ids:

                if i.subtotal:
                    total += i.subtotal
                    print('total', total)
                else:
                    i.subtotal = 0
                    record.total_price = 0
            record.total_price = total
            print('total_price', record.total_price)

    @api.depends('accommodation_id')
    def _compute_accommodation_room_id(self):
        for order in self:
            order.accommodation_room = order.accommodation_id.room_id.id

    @api.depends('accommodation_id')
    def _compute_accommodation_guest(self):
        for order in self:
            order.accommodation_guest = order.accommodation_id.guest_id.name

    @api.onchange('food_related_category_ids')
    def _onchange_food_items(self):

        for order in self:

            if order.food_related_category_ids:
                available_food = []

                all_foods = self.env['food.items'].search([('category_id', '=', order.food_related_category_ids)])
                for i in all_foods:
                    available_food.append(i.id)
                order.write({'food_items_menus_ids': [(6, 0, available_food)]})

    def confirm_order(self):
        products=self.env['product.template'].search([('name','=','Food expense')])
        self.state='confirm'

        vals={
            'accommodation_id':self.accommodation_id.id,
            'products':products.id,
            'quantity':1,
            'unit_price':self.total_price,
            'subtotal':self.total_price,
        }

        self.env['order.expense'].create(vals)

        return{
            'name': ' product',
            'view_mode': 'form',
            'res_model': 'order.food',
            'type': 'ir.actions.act_window',
            'res_id':self.id,
            'target': 'current',
        }


    @api.model_create_multi
    def create(self,vals):
        for record in vals:
            record['order_reference_number']=self.env['ir.sequence'].next_by_code('order.reference')
            return super().create(vals)


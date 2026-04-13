import typing

from odoo import fields,models,api
from datetime import timedelta,datetime
from odoo.exceptions import ValidationError
from odoo import Command


class  HotelAccommodation(models.Model):
    _name='hotel.accommodation'
    _description='hotel accommodation'
    _rec_name = 'reference_number'
    _inherit=['mail.thread','mail.activity.mixin']
    _order = 'check_in desc'


    active = fields.Boolean(string='active', default=True)
    reference_number=fields.Char(string='Reference Number',copy=False,readonly=True,default='New' ,tracking=True)
    guest_id=fields.Many2one('res.partner',string='Guest',tracking=True)
    guest_no=fields.Integer(string='No of Guest',defauilt=1,tracking=True)
    # other_guest_ids=fields.Many2many('res.partner',string='Other Guest',tracking=True)
    # check_in=fields.Datetime(string='Check In',tracking=True)
    check_in=fields.Date(string='Check In',tracking=True)
    # today=fields.Datetime(string='Today',tracking=True, default=datetime.today())
    # check_out=fields.Datetime(string='Check Out',tracking=True)
    check_out=fields.Date(string='Check Out',tracking=True)
    bed_type= fields.Selection(selection=[('single', 'Single'), ('double', 'Double'), ('dormitory', 'Dormitory')], string='Bed Type',tracking=True,required=True)
    # available_facilities_ids=fields.Many2many( 'hotel.facility',string='Available Facilities',tracking=True,required=True)
    facilities_ids=fields.Many2many('hotel.facility',string='Facilities',tracking=True)
    bed_type_base_rooms_ids = fields.Many2many('hotel.rooms', string='Bed Type', tracking=True, compute="_compute_bed_type_base_rooms_id")
    room_id=fields.Many2one('hotel.rooms',string='Room',tracking=True)
    state=fields.Selection(selection=[('draft','Draft'),('check-in','Check-In'),('check-out','Check-Out'),('cancel','Cancel')],string='State',default='draft',tracking=True)
    payment_status=fields.Selection(selection=[('not_paid','Not_paid'),('paid','Paid')],default='not_paid')
    identification_proof=fields.Binary(string='Identification Proof')
    expected_days=fields.Integer(string='Expected Days',tracking=True,default=1)
    # cancel_date=fields.Datetime(string='cancel Date',tracking=True,default='2026-03-07')
    cancel_date=fields.Date(string='cancel Date',tracking=True,)
    expected_date=fields.Date(string='Expected Days',tracking=True)
    other_guest_ids=fields.One2many('other.guests','accommodation_id',string='Guests',tracking=True,ondelete='cascade')
    food_order_id=fields.One2many('order.food','accommodation_id',string='food order',ondelete='cascade')
    food_payment_many_ids=fields.Many2many(comodel_name='order.list')
    expense_ids=fields.One2many('order.expense','accommodation_id',ondelete='cascade')
    rent_room=fields.Float(string='Rent')
    full_total=fields.Float(string='Total',compute='_compute_total')
    order_food_count=fields.Integer(string='order count',tracking=True,compute="compute_food_order_count")
    # invoice_id=fields.Many2one(comodel_name='account.move',string='invoice_id')
    invoice_id=fields.One2many(comodel_name='account.move',inverse_name='accommodation_id',string='invoice_id',)
    user_id=fields.Many2one('res.users',string='user',default=lambda self: self.env.user.id)
    company_id = fields.Many2one('res.company', string='user', default=lambda self: self.env.company.id)
    archive=fields.Boolean(string='archive' ,default=True)
    invoice_count=fields.Integer(string='Invoice Count',tracking=True,compute="compute_invoice_count")




    @api.depends('invoice_id')
    def compute_invoice_count(self):
        """invoice count for smart button"""
        for record in self:
            record.invoice_count=len(record.invoice_id)


    def get_invoice_record(self):
        """invoice record """
        self.ensure_one()
        return{
            'type': 'ir.actions.act_window',
            'name': 'invoice',
            'view_mode': 'form,list',
            'res_model': 'account.move',
            'res_id':self.invoice_id.id,
        }

    @api.depends('food_order_id','state')
    def compute_food_order_count(self):
        """order food records count"""
        for record in self:
            if record.state != 'draft':
                order_count = len(record.expense_ids)
                record.order_food_count =order_count - 1
            else:
                record.order_food_count =0
    def get_food_order_smart_record(self):
        """order food records"""
        self.ensure_one()
        food_orders=[]
        for order in self.food_order_id:
          food_orders.append(order.id)

        return{
            'type': 'ir.actions.act_window',
            'name': 'food order',
            'view_mode': 'list,form',
            'res_model': 'order.food',
            'domain':[('id','in',food_orders)],
            # 'res_id':m,
            'target':'current'

        }


    def order_food_now(self):
        """creating order food from accommodation record"""
        return{
            'type': 'ir.actions.act_window',
            'name': 'food order now',
            'view_mode': 'form,list',
            'res_model': 'order.food',
            'context':{'default_accommodation_id':self.id,'default_accommodation_guest':self.guest_id.name,'default_accommodation_room':self.room_id.id}
        }



    @api.depends('expense_ids')
    def _compute_total(self):
      """calculate total from expense_ids"""

      for record in self:
          rent_total=0
          for expence in record.expense_ids:
              if expence:
                  rent_total+=expence.subtotal

              else:
                  record.full_total = None
          record.full_total = rent_total



    @api.depends('bed_type','facilities_ids')
    def _compute_bed_type_base_rooms_id(self):
        """ user can select rooms based on bed type """
        for record in self:
            if record.bed_type:
                if record.facilities_ids:
                    all_rooms = self.env['hotel.rooms'].search([('bed', '=', record.bed_type), ('state', '=', 'available'),('facility_id', '=', record.facilities_ids)])
                    print('all_rooms', all_rooms)
                    record.bed_type_base_rooms_ids =all_rooms
                else:
                  all_rooms = self.env['hotel.rooms'].search([('bed', '=', record.bed_type), ('state', '=', 'available')])
                  record.bed_type_base_rooms_ids = all_rooms
            else:
                record.bed_type_base_rooms_ids=self.env['hotel.rooms'].search([('state','=','available')])




    def check_in_check(self):
       """check in function"""
       for record in self:
           file=self.env['ir.attachment'].search([('res_model','=','hotel.accommodation'),('res_id','=',self.id)])
           if len(file)==0 :
               raise ValidationError('Include Identification Proof')

           elif  record.guest_no !=len(record.other_guest_ids):
            raise ValidationError('Please provide all guest details')
           else:
                record.state = 'check-in'
                current_date = fields.Datetime.now()
                record.check_in = current_date
                record.expected_date = record.check_in + timedelta(days=+ record.expected_days)
                print('expected', record.expected_date)
                record.room_id.state = 'not available'



                products = self.env['product.template'].search([('name', '=', 'Rent')])
                print('products', products.name)
                print('products.list_price', products.list_price)
                vals = {
                    'accommodation_id': self.id,
                    'products': products.id,
                    'quantity': self.expected_days,
                    'unit_price': self.expected_days*self.room_id.rent,
                    'subtotal':self.expected_days*self.room_id.rent,

                }

                self.env['order.expense'].create(vals)

                return {
                    'name': ' product',
                    'view_mode': 'form',
                    'view_type': 'form',
                    'res_model': 'hotel.accommodation',
                    'type': 'ir.actions.act_window',
                    'res_id': self.id,
                    'target': 'current',
                }

    def check_out_check(self):
            """check out function"""
            if self.state=='check-in':
                self.state='check-out'
                self.room_id.state='available'
                current = fields.Datetime.now()
                self.check_out = current
                days=self.check_out.day -self.check_in.day
                if days==0:
                    pass
                else:
                    product_rent=self.env['order.expense'].search([('products','=','Rent')])
                    print('product_rent', product_rent)
                    if product_rent:
                        product_rent.write({
                            'quantity':days,
                            'unit_price':self.room_id.rent,
                            'subtotal':days*self.room_id.rent
                        })
                    else:
                        print('not fount')

                invoice_vals={
                    'move_type':'out_invoice',
                    'accommodation_id':self.id,
                    'partner_id':self.guest_id.id,
                    'invoice_date':fields.Date.context_today(self),
                    'line_ids':[Command.create({
                        'name':i.products.name,
                        'quantity':i.quantity,
                        'price_unit':i.unit_price,
                    }) for i in self.expense_ids]

                }
                print('invoice_vals',invoice_vals )
                invoices=self.env['account.move'].create(invoice_vals)
                for i in invoices:
                    print('values',i.line_ids)
                print('invoices',invoices.read())
                print('invoices', invoices.payment_state)
                self.invoice_id=invoices
                print('invoise id',self.invoice_id)
                print('accommodation',self.id)



                return{
                    'name': ' Customer Invoice',
                    'view_mode': 'form,list',
                    'view_type': 'form',
                    'res_model': 'account.move',
                    'type': 'ir.actions.act_window',
                    'res_id': invoices.id,
                    'target': 'current',
                }


    def accommodation_cancel(self):
        """cancel accommodation"""
        if self.state=='check-in':
            self.state='cancel'
            self.room_id.state='available'
            # mm=fields.Datetime.now().day-self.cancel_date.day
            self.cancel_date =fields.Datetime.now()
            print('cancel date',self.cancel_date)
            results=self.search([('state','=','cancel')])
            print('results', results)
            if results:
                    results.write({'active':False})

    def archive_automation(self):
        """archive automation archive  more than 2 days canceled records"""
        all_records=self.env['hotel.accommodation'].search([('state','in','cancel'),('active','=',False),('archive','=',True)])
        for record in all_records:
              print(record.reference_number)
              if record.cancel_date:
               date = fields.Datetime.now().day - record.cancel_date.day

               if 2<=date:
                record.write({
                    'archive':False
                })
                print('archive', record.archive)



    #mail send  function
    def action_send_mail(self):
        """send mail to guest"""
        template = self.env.ref('hotel_management.email_template_for_check_out')
        expected_checkout_today_records=self.search([('expected_date','=',fields.Date.today()),('state','=','check-in')])

        email_values = {'email_from': self.env.user.email}
        for record in  expected_checkout_today_records:
           template.send_mail(record.id, force_send=True, email_values=email_values)

    #sequence series......
    @api.model_create_multi
    def create(self, vals):
        """create sequence"""
        for sequence in vals:
            sequence['reference_number']=self.env['ir.sequence'].next_by_code('hotel.accommodation_code')

        res=super().create(vals)
        return res
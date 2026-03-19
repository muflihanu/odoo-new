

from odoo.exceptions import AccessError
from odoo import fields,models,api
from odoo import Command



class Travel_Agency_Booking(models.Model):
    _name='travel.agency_booking'
    _description='Travel_Agency'

    # name=fields.Char(string='Name')
    # t_booking_id=fields.Char(string='Booking id',required=True)
    t_booking_id=fields.Integer(string='Booking id', compute="_compute_booking_id")
    name=fields.Many2one('res.partner',string='Name')
    cust_address=fields.Char(string='Address')
    phone=fields.Char(string='Phone')
    email=fields.Char(string='Email')
    date=fields.Date(string='Date')
    members = fields.Integer(string='Members',default=2)
    package_name=fields.Many2one('travel.package',string='Package')
    days=fields.Integer(string=' Days',default=5)
    transportation_mode = fields.Selection(selection=[('bus', 'BUS'), ('train', 'Train'), ('flight', 'Flight')],
                                           default='bus', string='Transportation')
    total_amount=fields.Float(string='Total Amount',compute='_compute_total_amount')
    booking_team=fields.Many2one('booking.team',string='Booking Management Team')
    state=fields.Selection(selection=[('draft','Draft'),('confirmed','Confirmed'),('reschedule','Reschedule')],default='draft')
    reschedule_id=fields.Many2one('reschedule.booking', string='Reschedule Booking')
    sale_order=fields.Many2one('sale.order',string='Sale Order')


    @api.depends('t_booking_id')
    def _compute_booking_id(self):
        for i in self:

            i.t_booking_id+=i.id



    def reshedule_booking(self):
      self.ensure_one()
      variable={
          'b_id':self.t_booking_id,
          'ree_customer':self.name.id,
           're_date':self.date,
          'reshedule_package':self.package_name.id

      }
      ree=self.env['reschedule.booking'].create(variable)

      return{
          'name':'rescheduling',
          'view_mode':'form,list',
          'view_type':'list',
          'res_model':'reschedule.booking',
          'type':'ir.actions.act_window',
          'res_id':ree.id,

    }


    @api.depends('package_name.Amount')
    def _compute_total_amount(self):
        for i in self:
            i.total_amount=i.package_name.Amount

    def action_confirmed(self):
           self.state='confirmed'
           if self.sale_order:
               print('customer=',self.sale_order.partner_id.name)
               print('customer country=',self.sale_order.partner_id.country_id.name)
               print('customer currency=', self.sale_order.partner_id.currency_id.name)
               all=self.env['sale.order'].search([('partner_id','=',self.sale_order.partner_id.id)])
               print('customer total  sales count=',len(all))
               total_amount=0
                   # print(i.order_line)
               product_count={}
               for i in all:
                   total_amount += i.amount_total
                   for j in i.order_line:
                       product=j.product_template_id.name
                       qty=j.product_uom_qty
                       price=j.price_unit
                       if product in product_count:
                           product_count[product]+=qty
                       else:
                           product_count[product]=qty

               print('customer sales orders total amount=', total_amount)
               print('product=',product_count)
               purchase_count=0
               pro=''
               highest_purchased_pro={}
               for p,q in product_count.items():
                   if q>purchase_count:
                       purchase_count=q
                       pro=p

               highest_purchased_pro[pro]=purchase_count
               print("highest purchased product=",highest_purchased_pro)
               least_purchased_product={}
               least_pro=float('inf')
               least_product=''
               for p,q in product_count.items():
                   if q<least_pro:
                       least_pro=q
                       least_product=p

               least_purchased_product[least_product]=least_pro
               print('least purchased product=',least_purchased_product)
               total_margin = 0
               for i in all:

                       for j in i.order_line:
                           total_margin+=j.margin

                           if j.product_template_id.name==least_product:
                              print('----------------------------')
                              print('least product vendor and price:')
                              print(j.product_template_id.name)
                              print(j.price_unit)
                              print('vendor=',i.company_id.name)
               print('total margin=',total_margin)







    def action_reschedule(self):
        self.state='reschedule'



    def action_view_invoice(self):
        self.ensure_one()
        invoice_vals={
            'move_type': 'out_invoice',
            'partner_id': self.name.id,
            'line_ids':[Command.create({
               'name':self.package_name.package_name,
                'price_unit':self.total_amount,
            })]


        }

        invoice=self.env['account.move'].create(invoice_vals)

        return {
            'name': ' Customer Invoice',
            'view_mode': 'form,list',
            'view_type': 'form',
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'res_id':invoice.id,
            'target': 'current',
        }





class Travel_Package(models.Model):
    _name='travel.package'
    _description = 'package'
    _rec_name = 'package_name'

    package_name=fields.Char(string='Package Name')
    de_from=fields.Char(string='From')
    destination=fields.Selection(selection=[('manali','Manali'),('kashmir','Kashmir'),('rajasthan','Rajasthan'),('goa','Goa')],string='Destination')
    p_hotel=fields.Many2one('travel.hotel',string='Hotel')
    Amount=fields.Float(string='Total Amount')
    t_food=fields.Selection(selection=[('veg','Veg'),('non veg','Non Veg')],default='veg',string='Food')




class Travel_Hotel(models.Model):
    _name='travel.hotel'
    _description='travel_hotel'
    _rec_name = 'hotel_name'
    hotel_name=fields.Char(string=' Hotel Name')
    room_available=fields.Integer(string='Room Available')


class Cust_booking(models.Model):
    _name='cust.booking'
    _description='cust booking'


    @api.depends('cust_members')
    def _compute_cust_total_amount(self):
        for i in self:
            i.t_amount=i.cust_members*2000

    cust_name=fields.Many2one('res.users',string='Customer')
    c_address=fields.Char(string='Customer Address')
    cust_phone=fields.Char(string='Customer Phone')
    cust_email=fields.Char(string='Customer Email')
    cust_date=fields.Date(string='Date')
    cust_members=fields.Integer(string='Members')
    d_from=fields.Char(string='From',default='kerala')
    cust_des = fields.Selection(
        selection=[('manali', 'Manali'), ('kashmir', 'Kashmir'), ('rajasthan', 'Rajasthan'), ('goa', 'Goa')],
        string='Destination')
    h_days=fields.Integer(string='Days',default=5)
    cust_hotel = fields.Many2one('travel.hotel', string='Hotel')
    cust_food = fields.Selection(selection=[('veg', 'Veg'), ('non veg', 'Non Veg')], default='veg', string='Food')
    cust_transportation_mode = fields.Selection(selection=[('bus', 'BUS'), ('train', 'Train'), ('flight', 'Flight')],
                                           default='bus', string='Transportation')

    t_amount=fields.Float(string='Total Amount',compute='_compute_cust_total_amount')
    cust_booking_team = fields.Many2one('booking.team', string='Booking Management Team')


class Booking_managment_team(models.Model):
    _name='booking.team'
    _description = 'booking_management_team'
    _rec_name = 'team_name'

    team_name=fields.Char(string='Booking Management Team Name')
    employee=fields.Many2many('res.users',string='Employee')
    booked_cards_id=fields.One2many('travel.agency_booking','booking_team')




class Reschedule_booking(models.Model):
    _name='reschedule.booking'
    _description = 'reschedule_booking'

    ree_customer=fields.Many2one('res.partner',string='Customer')
    # re_customer=fields.One2many('travel.agency_booking','name',string='Customer')
    b_id=fields.Char(string='Booking ID')
    # ree_customer=fields.Char(string='Customer')
    reshedule_package=fields.Many2one('travel.package',string='Reschedule Package')
    re_date=fields.Date(string='Re-Date')
    book_id=fields.One2many('travel.agency_booking','reschedule_id')
    stage=fields.Selection(selection=[('new','New'),('confirm','Confirm')],string='Stage', default='new')


    def delete_record_another_rc(self):
          for r in self:
              r.stage='confirm'
              record = self.env['travel.agency_booking'].browse(r.id)
              record.unlink()
              # print('tesst',record)






from email.policy import default

from odoo import fields,models,api
from odoo.exceptions import UserError,ValidationError
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta

from odoo.orm.decorators import readonly


def get_date():
    today=date.today()
    date_after_3_month=today+relativedelta(months=+3)
    return  date_after_3_month



class Estate_Prorerty(models.Model):
    _name='estate.property'
    _description='real estate property description'
    _order='id desc'


    name=fields.Char('Property Name',required=True,translate=True)
    property__type=fields.Many2one('property.type',string='Property Type',required=True)
    tag=fields.Many2many('property.tags',string='Property Tags')
    property_description=fields.Text('Property Description',translate=True)
    postcode=fields.Char('Postcode')
    date_availability=fields.Date('Date Availability',copy=False,default=get_date())
    expected_price=fields.Float('Expected Price',required=True)
    selling_price=fields.Float('Selling Price',readonly=True )
    bedrooms=fields.Integer('Bedrooms',default=2)
    living_area=fields.Integer('Living area',required=True)
    facades=fields.Integer('Facades')
    garage=fields.Boolean('Garage')
    garden=fields.Boolean('Garden' )
    garden_area=fields.Integer('Garden Area',)
    garden_oreantation=fields.Selection(string='Type',selection=[('north','North'),('south','South'),('east','East'),('west','West')])
    active = fields.Boolean('Active', default=False)
    state=fields.Selection(string='State',selection=[('new','New'),('offer received','Offer Received'),('Offer accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')],default='new',copy=False,required=True)
    buyer=fields.Many2one('res.partner',string='Buyer',required=True,copy=False)
    seller=fields.Many2one('res.users',string='Seller',required=True,default=lambda self: self.env.user)
    offer=fields.One2many('property.offer','property_id',string='Offer',required=True)
    total_area=fields.Float('Total Area',required=True,compute='total_p')
    best_price=fields.Float('Best Price',required=True,compute='best_offer',default=0)
    # type_pro_ids=fields.Many2one('property.type',string='Property Type')



    _check_expected_price =models.Constraint('CHECK(expected_price>0)', 'A expected price must be positive')
    _check_selling_price = models.Constraint('CHECK(selling_price>0)', 'A selling price must be positive')





    @api.depends('living_area', 'garden_area')
    def total_p(self):
        for i in self:
            i.total_area = i.living_area + i.garden_area

    @api.depends('offer')
    def best_offer(self):
        for i in self:
            p = i.offer.mapped('offer_price')
            if p:
                i.best_price = max(p)
            else:
                i.best_price = 0



    # actions
    def sold_property(self):
        for i in self:
            if i.state=='cancelled':
               raise UserError('Property is canceled!!')
            else:
                i.state='sold'

        return True



    def cancel_property(self):
       for i in self:

           if i.state=='sold':
               raise UserError('Property is sold!!')
           else:
               i.state='cancelled'
       return True





    #onchange function working
    @api.onchange('garden')
    def onchange_garden(self):
          if self.garden:
              self.garden_area=10
              self.garden_oreantation='north'
          else:
              self.garden_area=0
              self.garden_oreantation=''


    # @api.constrains('expected_price')
    # def _checking_the_prices(self):
    #    for i in self:
    #     new_price=i.expected_price*0.9
    #     if i.selling_price<new_price:
    #             raise ValidationError('selling price cannot be lower than 90% of the expected price.')





class Property_Type(models.Model):
    _name='property.type'
    _description='property_type description'
    _rec_name='property_type'
    _order='property_type'
    property_type=fields.Char(string='Property Type',required=True)
    property_id = fields.One2many('estate.property', 'property__type', string='Property offers', copy=False)
    sequence=fields.Integer(string='Sequence',default=1)
    offer_id=fields.One2many('property.offer','property_id', string='offers')

    offer_count=fields.Integer(string='Offer Count',compute="_compute_offer_count")


    _property_type_unique  = models.Constraint ( 'UNIQUE(property_type)', 'A property type must be unique')

    @api.depends('offer_id')
    def _compute_offer_count(self):
        for i in self:
            i.offer_count=len(i.property_id.mapped('offer_id'))





class Property_tags(models.Model):
    _name='property.tags'
    _description='property_tags description'
    # _order='tags'
    _rec_name='tags'
    tags=fields.Char(required=True)
    color=fields.Integer(string='Color',required=True)


    _tags_unique = models.Constraint('UNIQUE(tags)', 'A property tag must be unique')



class Property_offer(models.Model):
    _name='property.offer'
    _description = 'property offer description'
    _order='offer_price'

    offer_price=fields.Float('Price',default=0)
    status=fields.Selection(selection=[('accepted','Accepted'),('refused','Refused')],string='Status',copy=False)
    partner_id=fields.Many2one('res.partner',required=True)
    property_id=fields.Many2one('estate.property',required=True)

    validity=fields.Integer(string='Validity',default=7)
    date_deadline=fields.Date('Date Deadline',compute='compute_deadline_offer',inverse='inverse_deadline_offer')
    # type_pro_ids = fields.Many2one('property.type')
    # type_id=fields.Many2one('property.type',stored='true')


    _check_offer_price = models.Constraint('CHECK(offer_price>0)', 'A offer price must be Positive')



    def accept_confirm(self):
        for i in self:
            if i.status=='accepted'  and  i.property_id.selling_price:
                raise UserError('already one offer  is accepted!!')
            else:
                i.status = 'accepted'
                i.property_id.buyer = i.partner_id
                i.property_id.selling_price = i.offer_price

                new_price = i.property_id.expected_price * 0.9
                if i.property_id.selling_price < new_price:
                    raise ValidationError('selling price cannot be lower than 90% of the expected price.')

    def accept_reject(self):
        for i in self:
            if  i.status == 'accepted':
                i.status = 'refused'
                i.property_id.selling_price=0
            else:
                i.status = 'refused'
    @api.depends('validity')
    def compute_deadline_offer(self):
        tod = date.today()
        for i in self:
            i.date_deadline = tod + timedelta(days=+i.validity)

    def inverse_deadline_offer(self):
        # new_dt=[]
        for i in self:

            tod = date.today()
            i.validity=i.date_deadline.day-tod.day
            print('testing=======testing', i.validity)





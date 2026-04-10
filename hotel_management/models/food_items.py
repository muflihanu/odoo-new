from email.policy import default

from odoo import fields,models,api


class FoodItems(models.Model):
    _name='food.items'
    _description='food items'
    _rec_name = 'food_name'

    # image=fields.Binary(string='Image')
    image=fields.Image(string='Image')
    food_name=fields.Char(string='Food Name')
    item=fields.Char(string='Item')
    category_id=fields.Many2one('food.category',string='Category')
    food_price=fields.Float(string='Unit Price')
    food_quantity=fields.Integer(string='Quantity')
    food_description=fields.Text(string='Description')
    food_order_id=fields.Many2one('order.food',string='Order List')
    sub_total=fields.Float(string='Sub Total',compute='_compute_subtotal')
    # order_line_ids=fields.One2many('order.line','order_id',string='Order Lines')
    state=fields.Selection([('draft','Draft'),('confirmed','Confirmed')],default='draft',string='State')
    supplier_id = fields.Many2one('lunch.supplier', 'Vendor', required=True,default= lambda self: self.env['lunch.supplier'].search([('name', '=', 'Hungry Dog')], limit=1))
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id)
    company_id = fields.Many2one('res.company', string='user', default=lambda self: self.env.company.id)



    @api.depends('food_price','food_quantity')
    def _compute_subtotal(self):
        for record in self:
            record.sub_total = record.food_price * record.food_quantity

    # def confim_food_items(self):
    #     if self.state=='draft':
    #         self.state='confirmed'

    def add_to_list(self):
        # self.ensure_one()
        variable={

        'order_name':self.food_name,
            'order_description':self.food_description,
            'quantity':self.food_quantity,
            'unit_price':self.food_price,
            'subtotal':self.sub_total,
            'order_food_id':self.env.context.get('default_order'),

        }
        self.env['order.list'].create(variable)

        print('dddd',self.env.context.get('default_order'))



        return {
            'name': 'order list',
            'view_mode':'form',
            # 'view_type': 'list',
            'res_model': 'order.food',
            'type': 'ir.actions.act_window',
            'res_id':self.env.context.get('default_order'),
        }

        # automation action function

    def create_product_to_lunch(self):
        self.ensure_one()
        lunch_category=self.env['lunch.product.category'].search([('name','=','Pizza')])
        print(lunch_category)
        vals = {
            'name': self.food_name,
            'category_id':lunch_category.id,
            'price':self.food_price,
            'supplier_id': self.supplier_id.id,

        }

        lunch_pro= self.env['lunch.product'].create(vals)
        print(lunch_pro,'lunch product')
        return {
            'name': 'order list',
            'view_mode': 'form',
            'view_type': 'list',
            'res_model': 'lunch.product',
            'type': 'ir.actions.act_window',
            'res_id': lunch_pro.id,

        }

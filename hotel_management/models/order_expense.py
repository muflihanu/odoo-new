from odoo import api,fields,models,exceptions
from odoo.tools.which import defpath


class OrderExpense(models.Model):
    _name = 'order.expense'
    _description = 'Order Expense'


    # food_order_ids = fields.One2many('order.food', 'food_expense_id', string='food payment')
    accommodation_id=fields.Many2one('hotel.accommodation',string='accommodation',ondelete='cascade')
    products=fields.Many2one('product.template',string='Product')
    quantity=fields.Integer(string='Quantity' ,default=1)
    unit_price=fields.Float(string='Unit Price')
    subtotal=fields.Float(string='Subtotal')


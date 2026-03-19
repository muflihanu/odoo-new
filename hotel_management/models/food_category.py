from odoo import fields,models,api

class FoodCategory(models.Model):
    _name='food.category'
    _description='food category'
    _rec_name = 'food_category_name'

    food_category_name=fields.Char(string='Food Category')

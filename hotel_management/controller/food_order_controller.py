from odoo import http
from odoo.http import request

class FoodOrderController(http.Controller):
    @http.route('/food_orders',type='http',auth="public",website=True)
    def food_order_form(self):

        return request.render('hotel_management.food_order_form_template')

    @http.route('/food_items', type='jsonrpc', auth="public", website=True)
    def food_order(self, category_values):
        category_ids =[]
        for cat in category_values:
            category_ids.append(int(cat))
        food_vals = []
        foods = self.env['food.items'].search([('category_id', 'in', category_ids)])
        print(category_ids)
        print(foods)
        for food in foods:
            food_vals.append({'food_id':food.id,'food_name': food.food_name, 'img':food.image,'food_qty':food.food_quantity})
        return  {'food_vals': food_vals}
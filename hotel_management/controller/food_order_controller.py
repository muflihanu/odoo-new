from odoo import http
from odoo.http import request
from odoo import Command

class FoodOrderController(http.Controller):
    @http.route('/food_orders',type='http',auth="public",website=True)
    def food_order_form(self):

        return request.render('hotel_management.food_order_form_template')

    @http.route('/food_items', type='jsonrpc', auth="public", website=True)
    def food_order(self, category_values):
        print(category_values)
        category_ids =[]
        for cat in category_values:
            category_ids=[]
            print(cat)
            print('categorylist',category_ids)
            category_ids.append(int(cat))
        food_vals = []
        foods = self.env['food.items'].sudo().search([('category_id', 'in', category_ids)])
        print(category_ids)
        print(foods)
        for food in foods:
            food_vals.append({'food_id':food.id,'food_name': food.food_name, 'img':food.image,'food_qty':food.food_quantity,'food_price':food.food_price})
        return  {'food_vals': food_vals}

    @http.route('/create_order', type='jsonrpc', auth="public", website=True)
    def create_food_order(self,accommodation_id,food_names,food_qty,food_price):
        vals=[]
        line_vals=[]
        print(food_names)
        print(food_qty)
        print(food_price)

        # res=dict(zip(food_names,food_qty))
        for f,q in zip(food_names,food_qty):
            vals.append({'food_name':f,'food_qty':q})

        for v,p in zip(vals,food_price):
            line_vals.append((0,0,{
                'order_name':v['food_name'],
                'quantity':v['food_qty'],
                'unit_price':p,
                'subtotal':int(p)*v['food_qty'],
            }))
        print(accommodation_id)
        print(vals)

        print(123123,  )

        created=self.env['order.food'].sudo().create({ 'accommodation_id':accommodation_id,
                                                       'order_list_ids':line_vals})
        print(created)


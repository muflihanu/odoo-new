from odoo import api,fields,models
from odoo import Command

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def add_sale_product(self):


        order = self.env["sale.order"].browse(self.env.context.get('sale_order_id'))
        print(order)
        product = self.env["product.product"].search([])
        sale_product = self.env['sale.product.wizard'].create({
            'sale_order_id': order.id,
            'product_line_ids': [Command.create({
                'product_id': pr.id,
                'product_qty': 0,
                'select_check': False,
            }) for pr in product]})
        return {
            'type': 'ir.actions.act_window',
            'name': 'product',
            'view_mode': 'form',
            'res_model': 'sale.product.wizard',
            'res_id': sale_product.id,
            'target': 'new'
        }
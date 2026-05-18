from odoo import api, fields, models, tools

class ProductWizard(models.TransientModel):
    _name = "sale.product.wizard"
    _description = "Product Wizard"

    sale_order_id = fields.Many2one('sale.order')
    product_line_ids=fields.One2many('sale.product.wizard.line','sale_product_wizard_id')

    def add_selected_products(self):
        if self.product_line_ids:
            for line in self.product_line_ids:
                if line.select_check == True:
                    order = self.env['sale.order.line'].create(
                        {'order_id': self.sale_order_id.id, 'product_id': line.product_id.id,
                         'product_uom_qty': line.product_qty})

        return {
            'type': 'ir.actions.act_window',
            'name': 'sale_order',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'res_id': self.sale_order_id.id,
        }
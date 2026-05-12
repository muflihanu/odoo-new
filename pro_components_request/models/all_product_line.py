from odoo import api, fields, models, tools

class AllProductLine(models.Model):
    _name = "all.product.line"
    _description = "All Product Line"

    # pro_request_id = fields.Many2one('product.requests', string='Request',)
    employee_request_id=fields.Many2one('employee.request',string="Request")
    product_id = fields.Many2one('product.template',string="Product")
    quantity = fields.Float(string="Quantity")
    pro_type=fields.Selection(selection=[('purchase order','Purchase Order'),('internal transfer','Internal Transfer')],string="Type")
    vendor = fields.Many2one('res.partner', string="Vendor",compute="_compute_product_vendors")

    @api.depends('pro_type')
    def _compute_product_vendors(self):
        for product in self:
         if product.pro_type == 'purchase order':
                    print(product.product_id.seller_ids.partner_id.name)
                    product.vendor=product.product_id.seller_ids.partner_id.id
         else:
            product.vendor=None





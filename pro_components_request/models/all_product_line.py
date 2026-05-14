# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools

class AllProductLine(models.Model):
    _name = "all.product.line"
    _description = "All Product Line"

    # pro_request_id = fields.Many2one('product.requests', string='Request',)
    employee_request_id=fields.Many2one('employee.request',string="Request")
    product_id = fields.Many2one('product.product',string="Product")
    quantity = fields.Float(string="Quantity")
    product_uom_ids = fields.Many2many('uom.uom', string="Unit of Measure", compute="compute_package_uom")
    unit_of_measure = fields.Many2one('uom.uom',string="UOM",readonly=False)
    pro_type=fields.Selection(selection=[('purchase order','Purchase Order'),('internal transfer','Internal Transfer')],string="Type")
    vendor = fields.Many2one('res.partner', string="Vendor",compute="_compute_product_vendors",inverse="inverse_partner")
    source_location_id=fields.Many2one('stock.location',string="Source Location")
    destination_location_id=fields.Many2one('stock.location',string="Destination Location")
    product_unit_price=fields.Float(string="Unit Price",related="product_id.lst_price",readonly=False)
    state=fields.Selection(selection=[('draft','draft'),('confirm','Confirm')],default='draft',string="State")
    # operation_type_id=fields.Many2one('stock.picking.type',string="Operation Type")



    @api.depends('pro_type')
    def _compute_product_vendors(self):
        """ compute product vendor """
        for product in self:
         if product.pro_type == 'purchase order':
                   if len(product.product_id.seller_ids.partner_id)>1:
                    partner=product.product_id.seller_ids.mapped('partner_id.id')
                    product.vendor=partner[0]
                   else:
                      product.vendor=product.product_id.seller_ids.partner_id.id
         else:
            product.vendor=None

    def inverse_partner(self):
        """partner inverse"""
        for product in self:
            if product.pro_type == 'purchase order':
                product.vendor=None

    @api.depends('product_id')
    def compute_package_uom(self):
        """ compute package uom """
        for product in self:
         if product.product_id.uom_ids:
           vals=product.product_id.mapped('uom_ids')
           product.product_uom_ids = vals.ids
           print(vals)
           print(product.product_uom_ids)
         else:
            product.product_uom_ids = []




    @api.onchange('product_id')
    def _onchange_product_unit_of_measure(self):
        """onchange product uom """
        if self.product_id:
            self.unit_of_measure=self.product_id.uom_id













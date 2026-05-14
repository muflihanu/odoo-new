# -*- coding: utf-8 -*-
from odoo import Command

from odoo import fields, models,api

class EmployeeRequest(models.Model):
    _name = "employee.request"
    _description = "Employee Request"
    _rec_name = "request_sequence"

    request_sequence=fields.Char(string="Sequence",copy=False,readonly=True,default='New')
    employee_id = fields.Many2one('res.users',string="name",default=lambda self: self.env.user.id)
    all_product_line_ids=fields.One2many('all.product.line','employee_request_id',string="All Product Lines")
    state=fields.Selection([('draft','Draft'),('confirm','Confirm'),('first approve','First Approve'),('po created','PO Created')],default='draft',string="State")
    # vendors=fields.Many2many('product.supplierinfo',string="Vendors")
    # vendor=fields.Many2one('product.supplierinfo',string="Vendor")
    reason=fields.Text(string="Reason",required=True)
    reason_bool=fields.Boolean(string="Reason",default=False)
    # purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order")
    purchase_order_id = fields.One2many('purchase.order','employee_request_id', string="Purchase Order")
    # internal_transfer_id=fields.Many2one('stock.picking',string="Internal Transfer")
    internal_transfer_ids = fields.One2many('stock.picking','stock_employee_request_id', string="Internal Transfer")
    # internal_bool=fields.Boolean(string="Internal Transfer",default=False)
    # purchase_bool=fields.Boolean(string="Purchase",default=False)
    po_count=fields.Integer(string="PO Count",default=0,compute="get_po_count")
    internal_record_count=fields.Integer(string="Internal Record Count",compute="get_internal_count")



    def send_request(self):
        """sending the request and changing the state"""
        if self.state == 'draft':
            self.state = 'confirm'
            self.all_product_line_ids.state='confirm'
        if self.reason_bool == True:
            self.reason_bool=False

    def first_approve(self):
        """first approval,HR approvel"""
        if self.state == 'confirm':
            self.state = 'first approve'


    def second_approve(self):
            """second approval,Manager approval and creating records """
            if self.all_product_line_ids:
                values = []
                internal_vals = []
                for line in self.all_product_line_ids:
                    if line.pro_type == 'purchase order' and line.vendor:
                        existing_po_order=self.env['purchase.order'].search([('partner_id','=',line.vendor.id),('state','=','draft')])
                        if existing_po_order:
                            val=existing_po_order[0]
                            val.write({'order_line':[Command.create({
                                'product_id': line.product_id.id,
                                'product_qty': line.quantity,
                                'product_uom_id':line.unit_of_measure.id,
                                'price_unit':line.product_unit_price,

                            })]})

                            values.append(val.id)



                        else:
                          order=self.env['purchase.order'].create({
                            'partner_id': line.vendor.id,
                            'order_line': [Command.create({
                                'product_id': line.product_id.id,
                                'product_qty': line.quantity,
                                'product_uom_id': line.unit_of_measure.id,
                                'price_unit': line.product_unit_price,
                            })]
                        })
                          values.append(order.id)
                    self.purchase_order_id = values
                    if line.pro_type == 'internal transfer':

                        code=self.env['stock.picking.type'].search([('code','=','internal')])
                        internal_order=self.env['stock.picking'].create({
                            'picking_type_id':code.id,
                            'move_ids': [Command.create({
                                'product_id': line.product_id.id,
                                'product_uom_qty': line.quantity/line.product_id.uom_id.relative_factor,
                            })]
                        })
                        internal_vals.append(internal_order.id)
                    self.internal_transfer_ids =internal_vals



            self.state = 'po created'


    def reject_request(self):
        """MR rejection"""
        self.state = 'draft'
        if self.reason_bool == False:
            self.reason_bool = True

    @api.depends('purchase_order_id','state')
    def get_po_count(self):
        """purchase order count  compute """
        for record in self:
          if record.state=='po created':
            record.po_count=len(record.purchase_order_id)
          else:
            record.po_count=0

    @api.depends('internal_transfer_ids', 'state')
    def get_internal_count(self):
        """internal transfer count  compute """
        for record in self:
            if record.state == 'po created':
                record.internal_record_count = len(record.internal_transfer_ids)
            else:
                record.internal_record_count = 0

    def get_po_record_smart_button(self):
        """  po  smart button  """
        orders=[]
        self.ensure_one()
        for rec in self.purchase_order_id:
            orders.append(rec.id)

        return {
            'type': 'ir.actions.act_window',
            'name': 'PO',
            'view_mode': 'list,form',
            'res_model': 'purchase.order',
            'domain': [('id', 'in', orders)],
        }

    def get_internal_transfer_record_smart_button(self):
        """ internal transfer smart button  """
        int_orders = []
        self.ensure_one()
        for rec in self.internal_transfer_ids:
            int_orders.append(rec.id)
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'SP',
            'view_mode': 'list,form',
            'res_model': 'stock.picking',
            'domain': [('id', 'in', int_orders)],
        }



    @api.model_create_multi
    def create(self, vals):
        """create sequence"""
        for sequence in vals:
            sequence['request_sequence'] = self.env['ir.sequence'].next_by_code('employee.request_code')

        res = super().create(vals)
        return res
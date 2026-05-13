from fileinput import lineno
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
    purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order")
    internal_transfer_id=fields.Many2one('stock.picking',string="Internal Transfer")



    def send_request(self):
        if self.state == 'draft':
            self.state = 'confirm'
            self.all_product_line_ids.write({'state':'confirm'})
        if self.reason_bool == True:
            self.reason_bool=False

    def first_approve(self):
        if self.state == 'confirm':
            self.state = 'first approve'


    def second_approve(self):
            if self.all_product_line_ids:
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
                            self.purchase_order_id=val.id
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
                          self.purchase_order_id = order.id
                    if line.pro_type == 'internal transfer':
                        code=self.env['stock.picking.type'].search([('code','=','internal')])
                        internal_order=self.env['stock.picking'].create({
                            'picking_type_id':code.id,
                            'move_ids': [Command.create({
                                'product_id': line.product_id.id,
                                'product_uom_qty': line.quantity*line.unit_of_measure.relative_factor,
                            })]
                        })
                        self.internal_transfer_id=internal_order.id


            self.state = 'po created'


    def reject_request(self):
        self.state = 'draft'
        if self.reason_bool == False:
            self.reason_bool = True

    def get_po_record_smart_button(self):
        """ record """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'PO',
            'view_mode': 'form,list',
            'res_model': 'purchase.order',
            'res_id': self.purchase_order_id.id,
        }

    def get_internal_transfer_record_smart_button(self):
        """ record """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'PO',
            'view_mode': 'form,list',
            'res_model': 'stock.picking',
            'res_id': self.internal_transfer_id.id,
        }



    @api.model_create_multi
    def create(self, vals):
        """create sequence"""
        for sequence in vals:
            sequence['request_sequence'] = self.env['ir.sequence'].next_by_code('employee.request_code')

        res = super().create(vals)
        return res
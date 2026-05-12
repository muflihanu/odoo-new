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
    state=fields.Selection([('draft','Draft'),('confirm','Confirm'),('first approve','First Approve'),('second approve','Second Approve')],default='draft',string="State")
    # vendors=fields.Many2many('product.supplierinfo',string="Vendors")
    # vendor=fields.Many2one('product.supplierinfo',string="Vendor")



    def send_request(self):
        if self.state == 'draft':
            self.state = 'confirm'

    def first_approve(self):
        if self.state == 'confirm':
            self.state = 'first approve'


    def second_approve(self):
        if self.state == 'first approve':
            self.state = 'second approve'

    def create_purchase_order(self):
        values=[]
        vendor=[]

        if self.all_product_line_ids:
            for line in self.all_product_line_ids:
                if line.pro_type=='purchase order' and line.vendor:
                    values.append({'product':line.product_id.id,'quantity':line.quantity})
                    vendor.append(line.vendor.id)
        self.env['purchase.order'].create({
            'partner_id':vendor,
            'order_line':Command.create[({
                'product_id':rec.product,
                'product_qty':rec.quantity,

            } for rec in values if len(values)>0) ]

        })

    @api.model_create_multi
    def create(self, vals):
        """create sequence"""
        for sequence in vals:
            sequence['request_sequence'] = self.env['ir.sequence'].next_by_code('employee.request_code')

        res = super().create(vals)
        return res
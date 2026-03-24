from odoo import api, fields, models
from odoo.exceptions import ValidationError

class EmployeeLoan(models.Model):
    _name = 'employee.loan'
    _description = 'Employee Loan'

    name=fields.Char(string='name',copy=False,readonly=True)
    employee_id=fields.Many2one('hr.employee', string='employee')
    loan_amount=fields.Float(string='Loan Amount')
    installment_count=fields.Integer(string='Installment Amount',default=1)
    start_date=fields.Date(string='Start Date')
    state=fields.Selection(selection=[('draft','Draft'),('approved','Approved'),('paid','Paid')],string='State')
    loan_line_ids=fields.One2many('employee.loan.line','loan_id',string='Loan Lines')
    installment_amount=fields.Float(string='Installment Amount')
    total_payable=fields.Float(string='Total Payable',compute='_compute_total_payable_amount')
    total_line_count=fields.Integer(string='Total Line Count',compute='_copute_counts')

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            val['name']=self.env['ir.sequence'].next_by_code('loan_employee_name')

        return super(EmployeeLoan,self).create(vals)

    @api.onchange('loan_amount','installment_count')
    def onchange_installment_amount(self):
        if self.installment_count==0:
            self.installment_amount=self.loan_amount
        elif self.loan_amount or self.installment_count!=0:
            self.installment_amount=self.loan_amount/self.installment_count





    @api.depends('loan_amount')
    def _compute_total_payable_amount(self):
        for record in self:
            if record.loan_amount:
               record.total_payable=record.loan_amount
            else:
               record.total_payable=None

    def action_approve(self):
        if self.loan_amount and self.loan_amount>0:
            self.state='approved'
        else:
            self.state='draft'


    def get_employee_loan_line(self):
        all=[]
        for record in self.loan_line_ids:
            all.append(record.id)

        return {
    'type': 'ir.actions.act_window',
    'name': 'employee loan line ',
    'view_mode': 'list,form',
    'res_model': 'employee.loan.line',
    'domain': [('id', 'in', all)],
    # 'res_id':m,
    'target': 'current'
        }

    @api.depends('loan_line_ids')
    def _copute_counts(self):
        if self.loan_line_ids:
            self.total_line_count=len(self.loan_line_ids)
        else:
            self.total_line_count=0

from odoo import fields, models, api

class EmployeeMails(models.Model):
    _name = "employee.mails"
    _description = "Employee Mails"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name= "name_id"

    name_id = fields.Many2one('hr.employee',string="Employee")
    payslip_name=fields.Char(string="Payslip Name")
    payslip_id=fields.Many2one('custom.payslip',string="Payslip ID")
    from_date=fields.Date(string="From Date")
    to_date=fields.Date(string="To Date")
    # state=fields.Selection([('draft','Draft'),('approved','Approved'),('confirm','Confirm')],default='draft',string="State")
    state = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('confirm', 'Confirm')], default='draft',  string="State")

    def approve_mail(self):
        if self.state == 'draft':
            self.state = 'approved'

    def action_send_mail(self):
        template = self.env.ref('payslips_in_my_account.employee_mails_email_template')
        payslip=self.env['custom.payslip'].search([('employee_id','=',self.name_id.id),('payslip_name','=',self.payslip_name)])

        # self.state='confirm'
        template.send_mail(self.id, force_send=True)
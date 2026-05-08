from odoo import fields, models, api

class EmployeeMails(models.Model):
    _name = "employee.mails"
    _description = "Employee Mails"
    _rec_name= "name"

    name = fields.Many2one('hr.employee',string="Employee")
    payslip_name=fields.Char(string="Payslip Name")
    payslip_id=fields.Many2one('custom.payslip',string="Payslip ID")
    from_date=fields.Date(string="From Date")
    to_date=fields.Date(string="To Date")
    state=fields.Selection([('draft','Draft'),('Approved','Approved')],default='draft',string="State")
from odoo import api, fields, models, tools
class EmployeeLoanLine(models.Model):
    _name = 'employee.loan.line'
    loan_id = fields.Many2one('employee.loan' ,string='lon id ')
    date = fields.Date(string='Date ')
    paid=fields.Boolean(string='Paid',default=False)

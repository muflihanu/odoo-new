from odoo import api, fields, models, tools

class CustomPayslip(models.Model):

    _name = 'custom.payslip'

    employee_id = fields.Many2one('hr.employee',string='Employee')
    employee_record=fields.Date(string='Employee Record')



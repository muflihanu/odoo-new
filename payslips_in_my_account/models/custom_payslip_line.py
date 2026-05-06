from odoo import fields,models

class CustomPayslipLine(models.Model):
    _name = 'custom.payslip.line'

    custom_payslip_id = fields.Many2one('custom.payslip',string='Custom Payslip')
    name = fields.Char(string='Name')
    days = fields.Float(string='Days')
    total_working_hours=fields.Float(string='Hours')
    amount = fields.Float(string='Amount')
    
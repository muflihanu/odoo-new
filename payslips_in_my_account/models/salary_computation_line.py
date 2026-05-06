from odoo import fields,models
class SalaryComputationLine(models.Model):
    _name = "salary.computation.line"

    # salary_structure_id = fields.Many2one('salary.structure',string='Salary Structure')
    custom_payslip_id=fields.Many2one('custom.payslip',string='Custom Payslip')
    name = fields.Char(string='Name')
    amount = fields.Float(string='Amount')
    code = fields.Char(string='Code')
    category = fields.Char(string='Category')

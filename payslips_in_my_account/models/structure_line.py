from odoo import api, fields, models

class StructureLine(models.Model):
    _name = 'structure.line'
    _description = 'Structure line'

    # structure_type_name = fields.Char(string='Structure Name')
    # country_id = fields.Many2one(comodel_name='res.country', string='Country')
    # wage_type = fields.Selection(selection=[('fixed wage','Fixed Wage'),('hourly wage','Hourly Wage')],string='Wage Type')
    # sheduled_pay=fields.Selection(selection=[('month','Month'),('year','Year'),('week','Week')],string='Sheduled Pay')
    # working_hours=fields.Many2one('resource.calendar',string='Working Hours')

    line_name = fields.Char(string='Name')
    line_amount = fields.Float(string='Amount')
    code=fields.Char(string='Code')
    category=fields.Selection(selection=[('allowance','Allowance'),('deduction','Deduction'),('tax','Tax'),('commission','Commission')],string='Category')
    salary_structure_id = fields.Many2one('salary.structure')
    
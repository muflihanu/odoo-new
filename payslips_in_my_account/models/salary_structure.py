from odoo import fields,models

class SalaryStructure(models.Model):

    _name='salary.structure'
    _rec_name = 'structure_name'
    structure_name=fields.Char(string='Salary Structure Name')
    structure_line_ids=fields.One2many(comodel_name='structure.line',inverse_name='salary_structure_id',string='Salary Structure Lines')
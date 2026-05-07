from odoo import api, fields, models

class StructureType(models.Model):
    _name = 'structure.type'
    _description = 'Structure Type'

    # structure_type_name = fields.Char(string='Structure Name')
    # country_id = fields.Many2one(comodel_name='res.country', string='Country')
    # wage_type = fields.Selection(selection=[('fixed wage','Fixed Wage'),('hourly wage','Hourly Wage')],string='Wage Type')
    # sheduled_pay=fields.Selection(selection=[('month','Month'),('year','Year'),('week','Week')],string='Sheduled Pay')
    # working_hours=fields.Many2one('resource.calendar',string='Working Hours')
    
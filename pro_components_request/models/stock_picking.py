# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools

class StockPicking(models.Model):
    _inherit = "stock.picking"
    stock_employee_request_id = fields.Many2one('employee.request')
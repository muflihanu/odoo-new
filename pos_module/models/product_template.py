from odoo import api, fields, models
class ProductTemplate(models.Model):
    _inherit = "product.template"
    brand= fields.Char(string="Brand")
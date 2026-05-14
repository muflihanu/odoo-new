from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    mandatory_attachment_for_po=fields.Boolean(string="Mandatory Attachment for Purchase Order",default=False)
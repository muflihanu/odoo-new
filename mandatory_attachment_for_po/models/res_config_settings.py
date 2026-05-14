from odoo import fields, models,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    # company_id = fields.Many2one( comodel_name='res.company', required=True, index=True,default=lambda self: self.env.company)
    mandatory_attachment_for_po=fields.Boolean(string="Mandatory Attachment for Purchase Order",related='company_id.mandatory_attachment_for_po',readonly=False)
    # po_validation = fields.Selection(related='company_id.po_double_validation', string="Levels of Approvals *", readonly=False)



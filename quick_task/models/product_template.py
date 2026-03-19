from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    status=fields.Char(string="Status")

    @api.model
    def name_search(self, name='', domain=None, operator='ilike', limit=100):
        domain=[]

        if name:
            domain+=['|',('name', operator, name),('status', operator, name)]
        all_records=self.search(domain,limit=limit)
        return  [(record.id,record.display_name)for record in all_records]
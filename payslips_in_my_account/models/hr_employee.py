from odoo import fields, models,api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def playslip_in_my_account(self):
       print('hello')
       print(self.contract_date_start)
       print(self.contract_date_end)
       print(self.name)
       
       return
from odoo import http
from odoo.http import request

class user_payslip_controller(http.Controller):
     @http.route(["/user_payslips/"], type="http",auth="public",website=True)

     def user_payslips(self):
         print("user_payslips")
         return request.render('payslips_in_my_account.payslips_template')

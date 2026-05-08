from odoo import http
from odoo.http import request

class user_payslip_controller(http.Controller):


     @http.route(["/user_payslips/"], type="http",auth="public",website=True)

     def user_payslips(self):
         values=[]
         slip_record=self.env['custom.payslip'].search([('employee_id.name','=',self.env.user.name)])
         for record in slip_record:
             values.append({'payslip_id':record.id,'name':record.payslip_name,'from':record.from_date,'to':record.to_date})
         return request.render('payslips_in_my_account.payslips_template',{'values':values})


     @http.route(["/payslip_details/<int:payslip_id>"], type="http", auth="user", website=True)
     def payslip_details(self,payslip_id):
         values=[]
         salary_lines=[]
         total_value=0
         payslip_details=self.env['custom.payslip'].browse(payslip_id)
         for record in payslip_details:
             values.append({'slip_id':record.id,'number':record.payslip_name,'employee':record.employee_id.name,'emp_record':record.employee_record,'from':record.from_date,'to':record.to_date,'wage':record.wage})
             total_value=round(float(record.total),2)
             if record.salary_computation_line_ids:
                 for rec in record.salary_computation_line_ids:
                     amount=round(float(rec.amount),2)
                     salary_lines.append({'c_name':rec.name,'code':rec.code,'category':rec.category,'amount':amount})
         return request.render('payslips_in_my_account.payslips_details_template',{'vals':values,'salary_lines':salary_lines,'total_value':total_value})


     @http.route(['/payslip/mail/request/<int:payslip_id>'], type="http", auth="user", website=True)
     def payslip_mail_request(self,payslip_id):

         print('mail',payslip_id)

         return





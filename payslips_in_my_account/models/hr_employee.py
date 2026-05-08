from openpyxl.styles.builtins import total

from odoo import fields, models,api
from datetime import date
from odoo.tools import date_utils
from odoo import Command

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    custom_payslip_ids=fields.One2many('custom.payslip',inverse_name='employee_id',string="Customer Payslips")
    salary_structure_id=fields.Many2one('salary.structure',string="Salary Structure",required=True)

    def playslip_in_my_account(self):
       today = date.today()
       previous_month = date_utils.subtract(today, months=1)
       previous_month_first = date_utils.start_of(previous_month, "month")
       previous_month_last = date_utils.end_of(previous_month, "month")
       emp = self.env['hr.attendance'].search([('employee_id', '=', self.id), ('check_in', '>=', previous_month_first),
                                               ('check_out', '<=', previous_month_last)])
       full_time=self.resource_calendar_id.full_time_required_hours*4
       per_hour=self.wage/full_time
       total_worked_hours = 0
       for rec in emp:
           if rec.worked_hours:
              total_worked_hours+=rec.worked_hours
       if total_worked_hours == 0:
           return False
       salary=total_worked_hours*per_hour
       if salary>=self.wage:
           total_salary=self.wage
       else:
           total_salary=salary

       line_id= self.env['custom.payslip'].create({
           'employee_id': self.id,
           'employee_record':self.contract_date_start,
           'wage':self.wage,
           'working_hours':self.resource_calendar_id.id,
           'salary_structure_id':self.salary_structure_id.id,
           'custom_payslip_line_ids':[Command.create({
               'name':'Salary',
               'total_working_hours':total_worked_hours,
               'amount':total_salary,
           })]
       })


       return {
           'type': 'ir.actions.act_window',
           'name': 'custom payslip line',
           'view_mode': 'form',
           'res_model': 'custom.payslip',
           'res_id': line_id.id,

       }

    def get_payslip_record(self):
        """payslip record """
        records=[]
        for record in self:
            for rec in record.custom_payslip_ids:
                records.append(rec.id)

        return {
            'type': 'ir.actions.act_window',
            'name': 'payslip',
            'view_mode': 'list,form',
            'res_model': 'custom.payslip',
            'domain': [('id', 'in', records)],
            'target': 'current',
        }
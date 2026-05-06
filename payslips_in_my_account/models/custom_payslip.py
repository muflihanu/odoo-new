from odoo import api, fields, models, tools
from datetime import date
import calendar
from odoo.tools import  date_utils

class CustomPayslip(models.Model):

    _name = 'custom.payslip'

    employee_id = fields.Many2one('hr.employee',string='Employee')
    employee_record=fields.Date(string='Employee Record')
    from_date=fields.Date(string='From',default=lambda self:self.get_first_date())
    to_date=fields.Date(string='To',default=lambda self:self.get_last_date())
    wage=fields.Float(string='Wage')
    working_hours = fields.Many2one('resource.calendar', string='Working Hours')
    custom_payslip_line_ids=fields.One2many('custom.payslip.line',inverse_name='custom_payslip_id')
    salary_structure_id=fields.Many2one('salary.structure',string='Salary Structure',required=True)
    salary_computation_line_ids=fields.One2many('salary.computation.line',inverse_name='custom_payslip_id')
    total=fields.Float(string='Total')


    @api.model
    def get_first_date(self):
     today = date.today()
     previous_month = date_utils.subtract(today, months=1)
     return date_utils.start_of(previous_month, "month")

    @api.model
    def get_last_date(self):
        today = date.today()
        previous_month = date_utils.subtract(today, months=1)
        return date_utils.end_of(previous_month, "month")

    def compute_salary_and_others(self):
        print('compute_salary')
        if self.salary_structure_id:
          print( self.salary_structure_id.structure_line_ids)

          for record in self.salary_structure_id.structure_line_ids:
           line=self.env['salary.computation.line'].create({
               'custom_payslip_id':self.id,
              'name':record.line_name,
               'code':record.code,
               'category':record.category,
              'amount':record.line_amount } )


        return {
            'type': 'ir.actions.act_window',
            'name': 'custom payslip line',
            'view_mode': 'form',
            'res_model': 'custom.payslip',
            'res_id': self.id,
        }

    # @api.depends('salary_computation_line_ids')
    def _compute_total(self):
        total = 0
        if self.salary_computation_line_ids:
            for line in self.salary_computation_line_ids:
                if line:
                  print(line.category)
                  if line.category !='tax' or line.category !='deduction':

                    total += line.line_amount
                  else:
                    total -= line.line_amount
            print(total)
            # if total:
            #     self.total = total
            # else:
            #     self.total = 0
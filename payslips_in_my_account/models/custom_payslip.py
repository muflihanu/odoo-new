from odoo import api, fields, models, tools
from datetime import date
import calendar
from odoo.tools import  date_utils

class CustomPayslip(models.Model):

    _name = 'custom.payslip'
    _rec_name = 'payslip_name'

    payslip_name=fields.Char(string='Payslip',copy=False,readonly=True,default='New')
    employee_id = fields.Many2one('hr.employee',string='Employee')
    employee_record=fields.Date(string='Employee Record')
    from_date=fields.Date(string='From',default=lambda self:self.get_first_date())
    to_date=fields.Date(string='To',default=lambda self:self.get_last_date())
    wage=fields.Float(string='Wage')
    working_hours = fields.Many2one('resource.calendar', string='Working Hours')
    custom_payslip_line_ids=fields.One2many('custom.payslip.line',inverse_name='custom_payslip_id')
    salary_structure_id=fields.Many2one('salary.structure',string='Salary Structure',required=True)
    salary_computation_line_ids=fields.One2many('salary.computation.line',inverse_name='custom_payslip_id')
    total=fields.Float(string='Total',compute='compute_total',default=0)
    state=fields.Selection([('draft','Draft'),('confirmed','Confirmed') ],default='draft')


    @api.model
    def get_first_date(self):
     """previous month first date"""
     today = date.today()
     previous_month = date_utils.subtract(today, months=1)
     return date_utils.start_of(previous_month, "month")

    @api.model
    def get_last_date(self):
        """previous month last date"""
        today = date.today()
        previous_month = date_utils.subtract(today, months=1)
        return date_utils.end_of(previous_month, "month")

    def compute_salary_and_others(self):
        """computing salary and other allowance,tax,deduction"""
        lines=[]
        print('compute_salary')
        if self.custom_payslip_line_ids:
            for rec in self.custom_payslip_line_ids:
             lines.append((0,0,{
                'name': rec.name,
                'code':'SR',
                'category':'allowance',
                'amount': rec.amount,
            }))

        sales=self.env['sale.order'].search([('user_id.name','=',self.employee_id.name),('state','=','sale')])
        if sales:
         sale_amount=0
         for rec in sales:
             sale_amount+= rec.amount_total

         if sale_amount>4000:
          lines.append((0,0,{
             'name': 'Sale Commission',
             'code': 'SC',
             'category': 'commission',
             'amount':sale_amount*5/100,
         }))

        if self.salary_structure_id:
          for record in self.salary_structure_id.structure_line_ids:
            lines.append((0,0,{
             'custom_payslip_id':self.id,
              'name':record.line_name,
            'code':record.code,
              'category':record.category,
              'amount':record.line_amount,
            }))
          self.salary_computation_line_ids=lines
          self.state='confirmed'

        return {
            'type': 'ir.actions.act_window',
            'name': 'custom payslip line',
            'view_mode': 'form',
            'res_model': 'custom.payslip',
            'res_id': self.id,
        }

    @api.depends('salary_computation_line_ids')
    def compute_total(self):
        """compute total computation line"""
        total = 0
        if self.salary_computation_line_ids:
            for line in self.salary_computation_line_ids:
                  if line.category =='allowance' or line.category=='commission':
                    total += line.amount
                  else:
                    total - line.amount
            print(total)
            if total>0:
                self.total = round(total,2)
            else:
                self.total = None
        else:
            self.total = None


    @api.model_create_multi
    def create(self, vals):
        """create sequence"""
        for sequence in vals:
            sequence['payslip_name'] = self.env['ir.sequence'].next_by_code('custom.payslip_code')

        res = super().create(vals)
        return res

    def _get_report_base_filename(self):
        self.ensure_one()
        return self.payslip_name
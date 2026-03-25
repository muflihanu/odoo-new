from odoo import api, fields, models
from odoo.exceptions import ValidationError
class HotelManagementReportWizard(models.TransientModel):
    _name = "hotel.management.report.wizard"
    _description = "Hotel Management Report Wizard"


    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    # guest= fields.Char(string="Guest")
    guest=fields.Many2one('res.partner',string="Guest")



    def action_report_wizard(self):

        if self.from_date and self.to_date and self.guest:
           query=f''' SELECT id,guest_id,check_in,check_out,state from hotel_accommodation WHERE  guest_id={self.guest.id}  AND check_in='{self.from_date}' AND expected_date='{self.to_date}' '''
           self.env.cr.execute(query)
           all_rec=self.env.cr.dictfetchall()
           data = {'date': self.read()[0],'report': all_rec}
           return self.env.ref('hotel_management.action_report_hotel_management').report_action(None,data=data)
           # all_ids=[]
           # for rec in all_rec:
           #   all_ids.append(rec[0])
           #
           #
           #   print(rec)
           #   get_records=self.env['hotel.accommodation'].search([('id','in',all_ids)])
           #
           #   for record  in get_records:
           #       print(record.reference_number)
           #   print(all_ids)






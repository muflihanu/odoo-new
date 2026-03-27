from odoo import api, fields, models
from odoo.exceptions import ValidationError
import io
import json
import xlsxwriter
from odoo.tools import json_default
class HotelManagementReportWizard(models.TransientModel):
    _name = "hotel.management.report.wizard"
    _description = "Hotel Management Report Wizard"


    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    # guest= fields.Char(string="Guest")
    guest=fields.Many2one('res.partner',string="Guest")



    def action_report_wizard(self):

        if self.from_date and self.to_date and self.guest:
           query=f''' SELECT m.reference_number,p.name,m.check_in,m.check_out,m.state from hotel_accommodation AS m  INNER JOIN res_partner AS p ON   p.id=m.guest_id  WHERE guest_id={self.guest.id}  AND check_in='{self.from_date}' AND expected_date='{self.to_date}' '''
           self.env.cr.execute(query)
           all_rec=self.env.cr.dictfetchall()
           data = {'date':self.read()[0],'report': all_rec}

           return self.env.ref('hotel_management.action_report_hotel_management').report_action(self,data=data)


class HotelManagementReportPDF(models.AbstractModel):
    _name = "report.hotel_management.hotel_management_report"

    @api.model
    def _get_report_values(self,docids,data=None):
        print(data)
        return {
            'doc_ids': docids,
            'doc_model': 'hotel.accommodation',
            'docs':1,
            'data': data,
        }








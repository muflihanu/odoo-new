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

    def get_values(self):
        print('values',self.guest,self.from_date,self.to_date)
        query = f''' SELECT m.reference_number,p.name,m.check_in,m.check_out,m.state from hotel_accommodation AS m  INNER JOIN res_partner AS p ON   p.id=m.guest_id  WHERE '''
        if self.from_date and self.to_date and self.guest:
            query += f''' guest_id={self.guest.id}  AND check_in BETWEEN'{self.from_date}' AND '{self.to_date}' ORDER BY reference_number '''
        elif self.from_date:
            query += f'''  check_in  BETWEEN '{self.from_date}' AND '{fields.Datetime.now()}' ORDER BY reference_number '''
        elif self.to_date:
            query += f'''  check_in<='{self.to_date}'  ORDER BY reference_number'''
        elif self.guest:
            query += f''' guest_id={self.guest.id} ORDER BY reference_number '''
        elif self.from_date and self.to_date:
            query += f''' check_in BETWEEN'{self.from_date}' AND '{self.to_date}' '''
        else:
            query = f''' SELECT m.reference_number,p.name,m.check_in,m.check_out,m.state from hotel_accommodation AS m  INNER JOIN res_partner AS p ON   p.id=m.guest_id  ORDER BY reference_number'''

        self.env.cr.execute(query)
        all_rec = self.env.cr.dictfetchall()
        return all_rec


    def action_report_wizard(self):

        record= self.get_values()

        data = {'date': self.read()[0], 'report': record}
        return self.env.ref('hotel_management.action_report_hotel_management').report_action(self, data=data)

    def xlsx_accommodation_report(self):

      rec=self.get_values()

      xl_data = {'from_date': self.from_date, 'to_date': self.to_date, 'guest': self.guest.name, 'report':rec}
      return {
        'type':'ir.actions.report',
        'data':{
            'model':'hotel.management.report.wizard',
            'options':json.dumps(xl_data,default=json_default),
            'output_format': 'xlsx',
            'report_name': 'Hotel Management Excel Report',
        },
        'report_type': 'xlsx',
    }

    def get_xlsx_report(self, xl_data, response):

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '8px', 'align': 'center','border':3,})
        theading=workbook.add_format({'align': 'center', 'bold': True, 'font_size': '8px','border':3})
        sheet.set_column(0, 2, 15)
        sheet.set_column(0, 4, 15)

        sheet.merge_range('B2:I3', 'EXCEL REPORT', head)
        sheet.merge_range('A4:B4', 'Customer:', cell_format)if xl_data['guest'] else sheet.merge_range('A4:B4', '', cell_format)
        sheet.merge_range('C4:D4', xl_data['guest'], cell_format) if xl_data['guest'] else sheet.merge_range('C4:D4','', cell_format)


        sheet.merge_range('A5:B5', 'From Date:', cell_format) if xl_data['from_date'] else sheet.merge_range('A5:B5','', cell_format)
        sheet.merge_range('C5:D5', xl_data['from_date'], cell_format) if xl_data['from_date'] else sheet.merge_range('C5:D5','', cell_format)
        sheet.merge_range('A6:B6', 'To Date:', cell_format) if xl_data['to_date'] else sheet.merge_range('A6:B6','', cell_format)
        sheet.merge_range('C6:D6', xl_data['to_date'], cell_format) if xl_data['to_date'] else sheet.merge_range('C6:D6','', cell_format)

        sheet.write('B10', 'SL.NO',theading)
        sheet.write('C10', 'GUEST',theading)
        sheet.write('D10', 'CHECK IN',theading)
        sheet.write('E10', 'CHECK OUT',theading)
        sheet.write('F10', 'STATE',theading)
        row = 10
        for i in xl_data['report']:
            col = 1
            sheet.write(row,col,i['reference_number'],txt)
            col+=1
            sheet.write(row,col,i['name'],txt)
            col+=1
            sheet.write(row, col, i['check_in'], txt)
            col += 1
            sheet.write(row, col, i['check_out'], txt)
            col += 1
            sheet.write(row, col, i['state'], txt)
            row += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()





class HotelManagementReportPDF(models.AbstractModel):
    _name = "report.hotel_management.hotel_management_report"

    @api.model
    def _get_report_values(self,docids,data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'hotel.accommodation',
            'docs':1,
            'data': data,
        }








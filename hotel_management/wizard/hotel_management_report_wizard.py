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
           if all_rec:
               data = {'date':self.read()[0],'report': all_rec}
               return self.env.ref('hotel_management.action_report_hotel_management').report_action(self,data=data)

        elif self.from_date:
            query = f''' SELECT m.reference_number,p.name,m.check_in,m.check_out,m.state from hotel_accommodation AS m  INNER JOIN res_partner AS p ON   p.id=m.guest_id  WHERE   check_in='{self.from_date}' '''
            self.env.cr.execute(query)
            all_rec = self.env.cr.dictfetchall()
            if all_rec:
                data = {'date': self.read()[0], 'report': all_rec}
                return self.env.ref('hotel_management.action_report_hotel_management').report_action(self, data=data)

        elif self.to_date:
            query = f''' SELECT m.reference_number,p.name,m.check_in,m.check_out,m.state from hotel_accommodation AS m  INNER JOIN res_partner AS p ON   p.id=m.guest_id  WHERE   expected_date='{self.to_date}' '''
            self.env.cr.execute(query)
            all_rec = self.env.cr.dictfetchall()
            if all_rec:
                data = {'date': self.read()[0], 'report': all_rec}
                return self.env.ref('hotel_management.action_report_hotel_management').report_action(self, data=data)

        elif self.guest:
            query = f''' SELECT m.reference_number,p.name,m.check_in,m.check_out,m.state from hotel_accommodation AS m  INNER JOIN res_partner AS p ON   p.id=m.guest_id  WHERE   guest_id={self.guest.id} '''
            self.env.cr.execute(query)
            all_rec = self.env.cr.dictfetchall()
            if all_rec:
                data = {'date': self.read()[0], 'report': all_rec}
                return self.env.ref('hotel_management.action_report_hotel_management').report_action(self, data=data)

        elif self.from_date and self.to_date:
            query = f''' SELECT m.reference_number,p.name,m.check_in,m.check_out,m.state from hotel_accommodation AS m  INNER JOIN res_partner AS p ON   p.id=m.guest_id  WHERE   check_in='{self.from_date}' AND expected_date='{self.to_date}' '''
            self.env.cr.execute(query)
            all_rec = self.env.cr.dictfetchall()
            if all_rec:
                data = {'date': self.read()[0], 'report': all_rec}
                return self.env.ref('hotel_management.action_report_hotel_management').report_action(self, data=data)
        else:
            return False

    def xlsx_accommodation_report(self):
      if self.guest and self.from_date and self.to_date:
        xl_query=f""" SELECT m.reference_number ,p.name,m.check_in,m.check_out,m.state From hotel_accommodation AS m INNER JOIN res_partner AS p ON p.id=m.guest_id WHERE  guest_id={self.guest.id}  AND check_in='{self.from_date}' AND expected_date='{self.to_date}' """
        self.env.cr.execute(xl_query)
        xls_report=self.env.cr.dictfetchall()
        xl_data={'from_date':self.from_date,'to_date':self.to_date,'guest':self.guest.name,'report':xls_report}
      elif  self.from_date and self.to_date:
          xl_query = f""" SELECT m.reference_number ,p.name,m.check_in,m.check_out,m.state From hotel_accommodation AS m INNER JOIN res_partner AS p ON p.id=m.guest_id WHERE  check_in='{self.from_date}' AND expected_date='{self.to_date}' """
          self.env.cr.execute(xl_query)
          xls_report = self.env.cr.dictfetchall()
          xl_data = {'from_date': self.from_date, 'to_date': self.to_date,'guest':self.guest.name, 'report': xls_report}
      elif self.from_date:
          xl_query = f""" SELECT m.reference_number ,p.name,m.check_in,m.check_out,m.state From hotel_accommodation AS m INNER JOIN res_partner AS p ON p.id=m.guest_id WHERE  check_in='{self.from_date}' """
          self.env.cr.execute(xl_query)
          xls_report = self.env.cr.dictfetchall()
          xl_data = {'from_date': self.from_date, 'to_date': self.to_date,'guest':self.guest.name,'report': xls_report}
      elif self.to_date:
          xl_query = f""" SELECT m.reference_number ,p.name,m.check_in,m.check_out,m.state From hotel_accommodation AS m INNER JOIN res_partner AS p ON p.id=m.guest_id WHERE expected_date='{self.to_date}'  """
          self.env.cr.execute(xl_query)
          xls_report = self.env.cr.dictfetchall()
          xl_data = {'from_date': self.from_date, 'to_date': self.to_date,'guest':self.guest.name,'report': xls_report}
      elif self.guest:
          xl_query = f""" SELECT m.reference_number ,p.name,m.check_in,m.check_out,m.state From hotel_accommodation AS m INNER JOIN res_partner AS p ON p.id=m.guest_id WHERE guest_id={self.guest.id}  """
          self.env.cr.execute(xl_query)
          xls_report = self.env.cr.dictfetchall()
          xl_data = {'from_date': self.from_date, 'to_date': self.to_date,'guest':self.guest.name,'report': xls_report}
      else:
          xl_query = f""" SELECT m.reference_number ,p.name,m.check_in,m.check_out,m.state From hotel_accommodation AS m INNER JOIN res_partner AS p ON p.id=m.guest_id  """
          self.env.cr.execute(xl_query)
          xls_report = self.env.cr.dictfetchall()
          xl_data = {'from_date': self.from_date, 'to_date': self.to_date, 'guest': self.guest.name, 'report': xls_report}
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

        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})

        sheet.merge_range('B2:I3', 'EXCEL REPORT', head)
        sheet.merge_range('A4:B4', 'Customer:', cell_format)
        if xl_data['guest']:
            sheet.merge_range('C4:D4', xl_data['guest'], cell_format)
        else:
            sheet.merge_range('C4:D4','', cell_format)

        sheet.merge_range('A5:B5', 'from_date:', cell_format)
        sheet.merge_range('C5:D5', xl_data['from_date'], cell_format)
        sheet.merge_range('A6:B6', 'to_date:', cell_format)
        sheet.merge_range('C6:D6', xl_data['to_date'], cell_format)


        sheet.write('I10:J10', 'SL.NO')
        sheet.write('K10:L10', 'GUEST')
        sheet.write('M10:N10', 'CHECK IN')
        sheet.write('O10:P10', 'CHECK OUT')
        sheet.write('Q10:R10', 'STATE')
        row = 11
        for i in xl_data['report']:
            col = 8
            sheet.write(row,col,i['reference_number'],txt)
            col+=2
            sheet.write(row,col,i['name'],txt)
            col+=2
            sheet.write(row, col, i['check_in'], txt)
            col += 2
            sheet.write(row, col, i['check_out'], txt)
            col += 2
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
        print(data)
        return {
            'doc_ids': docids,
            'doc_model': 'hotel.accommodation',
            'docs':1,
            'data': data,
        }








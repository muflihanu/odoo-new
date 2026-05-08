
from odoo import http
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager


class CustomerPortal(portal.CustomerPortal):

    @http.route(["/payslip_print/<int:slip_id>"], type="http", auth="user", website=True)
    def payslip_print(self, slip_id,access_token=None):
        """download the payslip details"""
        model = self._document_check_access('custom.payslip', slip_id, access_token=access_token)
        return self._show_report(model=model, report_type='pdf', report_ref='payslips_in_my_account.action_report_payslips_in_my_account',  download=True)

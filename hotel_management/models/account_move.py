from odoo import fields, models, api

class AccountMove(models.Model):

    _inherit = 'account.move'
    accommodation_id =fields.Many2one(comodel_name='hotel.accommodation', ondelete='cascade')
    # accommodation_id = fields.One2many('hotel.accommodation','invoice_idd')


    @api.depends('payment_state', 'state', 'is_move_sent','accommodation_id')
    def _compute_status_in_payment(self):
        for record in self:
            if record.payment_state=='paid':
                record.accommodation_id.payment_status='paid'

            elif record.payment_state=='not paid':
                record.accommodation_id.payment_status='not_paid'
                print('mmmmmm')
            else:
                record.accommodation_id.payment_status = 'not_paid'

        return super(AccountMove,self)._compute_status_in_payment()
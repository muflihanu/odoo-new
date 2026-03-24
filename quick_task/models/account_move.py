import typing

from odoo import fields,models,api
from odoo import Command



class AccountMove(models.Model):
    _inherit='account.move'
    partner_related_so = fields.Many2many('sale.order', string='Related SO', tracking=True, compute='compute_related_os_ids')
    related_so=fields.Many2many('sale.order',string='Related SO',copy=False)






    @api.depends('partner_id')
    def compute_related_os_ids(self):
        for record in self:
            all_records=[]
            if record.partner_id:
                so=self.env['sale.order'].search([('partner_id','=',self.partner_id)])
                for rec in so:
                  all_records.append(rec.id)
            else:
                self.partner_related_so=None
            self.write({'partner_related_so':[(6, 0, all_records)]})


    @api.onchange('related_so')
    def onchange_related_so(self):
        self.invoice_line_ids=[Command.clear()]
        if  self.related_so:
            unique_id=[]
            for record in self.related_so:
                for record in self:
                    if record.id not in unique_id:
                        unique_id.append(record.id)
                    if record.id not in unique_id:
                        record.clear()
                        self.update({
                        'invoice_line_ids': [Command.create({
                            'product_id': rec.product_id.id,
                            'price_unit': rec.price_unit,
                            'quantity':rec.product_uom_qty,
                         })  for rec in record.order_line ]})

            print(unique_id)

    def action_post(self):
        if self.related_so:
            self.related_so.invoice_status='no'
        return super(AccountMove,self).action_post()



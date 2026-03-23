import typing

from odoo import fields,models,api
from odoo import Command
from odoo.orm.types import ValuesType


class AccountMove(models.Model):
    _inherit='account.move'
    partner_related_so = fields.Many2many('sale.order', string='Related SO', tracking=True, compute='compute_related_os_ids')
    related_so=fields.Many2many('sale.order',string='Related SO',copy=False)




    related_so=fields.Many2many('sale.order',string='Related SO',domain=[('invoice_status','in','to invoice')])



    @api.onchange('related_so')
    def onchange_related_so(self):

        if self.related_so:
            all_product = []
            for record in self.related_so:
                all_product.append(record.order_line.order_id.id)
                for rec in record.order_line:

                    print("order_id",rec.order_id.id)
                    print(rec.product_id.name)
                    print(rec.price_unit)
                print(all_product)

                self.update({
                    'invoice_line_ids':[Command.create({
                        'product_id':rec.product_id.id,
                        'price_unit':rec.price_unit,
                    })for rec in record.order_line]})





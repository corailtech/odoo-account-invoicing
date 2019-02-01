# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    @api.onchange('fiscal_position_id')
    def _onchange_fiscal_position_id(self):
        _logger.warning('tax_auto _onchange_fiscal_position_id')
        self._onchange_invoice_line_ids()
        return

    @api.onchange('invoice_line_ids')
    def _onchange_invoice_line_ids(self):
        super(AccountInvoice, self)._onchange_invoice_line_ids()
        _logger.warning('tax_auto _onchange_invoice_line_ids.')
        tax_auto_ids = self.env['account.tax'].search([('auto_tax', '=', True)])
        fpos = self.fiscal_position_id
        _logger.warning('tax_auto_ids = self.env[...')
        tax_auto_ids = fpos.map_tax(tax_auto_ids)
        for tax in tax_auto_ids:
            _logger.warning('tax auto name (%s)',tax['name'])
            self.tax_line_ids += self.env['account.invoice.tax'].new({
                'invoice_id': self.id,
                'name': tax['name'],
                'tax_id': tax['id'],
                'amount': tax['amount'],
                #'base': 0.0,
                'manual': False,
                'sequence': tax['sequence'],
                'account_id': tax['refund_account_id'],
            })
        return

class AccountTax(models.Model):
    _inherit = 'account.tax'
    auto_tax = fields.Boolean(default=False, string='Tax automatically added to invoice')

def map_tax(self, taxes, product=None, partner=None):
        result = self.env['account.tax'].browse()
        for tax in taxes:
            tax_count = 0
            for t in self.tax_ids:
                if t.tax_src_id == tax:
                    tax_count += 1
                    if t.tax_dest_id:
                        result |= t.tax_dest_id
            if not tax_count:
                result |= tax
        return result
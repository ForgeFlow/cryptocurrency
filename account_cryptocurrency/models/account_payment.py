# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    res_currency_move_ids = fields.One2many(
        'res.currency.move', 'payment_id', readonly=True, copy=False,
        ondelete='cascade')

    def _prepare_currency_inventory_move(self, amount):
        return {
            'payment_id': self.id,
            'amount': abs(amount),
            'currency_id': self.currency_id.id,
            'company_id': self.company_id.id,
            'date': self.payment_date,
            'direction': self.payment_type,
            'journal_id': self.journal_id.id,
        }

    def _create_payment_entry(self, amount):
        res = super(AccountPayment, self)._create_payment_entry(amount)
        if self.currency_id.inventoried:
            curr_inv_move_data = self._prepare_currency_inventory_move(amount)
            curr_inv_move = self.env['res.currency.move'].create(
                curr_inv_move_data)
            curr_inv_move.post()
        return res

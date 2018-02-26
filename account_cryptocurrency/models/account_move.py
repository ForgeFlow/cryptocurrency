# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    res_currency_move_line_id = fields.Many2one(
        'res.currency.move.line', readonly=True, copy=False,
        ondelete='cascade')

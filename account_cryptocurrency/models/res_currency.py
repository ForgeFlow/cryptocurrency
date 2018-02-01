# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

_VALUATION_METHODS = [
    ('fifo', 'First-in-First Out'),
    ('average', 'Average'),
]


class ResCurrency(models.Model):
    _inherit = "res.currency"

    inventoried = fields.Boolean('Inventoried')
    valuation_method = fields.Selection(selection=_VALUATION_METHODS,
                                        string='Valuation Method')
    inventory_account_id = fields.Many2one('account.account',
                                           string='Inventory Account',
                                           company_dependent=True)

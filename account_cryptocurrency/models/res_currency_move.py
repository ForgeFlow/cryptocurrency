# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _
from odoo.exceptions import ValidationError

_STATES = [
    ('draft', 'Draft'),
    ('posted', 'Posted'),
]

_DIRECTIONS = [
    ('inbound', 'Receive Money'),
    ('outbound', 'Send Money'),
]


class ResCurrencyMove(models.Model):
    _name = "res.currency.move"
    _description = 'Currency Move'

    name = fields.Char(index=True, required=True)
    payment_id = fields.Many2one('account.payment',
                                 string='Payment')
    amount = fields.Float('Amount')
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  ondelete='restrict', required=True)
    date = fields.Date(string='Payment Date',
                       default=fields.Date.context_today, required=True,
                       copy=False)
    journal_id = fields.Many2one('account.journal',
                                 string='Account Journal',
                                 required=True)
    state = fields.Selection(selection=_STATES, required=True,
                             default='draft')

    company_id = fields.Many2one('res.company', string='Company',
                                 required=True)
    direction = fields.Selection(selection=_DIRECTIONS,
                                 string='Direction', required=True)
    move_line_ids = fields.One2many('res.currency.move.line', 'move_id',
                                    string='Currency move lines')

    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'res.currency.move')
        return super(ResCurrencyMove, self).create(vals)

    def _prepare_incoming_move_line(self):
        self.ensure_one()
        amount = self.currency_id.with_context(date=self.date).compute(
            self.amount, self.company_id.currency_id)
        return {
            'move_id': self.id,
            'quantity': self.amount,
            'date': self.date,
            'amount': amount,
        }

    def _prepare_outgoing_move_line(self, candidate, qty):
        self.ensure_one()
        return {
            'move_id': self.id,
            'quantity': qty,
            'date': self.date,
            'in_move_line_id': candidate.id,
            'amount': candidate.price_unit * qty
        }

    def _get_fifo_candidates_in_move_line(self):
        """ Find IN moves that can be used to value OUT moves.
        """
        self.ensure_one()
        domain = [('currency_id', '=', self.currency_id.id),
                  ('remaining_qty', '>', 0.0)] + self.env[
            'res.currency.move.line']._get_in_base_domain(
            company_id=self.company_id.id)
        candidates = self.env['res.currency.move.line'].search(
            domain, order='date, id')
        return candidates

    def _run_fifo(self):
        self.ensure_one()
        qty_to_take_on_candidates = self.amount
        candidates = self._get_fifo_candidates_in_move_line()
        for candidate in candidates:
            if not candidate.remaining_qty:
                continue
            if candidate.remaining_qty <= qty_to_take_on_candidates:
                qty_taken_on_candidate = candidate.remaining_qty
            else:
                qty_taken_on_candidate = qty_to_take_on_candidates
            move_line_data = self._prepare_outgoing_move_line(
                candidate, qty_taken_on_candidate)
            self.env['res.currency.move.line'].create(move_line_data)
            qty_to_take_on_candidates -= qty_taken_on_candidate
        if qty_to_take_on_candidates:
            raise ValidationError(_('It was not possible to find enough '
                                    'currency units from incoming moves'))
        return True

    def post(self):
        for rec in self:
            if rec.direction == 'inbound':
                move_line_data = rec._prepare_incoming_move_line()
                self.env['res.currency.move.line'].create(
                    move_line_data)
            elif rec.direction == 'outbound':
                self._run_fifo()
            rec.state = 'posted'

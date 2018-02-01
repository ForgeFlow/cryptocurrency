# -*- coding: utf-8 -*-
#  Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
import time
import odoo.tests.common as common
from odoo import fields


class TestAccountCryptocurrency(common.TransactionCase):

    def setUp(self):
        res = super(TestAccountCryptocurrency, self).setUp()
        self.company = self.env.ref('base.main_company')
        self.receivable_account = self.env['account.account'].search(
            [('user_type_id', '=', self.env.ref(
                'account.data_account_type_receivable').id),
             ('company_id', '=', self.company.id)],
            limit=1)
        self.account_expenses = self.env['account.account'].search(
            [('user_type_id', '=', self.env.ref(
                'account.data_account_type_expenses').id),
             ('company_id', '=', self.company.id)],
            limit=1)
        self.account_revenue = self.env['account.account'].search(
            [('user_type_id', '=', self.env.ref(
                'account.data_account_type_revenue').id),
             ('company_id', '=', self.company.id)],
            limit=1)

        self.inventory_account = self.env['account.account'].create({
            'name': 'CC Inventory',
            'code': '9991',
            'company_id': self.company.id,
            'user_type_id': self.env.ref(
                'account.data_account_type_current_assets').id

        })
        self.to_inventory_account = self.env['account.account'].create({
            'name': 'CC To Inventory',
            'code': '9992',
            'company_id': self.company.id,
            'user_type_id': self.env.ref(
                'account.data_account_type_current_assets').id

        })
        self.currency_cc = self.env['res.currency'].with_context(
            company_id=self.company.id,
            force_company=self.company.id).create({
                'name': 'CC',
                'rounding': 0.010000,
                'symbol': 'CC',
                'position': 'after',
                'inventoried': True,
                'valuation_method': 'fifo',
                'inventory_account_id': self.inventory_account.id,
        })
        self.customer = self.env['res.partner'].create({
            'name': 'Test customer',
            'customer': True,
        })
        self.cc_journal = self.env['account.journal'].create({
            'name': 'CC Payments Journal',
            'code': 'CC',
            'type': 'bank',
            'company_id': self.company.id,
            'default_debit_account_id': self.to_inventory_account.id,
            'default_credit_account_id': self.to_inventory_account.id,

        })
        # We want to make sure that the company has no rates, that would
        # screw up the conversions.
        company_rates = self.env['res.currency.rate'].search(
            [('currency_id', '=', self.company.currency_id.id)])
        company_rates.unlink()

        return res

    def test_01(self):
        """ Implements test for scenario 1 as defined in the repository
        readme """
        ####
        # Day 1: Invoice Cust/001 to customer (expressed in CC)
        # Market value of CC (day 1): 1 CC = $0.5
        # * Dr. 100 CC / $50 - Accounts receivable
        # * Cr. 100 CC / $50 - Revenue
        ####
        invoice_cust_001 = self.env['account.invoice'].create({
            'partner_id': self.customer.id,
            'account_id': self.receivable_account.id,
            'type': 'out_invoice',
            'currency_id': self.currency_cc.id,
            'company_id': self.company.id,
            'date_invoice': time.strftime('%Y') + '-01-01',
        })
        self.env['account.invoice.line'].create({
            'product_id': self.env.ref('product.product_product_4').id,
            'quantity': 1.0,
            'price_unit': 100.0,
            'invoice_id': invoice_cust_001.id,
            'name': 'product that cost 100',
            'account_id': self.account_revenue.id,
        })
        self.env['res.currency.rate'].create({
            'currency_id': self.currency_cc.id,
            'name': time.strftime('%Y') + '-01-01',
            'rate': 2,
        })
        invoice_cust_001.action_invoice_open()
        self.assertEqual(invoice_cust_001.residual_company_signed, 50.0)
        aml = invoice_cust_001.move_id.mapped('line_ids').filtered(
            lambda x: x.account_id == self.account_revenue)
        self.assertEqual(aml.credit, 50.0)
        #####
        # Day 2: Receive payment for half invoice Cust/001 (in CC)
        # -------------------------------------------------------
        # Market value of CC (day 2): 1 CC = $0.8

        # Payment transaction:
        # * Dr. 50 CC / $40 - CC To Inventory (valued at market price
        # at the time of receiving the coins)
        # * Cr. 50 CC / $40 - Accounts Receivable

        # Actual receipt of the coins:
        # * Dr. 50 CC / $40 - CC Inventory (valued at market price
        # at the time of receiving the coins)
        # * Cr. 50 CC / $40 - CC To Inventory
        #####
        # Instead of changing day we just change the rate
        self.env['res.currency.rate'].create({
            'currency_id': self.currency_cc.id,
            'name': time.strftime('%Y') + '-01-02',
            'rate': 1.25,
        })
        # register payment on invoice
        payment = self.env['account.payment'].create(
            {'payment_type': 'inbound',
             'payment_method_id': self.env.ref(
                 'account.account_payment_method_manual_in').id,
             'partner_type': 'customer',
             'partner_id': self.customer.id,
             'amount': 50,
             'currency_id': self.currency_cc.id,
             'payment_date': time.strftime('%Y') + '-01-02',
             'journal_id': self.cc_journal.id,
             })
        payment.post()
        payment_move_line = False
        for l in payment.move_line_ids:
            if l.account_id == self.receivable_account:
                payment_move_line = l
        invoice_cust_001.register_payment(payment_move_line)
        self.assertEqual(invoice_cust_001.state, 'open')
        aml = payment.move_line_ids.filtered(
            lambda x: x.account_id == self.receivable_account)
        self.assertEqual(aml.amount_currency, -50.0)
        self.assertEqual(aml.credit, 40.0)
        # Inventory of CC (day 1)
        # ----------------------
        # day 2:
        # 50 CC @$0,8/CC (total valuation of coins received /
        # number of coins received)
        cc_ml = payment.res_currency_move_ids.mapped(
            'move_line_ids')[0]
        self.assertEqual(cc_ml.quantity, 50.0)
        self.assertEqual(cc_ml.amount, 40.0)
        self.assertEqual(cc_ml.price_unit, 0.8)
        ####
        # Day 3: Receive remaining payment for invoice Cust/001 (in CC)
        # -------------------------------------------------------------
        # Market value of CC (day 3): 1 CC = $2
        #
        # Payment transaction:
        # * Dr. 50 CC / $100 - CC To Inventory (valued at market price at
        #   the time of receiving the coins)
        # * Cr. 50 CC / $100 - Accounts Receivable
        # Actual receipt of the coins:
        # * Dr. 50 CC / $100 - CC Inventory (valued at market price at the
        # time of receiving the coins)
        # * Cr. 50 CC / $100 - CC To Inventory
        # Full invoice reconciliation. Realization of the full transaction
        # gain/loss:
        # * Dr. 0 CC / $90 - Accounts Receivable
        # * Cr. 0 CC / $90 - Crypto currency exchange gain
        ####
        self.env['res.currency.rate'].create({
            'currency_id': self.currency_cc.id,
            'name': time.strftime('%Y') + '-01-03',
            'rate': 0.5,
        })
        # register payment on invoice
        payment = self.env['account.payment'].create(
            {'payment_type': 'inbound',
             'payment_method_id': self.env.ref(
                 'account.account_payment_method_manual_in').id,
             'partner_type': 'customer',
             'partner_id': self.customer.id,
             'amount': 50,
             'currency_id': self.currency_cc.id,
             'payment_date': time.strftime('%Y') + '-01-03',
             'journal_id': self.cc_journal.id,
             })
        payment.post()
        payment_move_line = False
        for l in payment.move_line_ids:
            if l.account_id == self.receivable_account:
                payment_move_line = l
        invoice_cust_001.register_payment(payment_move_line)
        self.assertEqual(invoice_cust_001.state, 'paid')
        aml = payment.move_line_ids.filtered(
            lambda x: x.account_id == self.receivable_account)
        self.assertEqual(aml.amount_currency, -50.0)
        self.assertEqual(aml.credit, 100.0)
        # Inventory of CC (day 3)
        # -----------------------
        # day 1:
        # * 50 CC @$0,98/CC
        # day 3:
        # * 50 CC @$2,00/CC
        cc_ml = payment.res_currency_move_ids.mapped(
            'move_line_ids')[0]
        self.assertEqual(cc_ml.quantity, 50.0)
        self.assertEqual(cc_ml.amount, 100.0)
        self.assertEqual(cc_ml.price_unit, 2)


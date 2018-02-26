.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

=======================
Account Crypto Currency
=======================

This module provides basic support for the management of cryptocurrencies.


Installation
============

* Install the module 'account_invoicing' to be able to display the menus.

Configuration
=============

* For the user that will do the configuration, make sure to activate the
  option 'Show Full Accounting Features' in the user profile.

* Activate the Multi-Currency in 'Invoicing / Configuration /
  Settings / Multi-Currencies.

* Create the crypto currency in 'Invoicing / Configuration / Accounting /
  Currencies'. Complete the following fields:  'Inventoried', 'Valuation
  Method'.

* Add to the crypto currency an 'Inventory Account'. This Account must
  indicate in field 'Account Currency' the same currency.

* Create an Account Journal associated to the payments of the crypto
  currency, in 'Invoicing / Configuration / Accounting / Journals'. Indicate
  in the 'Currency' field the crypto currency. In the 'Default Credit Account'
  and 'Default Debit Account' you should indicate a new Account of type
  'Expenses', with a name similar to 'Crypto currency X Gain/Loss'. The new
  Account must also refer to the crypto currency account.


Additional remarks:

 * In case that your company currency is not EUR, make sure that the main
   company currency has no exchange rates. Go to 'Invoicing / Configuration /
   Accounting / Currencies' and for the company currency press the
   button 'Rates' and delete any rate listed.



Known issues / Roadmap
======================



Credits
=======

Contributors
------------

* Jordi Ballester <jordi.ballester@eficent.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

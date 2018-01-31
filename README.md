
Cryptocurrency
==============

This project intends to implement cryptocurrency support for OCA.


# Accounting background

* Cryptocurrencies are considered property from a taxation standpoint.

* This means that every time that you receive or send cryptocurrencies,
  you are entering into a taxable transaction, and will need to report on the
  gain/loss resulting from the receipt/issue of the cryptocurrency.

* Cryptocurrencies are similar to currencies, and can be used in the exchange
  of goods and services between entities.

* When you receive cryptocurrencies (in exchange for goods delivered,
  service rendered or because you mined it), that translates into taxable
  income to the recipient. The valuation should be based on the market value of
  the cryptocurrency at the time of receipt, and it can be provided by a
  third party (e.g. the exchange platform) or needs to be identified by you somehow.

* You have to retain the cost of the crytptocurrency for as long as you keep it.

* When you pay out cryptocurrencies (in exchange for goods or services
  purchased, or if you exchanged fpr another crypto or normal currency) this
  constitutes again a taxable transaction. In that case the gain/loss is
  computed as the difference between the cost of the cryptocurrency that
  you pay with, and the value of what you receive back, valued in your
  operating normal currency.

* For example, if I buy 1 chair valued at $2 with 1 crypto that cost me $1,
  my gain is $1.

* So, every time that I pay with crypto, I need to value in terms of the
  reportable company currency what I receive back in exchange.

* I understand that if you purchase something that is advertised in
  normal currency, and pay with crypto, the sale price is determined as
  advertised.

* If you purchase something that is advertised in crypto, the sale price
  would be determined as fair market value of the crypto at the time of the
  exchange.

* When you pay with crypto currencies, you can apply a FIFO, LIFO or
  Average cost method to determine the actual property used, same as it would
  apply to other property such as stock.

* At the end of each month open receivables and payables that are expressed
  in crypto currencies need to be revaluated at market value of the crypto.

## Open issues
* Is it possible to express an invoice in crypto currency? Seems possible,
  as long as you indicate what was the exchange rate used.

# Accounting examples
Assume crypto coins use symbol 'CC'.
At the time when you receive the CC the market value is 1 CC = $0.5.

Day 1: Invoice Cust/001 to customer (expressed in CC)
----------------------------------------------------
Market value of CC (day 1): 1 CC = $0.5
* Dr. 100 CC / $50 - Accounts receivable
* Cr. 100 CC / $50 - Revenue


Day 2: Receive payment for half invoice Cust/001 (in CC)
--------------------------------------------------------
Market value of CC (day 2): 1 CC = $0.8

Payment transaction:
* Dr. 50 CC / $40 - CC To Deposit (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $40 - Accounts Receivable

Actual receipt of the coins:
* Dr. 50 CC / $40 - CC Deposit (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $40 - CC To Deposit

Inventory of CC (day 1)
----------------------
day 1:
* 50 CC @$0,8/CC (total valuation of coins received / number of coins received)

Day 3: Receive remaining payment for invoice Cust/001 (in CC)
-------------------------------------------------------------
Market value of CC (day 3): 1 CC = $2

Payment transaction:
* Dr. 50 CC / $100 - CC To Deposit (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $100 - Accounts Receivable

Actual receipt of the coins:
* Dr. 50 CC / $100 - CC Deposit (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $100 - CC To Deposit

Full invoice reconciliation. Realization of the full transaction gain/loss:
* Dr. 0 CC / $90 - Accounts Receivable
* Cr. 0 CC / $90 - Crypto currency exchange gain

Inventory of CC
---------------
day 1:
* 50 CC @$0,98/CC
day 2:
* 50 CC @$2,00/CC





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
* Dr. 50 CC / $40 - CC To Inventory (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $40 - Accounts Receivable

Actual receipt of the coins:
* Dr. 50 CC / $40 - CC Inventory (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $40 - CC To Inventory

Inventory of CC (day 1)
----------------------
day 2:
* 50 CC @$0,8/CC (total valuation of coins received / number of coins received)

Day 3: Receive remaining payment for invoice Cust/001 (in CC)
-------------------------------------------------------------
Market value of CC (day 3): 1 CC = $2

Payment transaction:
* Dr. 50 CC / $100 - CC To Inventory (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $100 - Accounts Receivable

Actual receipt of the coins:
* Dr. 50 CC / $100 - CC Inventory (valued at market price at the time of receiving the coins)
* Cr. 50 CC / $100 - CC To Inventory

Full invoice reconciliation. Realization of the full transaction gain/loss:
* Dr. 0 CC / $90 - Accounts Receivable
* Cr. 0 CC / $90 - Crypto currency exchange gain

Inventory of CC (day 3)
-----------------------
day 2:
* 50 CC @$0,80/CC
day 3:
* 50 CC @$2,00/CC

Exchange Rate Profit/Loss
-------------------------
Profit resulting from exchange rate should be the difference
between the money in normal currency that we get after we get paid (
100.00 + 40.00) - what we were supposed to get paid if the exchange
rate had stayed the same (50.00)

Day 4: Invoice to supplier Supp/001 (expressed in CC)
-----------------------------------------------------
Market value of CC (day 4): 1 CC = $4
* Cr. 60 CC / $240 - Accounts Payable
* Dr. 60 CC / $240 - Expenses

Day 5: Pay half invoice of Supp/001 (in CC)
-------------------------------------------
Market value of CC (day 5): 1 CC = $6
Assume FIFO strategy for issuing crypto coins
* Dr. 30 CC / $180 - Accounts Payable
* Cr. 30 CC / $180 - CC To Inventory

* Cr. 30 CC / $24 - CC Inventory (30 CC @$0,80/CC)
* Dr. 30 CC / $24 - CC To Inventory


Inventory of CC (day 5)
-----------------------
day 1:
* 20 CC @$0,80/CC
day 2:
* 50 CC @$2,00/CC

Exchange Rate Profit/Loss
-------------------------
Profit resulting from exchange rate should be the difference
between the cost of the coins at original purchase price ($0,80/CC) and the
valuation at the time of paying them ($5,00/CC). That is, a profit of $126,00.

Day 6: Pay the other half invoice of Supp/001 (in CC)
----------------------------------------------------
Market value of CC (day 6): 1 CC = $5
Assume FIFO strategy for issuing crypto coins
* Dr. 30 CC / $150 - Accounts Payable
* Cr. 30 CC / $150 - CC To Inventory

* Cr. 30 CC / $36 - CC Inventory (20 CC @$0,80/CC + 10 CC @$2,00/CC)
* Dr. 30 CC / $36 - CC To Inventory

Inventory of CC (day 6)
-----------------------
day 1:
* 0 CC @$0,80/CC
day 2:
* 40 CC @$2,00/CC

Exchange Rate Profit/Loss
-------------------------
Profit resulting from exchange rate should be the difference
between the cost of the 20 CC @$0,80/CC and 10 @$2,00/CC, and the
valuation at the time of paying them ($5,00/CC).
That is, a profit of $114,00, added to the prior 126.

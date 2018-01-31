This project intends to implement cryptocurrency support for OCA.

# Accounting background
* Cryptocurrencies are considered property from a taxation standpoint. 
* This means that every time that you receive or send cryptocurrencies, you are entering into a taxable transaction, and will need to report on the gain/loss resulting from the receipt/issue of the cryptocurrency. 
* Cryptocurrencies are similar to currencies, and can be used in the exchange of goods and services between entities.
* When you receive cryptocurrencies (in exchange for goods delivered, service rendered or because you mined it), that translates into taxable income to the recipient. The valuation should be based on the market value of the cryptocurrency at the time of receipt, and it can be provided by a third party (e.g. the exchange platform) or needs to be identified by you somehow.
* You have to retain the cost of the crytptocurrency for as long as you keep it.
* When you pay out cryptocurrencies (in exchange for goods or services purchased, or if you exchanged fpr another crypto or normal currency) this constitutes again a taxable transaction. In that case the gain/loss is computed as the difference between the cost of the cryptocurrency that you pay with, and the value of what you receive back, valued in your operating normal currency.
* For example, if I buy 1 chair valued at $2 with 1 crypto that cost me $1, my gain is $1.
* So, every time that I pay with crypto, I need to value in terms of the reportable company currency what I receive back in exchange.
* I understand that if you purchase something that is advertised in normal currency, and pay with crypto, the sale price is determined as advertised. 
* If you purchase something that is advertised in crypto, the sale price would be determined as fair market value of the crypto at the time of the exchange.
* When you pay with crypto currencies, you can apply a FIFO, LIFO or Average cost method to determine the actual property used, same as it would apply to other property such as stock.
* At the end of each month open receivables and payables that are expressed in crypto currencies need to be revaluated at market value of the crypto.

## Open issues
* Is it possible to express an invoice in crypto currency? Seems possible, as long as you indicate what was the exchange rate used.

# Accounting examples
Assume crypto coins use symbol 'CC'.
At the time when you receive the CC the market value is 1 CC = $0.5. The transaction fee is $5.

Day 1: Invoice Cust/001 to customer (expressed in CC)
----------------------------------------------------
Market value of CC (day 1): 1 CC = $0.5
* Dr. 100 CC / $50 - Accounts receivable
* Cr. 100 CC / $50 - Revenue

Day 1: Invoice Cust/002 to customer (expressed in $)
----------------------------------------------------
* Dr. $100 - Accounts receivable
* Cr. $100 - Revenue

Day 2: Receive payment for half invoice Cust/001 (in CC)
--------------------------------------------------------
Market value of CC (day 2): 1 CC = $0.7
Transaction fee: $1
* Dr. 50 CC / $50 - Crypto Currency Deposit (valued at market price at the time of receiving the coins)
* Cr. $1 - Crypto Currency Deposit (transaction fee) - The cost of the transaction is added to the asset, same as it would occur with freight charge received. 
* Cr. 50 CC / $25 - Accounts Receivable
* Cr. $24 - Capital Gain (just the difference between what you received and Accounts Receivable)

Summary: At day 1 you recognized revenue worth the market valuation at that time, $50. But when you actually cash-in the money, you recognize an extra gain associated to the currency revaluation.

Day 2: Receive payment for half invoice Cust/002 (in CC)
--------------------------------------------------------
Market value of CC (day 2): 1 CC = $1
Transaction fee: $1,5
* Dr. 100 CC / $100 - Crypto Currency Deposit (valued at market price at the time of receiving the coins)
* Cr. $1,5 - Crypto Currency Deposit (transaction fee) - The cost of the transaction is added to the asset, same as it would occur with freight chy received. 
* Cr. $100 - Accounts Receivable
* Dr. $1,5 - Capital Loss (just the difference between what you received and Accounts Receivable)

Inventory of CC (day 1)
----------------------
day 1: 
* 50 CC @$0,98/CC (total valuation of coins received - transaction fee / number of coins received)
* 100 CC @$0,985/CC

Day 3: Receive remaining payment for invoice Cust/001 (in CC)
-------------------------------------------------------------
Market value of CC (day 3): 1 CC = $2
Transaction fee: $2
* Dr. 50 CC / $100 - Crypto Currency Deposit (valued at market price at the time of receiving the coins)
* Cr. $2 - Crypto Currency Deposit (transaction fee)
* Cr. 50 CC / $25 - Accounts Receivable
* Cr. $49 - Capital Gain (just the difference between what you received and Accounts Receivable)

Inventory of CC
---------------
day 1: 
* 50 CC @$0,98/CC
* 100 CC @$0,985/CC
day 2: 
* 50 CC @$1,96/CC

Day 4: Invoice to supplier Supp/001 (expressed in CC)
-----------------------------------------------------
Market value of CC (day 4): 1 CC = $3
* Cr. 400 CC / $1200 - Accounts Payable
* Dr. 400 CC / $1200 - Expenses

Day 5: Pay half invoice of Supp/001 (in CC)
-------------------------------------------
Market value of CC (day 5): 1 CC = $4
Assume FIFO strategy for issuing crypto coins
Transaction fee: $3
* Dr. 175 CC / $525 - Accounts Payable
* Dr. $3 - Expense (transaction fee)
* Cr. 175 CC / $196,50 - Crypto Currency Deposit (Issuing 50 CC @$0,98/CC + 100 CC @$0,985/CC + 25 CC @$1,96/CC)
* Cr. 1,53 CC / $3 - Crypto Currency Deposit (Issuing 1,53 CC @$1,96/CC) - pay the fees
* Cr. $328,50 - Capital Gain (difference between what you issued and Accounts Payable)

Inventory of CC
---------------
day 1: 
* 0 CC @$0,98/CC
* 0 CC @$0,985/CC
day 2: 
* 23,47 CC @$1,96/CC

Day 6 (end of month): Revaluation of receivables and payables
-------------------------------------------------------------
Market value of CC (day 6): 1 CC = $1,5
At the end of each month a revaluation needs to occur with open receivables and payables associated to invoices in crypto currencies.
Starting Receivables: 0CC / $0
Starting Payables: 75CC / $275
Dr. $225 Accounts Payable (150 CC*($3/CC - $1,5/CC))
Cr. $225 Gain from exchange rate

# Implications in OCA

* You need to create cryptocurrencies as a normal currency (`res.currency`)
* You will need to retain the cost of crypto currencies while you hold them. As a consequence, seems logical to use an approach similar to stock.move or stock.quant to retain or get to know the cost of the crypto currencies. 
* To analyze the differences in costing methods for stock in v11/v10. Perhaps we can apply the same procedure.
* In crypto currencies the triggering of the transactionable event should occur when you send or receive money. 
* It seems logical that we should link the movements of crypto currencies with the `account.move.line`, associated to the asset account move line that represents the deposits of this crypto.

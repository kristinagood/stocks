COMMISSION_RATE = float(input('please enter commission rate:'))
NUM_SHARES = float(input('please enter number of shares:'))
PURCHASE_PRICE = float(input('please enter purchase price:'))
SELLING_PRICE = float(input('please enter selling price:'))
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
SELLING_PRICE = (NUM_SHARES * SELLING_PRICE)
PURCHASE_PRICE = (NUM_SHARES * PURCHASE_PRICE)
print(SELLING_PRICE)
print(sellingCommission)
print(purchaseCommission)
print(PURCHASE_PRICE)

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
print(f'Amount paid for stock: ${SELLING_PRICE}')
print(f'Commission paid on the purchase: ${sellingCommission}')
print(f'Commission paid on the sale: ${purchaseCommission}')
print(f'Amount the stock sold for: ${PURCHASE_PRICE}')
print(f'Total commission paid: ${totalPaid}')
print(f'Profit (or loss if negative): ${profitOrLoss}')
if profitOrLoss < 0:
    print(f'your loss is: ${profitOrLoss}')
if profitOrLoss > 0:
    print(f'your profit is: ${profitOrLoss}')
if profitOrLoss == 0:
    print(f'there is no gain or loss: ${profitOrLoss}')
    

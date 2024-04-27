Amount = int(input("Enter the transaction amount: "))

Trx_Fee = 0.406 * Amount
Tax = 0.10 * Amount

Total = Amount + Tax + Trx_Fee

print(Trx_Fee)
print(Tax)
print(Total)
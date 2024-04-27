set = True
while set == True:
    Amount = float(input("Enter the transaction amount: "))

    Trx_Fee = 0.0406 * Amount
    Tax = 0.10 * Amount

    Total = Amount + Tax + Trx_Fee

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Transaction fee will be: ',Trx_Fee)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Tax will be: ',Tax)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Total amount will be: ',Total)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('*********************************')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    ans = input("Do you want to do another calculation? y/n: ")
    if ans == 'y':
        set = True
    else:
        set = False


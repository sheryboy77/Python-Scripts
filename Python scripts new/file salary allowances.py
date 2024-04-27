def allowance(salary):
    HouseRent = 61/100 * salary
    Medical = 48/100 * salary
    Total = salary + HouseRent + Medical
    arr = [0,0,0]
    arr[0] = Total
    arr[1] = HouseRent
    arr[2] = Medical
    return arr

def taxes(SBTax):
    if SBTax >= 200000:
        tax = 2.1
    elif SBTax < 200000 and SBTax >= 150000:
        tax = 1.6
    else:
        tax = 1

    Tax = tax/100 * SBTax
    SATax = SBTax - Tax
    arrr = [0,0]
    arrr[0] = SATax
    arrr[1] = Tax
    return arrr

SFile = open("Salary allowances and taxes.txt", "w")

for a in range(5):
    
    Name = input('Enter employee name: ')
    Salary = int(input('Enter employee salary: '))

    allowances = allowance(Salary)
    Taxes = taxes(allowances[0])

    TotalSalary = allowances[0]
    HouseRent = allowances[1]
    Medical = allowances[2]
    AfterTax = Taxes[0]
    TotalTax = Taxes[1]

#    SFile.write('Employee name: ' + Name +
#                '\nEmployee initial salary: ' + str(Salary) +
#                '\nEmployee salary after allowances: ' + str(TotalSalary) +
#                '\nEmployee medical: ' + str(Medical) +
#                '\nEmployee salary after tax: ' + str(AfterTax) +
#                '\nTotal tax deducted: ' + str(TotalTax) + '\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=' + '\n')

    SFile.write(f'Employee name: {Name}' +
                f'\nEmployee initial salary: {Salary}' +
                f'\nEmployee salary after allowances: {TotalSalary}' +
                f'\nEmployee medical: {Medical}' +
                f'\nEmployee salary after tax: {AfterTax}' +
                f'\nTotal tax deducted: {TotalTax}' + '\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=' + '\n')

SFile.close()





























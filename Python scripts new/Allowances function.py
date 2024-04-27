def allowance(salary):
    HouseRent = 48/100 * salary
    Medical = 39/100 * salary
    Conveince = 22/100 * salary
    return ('Your total salary is: ',salary + HouseRent + Medical + Conveince)

ans = 'y'
while ans == 'y':
    Salary = int(input("Enter the salary: "))
    print (allowance(Salary))
    ans = input('Do you want to calculate another salary? y|n: ')

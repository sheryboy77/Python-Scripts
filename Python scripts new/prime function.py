def prime(number):
    if number == 1:
        return('It is not a prime number')
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return('It is not a prime number')
                break
        else:
            return('It is a prime number')

ans = 'y'
while ans == 'y':
    num = int(input("Enter the number: "))
    print(prime(num))
    ans = input('Do you want to enter another number? y|n : ')

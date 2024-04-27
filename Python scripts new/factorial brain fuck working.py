def factorial(num):
    while num < 0:
        num = int(input('Enter positive number: '))
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input('Enter the number: '))
print(factorial(num))

def even_odd(num):
    if num % 2 == 0:
        return 'number is even'
    else:
        return 'number is odd'

ans = "y"
while ans == "y":
    number = int(input('enter the number: '))
    print(even_odd(number))

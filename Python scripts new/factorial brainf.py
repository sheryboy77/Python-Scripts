def fact(num,num1):
    if num1 > 1:
        num1 = num1 - 1
        num = num * num1
        num = fact(num,num1)
    return num

number = int(input('Enter the number: '))
print(fact(number,number))

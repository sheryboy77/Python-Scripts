def calculator(n1,n2):
    op = input("what do you want to do? +|-|*|/ : ")
    if op == '+':
        return(n1+n2)
    elif op == '-':
        return(n1-n2)
    elif op == '*':
        return(n1*n2)
    elif op == '/':
        return(n1/n2)

ans = 'y'
while ans == 'y':
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    print(calculator(number1,number2))
    ans = input('do you want do do another calculation? y|n : ')
    

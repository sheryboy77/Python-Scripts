ans = "y"
while ans == "y":
    num = int(input("Enter the number: "))
    if num%2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

    ans = (input("do you want to input another number? y|n: "))
    

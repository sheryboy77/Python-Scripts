number = int(input("Enter the number: "))
while number < 0:
    number = int(input("number is negative, input another number: "))

num = number

while num > 1:
    num = num - 1
    number = number * num

if number == 0:
    number = 1

print("Factorial are:", number)

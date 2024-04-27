msg = input("Enter your message: ")
count = 1

print("Using FOR loop")

for i in range(1, 31):
    print(i, msg)

print("Using WHILE loop")

while count < 31:
    print(count, msg)
    count = count+1

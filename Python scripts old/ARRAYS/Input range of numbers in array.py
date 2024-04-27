n = int(input("How many element to store in the list: "))

print("Enter", n, "elements for the list: ")
list = []

for i in range(n):
    val = int(input())
    list.append(val)

print("The list is: ")
for i in range(n):
    print(list[i])
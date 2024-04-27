ResultSheet = []
Index = 1
Found_Flag = False

for i in range(1, 11):
    ResultSheet.insert(i, int(input(f"Enter marks of student {i}: ")))

num = int(input("Enter value you want to search: "))

for i in range(1, 11):
    if num == ResultSheet[i]:
        index = i
        break

print(f"Number found at index number: {index}")
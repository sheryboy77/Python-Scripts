ResultSheet = [10, 23, 335, 34, 4345, 5456, 27, 238, 549, 3410]
Index = 1
Found_Flag = False

num = int(input("Enter value you want to search: "))

Length = len(ResultSheet)

for i in range(Length):
    if num == ResultSheet[i]:
        index = i
        break

print(f"Number found at index number: {index}")


age = [23,52,17,25,18,15]

# Finding the desired number in array
flag = False
num = int(input("Enter the number to find: "))
for a in range(0,6):
    if age[a] == num:
        flag = True
if flag == True:
    print("Found")
else:
    print("Not Found")

# Finding the min and max values in the arraya
Max = 0
Min = 1000
for a in range(0,6):
    if age[a] > Max:
        Max = age[a]
    if age[a] < Min:
        Min = age[a]
print('minimum value is ', Min,', maximum value is', Max)

# Finding the average of the values in the array
Avg = 0
Sum = 0
for a in range(0,6):
    Sum = Sum + age[a]
Avg = Sum/6
print('Average is ',Avg)

# Reverse the order of the array
rev_age = []
for b in range(5,-1,-1):
    rev_age.append(age[b])
print(rev_age)

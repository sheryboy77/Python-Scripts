data = [20,12,24,435,23,34,23,]
count = 0

ini_limit = int(input("Enter the initial limit: "))
final_limit = int(input("Enter the final limit: "))
find = int(input("Enter the unit number to find: "))

for a in range(ini_limit, final_limit):
    if a%10 == find:
        count = count + 1
        data.append(a)

print("all numbers containing",find,"at unit place =",count)
print("number of",find,"'s at unit place",data)

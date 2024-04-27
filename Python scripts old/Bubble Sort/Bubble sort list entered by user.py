Mylist = []
Size = int(input("Enter the size of list: "))
index = Size-1
swap = False

for i in range(Size):
    Mylist.append(int(input(f"Enter number {i}: ")))


for count in range(Size):
    for x in range(index):
        if Mylist[x] > Mylist[x+1]:
            Temp = Mylist[x]
            Mylist[x] = Mylist[x+1]
            Mylist[x+1] = Temp
            swap = True
    index = index-1

print(Mylist)

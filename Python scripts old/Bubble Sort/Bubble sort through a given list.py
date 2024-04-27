Mylist = [23, 1, 20, 15, 100, 8]
Size = 6
index = Size-1
swap = False


for count in range(Size):
    for x in range(index):
        if Mylist[x] > Mylist[x+1]:
            Temp = Mylist[x]
            Mylist[x] = Mylist[x+1]
            Mylist[x+1] = Temp
            swap = True
    index = index-1

print(Mylist)
def BinaryS(array,data):
    sp = 0
    ep = len(array)-1
    flag = False
    while sp <= ep and not flag:
        mid = (sp+ep)//2
        if data == array[mid]:
            flag = True
        elif number > array[mid]:
            sp = mid+1
        else:
            ep = mid - 1
    if flag == True:
        return("Number Found")
    else:
        return('Not Found')

age = [2,8,11,17,32,78]
num = int(input('Enter the number to find: ' ))
print(BinaryS(num,age))

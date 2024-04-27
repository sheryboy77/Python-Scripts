def LinearS(array,data):
    found = False
    for a in range(len(array)):
        if array[a] == data:
            found = True
    if found == True:
        return('Found')
    else:
       return('Not Found')

age = [7,9,12,14,16,17,20,26,29,34,38,44]
ans = 'y'
while ans == 'y':
    num = int(input('enter the number to find: '))
    print(LinearS(age,num))
    ans = input('Do you want to search for another number? y|n: ')

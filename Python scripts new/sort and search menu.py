def LinearS(array,data):
    found = False
    for a in range(len(array)):
        if array[a] == data:
            found = True
    if found == True:
        return('Found')
    else:
        return('Not Found')


def BinaryS(array,data):
    sp = 0
    ep = len(array)-1
    flag = False
    while sp <= ep and not flag:
        mid = (sp+ep)//2
        if data == array[mid]:
            flag = True
        elif data > array[mid]:
            sp = mid+1
        else:
            ep = mid - 1
    if flag == True:
        return('Found')
    else:
        return('Not Found')


def Bubble(array):
    for outer in range(0,len(array)):
        for inner in range(0,len(array)-1):
            if array[inner] > array[inner+1]:
                temp = array[inner]
                array[inner] = array[inner+1]
                array[inner+1] = temp
    return(array)


def Insertion(array):
    for outer in range(0,len(array)):
        for inner in range(outer-1,-1,-1):
            if array[inner] > array[inner+1]:
                temp = array[inner]
                array[inner] = array[inner+1]
                array[inner+1] = temp
    return(array)


def menu(List):
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('         PLEASE SELECT ONE OF THE OPTIONS BELOW          ')
    print()
    print('  (1)              Linear Search                    (1)  ')
    print()
    print('  (2)              Binary Search                    (2)  ')
    print()
    print('  (3)               Bubble Sort                     (3)  ')
    print()
    print('  (4)              Insertion Sort                   (4)  ')
    print()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print()
    choice = int(input('Your Selection: '))
    while choice > 4 or choice < 1:
        choice = int(input('Please enter a number in range: '))
    if choice == 1:
        number = int(input('Enter the number to find: '))
        return(LinearS(List,number))
    elif choice == 2:
        number = int(input('Enter the number to find: '))
        return(BinaryS(List,number))
    elif choice == 3:
        return(Bubble(List))
        List = Bubble(List)
    elif choice == 4:
        return(Insertion(List))
        List = Insertion(List)



#size = int(input('Enter the size of your list: '))
#for a in range(size):
#    List.append(int(input('Enter number at position {a}: ')))
    

ages = [5,2,9,11,8,3,-8,1,23,72,21,69,43,-21,-75,24,64,78,47]

ans = 'y'
while ans == 'y':
    print(menu(ages))
    ans = input('Do you want to do something else or exit? y|n : ')
    























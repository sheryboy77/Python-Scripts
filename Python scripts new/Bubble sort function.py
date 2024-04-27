def bubble(array):
    for outer in range(0,len(array)):
        for inner in range(0,len(array)-1):
            if array[inner] > array[inner+1]:
                temp = array[inner]
                array[inner] = array[inner+1]
                array[inner+1] = temp
    return(array)

#      0 1 2 3  4 5 6  7
age = [5,2,9,11,8,3,-8,1]

print(bubble(age))

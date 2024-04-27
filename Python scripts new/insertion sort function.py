def insertion(array):
    for outer in range(0,len(array)):
        for inner in range(outer-1,-1,-1):
            if array[inner] > array[inner+1]:
                temp = array[inner]
                array[inner] = array[inner+1]
                array[inner+1] = temp
    return(array)

age = [5,3,9,7,19,1,2,4,6,8]
print(insertion(age))

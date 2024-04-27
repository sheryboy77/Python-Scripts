def insertion(array):
    for outer in range(0,len(array)-1):
        while array[outer+1] < array[outer] and outer >= 0:
            temp = array[outer+1]
            array[outer+1] = array[outer]
            array[outer] = temp
            outer = outer-1
    return(array)

age = [5,3,9,7,19,1]
print(insertion(age))

array =[5,3,9,7,19,1]

for outer in range(6, 6):
    print('outer = ',outer)
    for inner in range(outer - 1, -1, -1):
        print('inner = ',inner)
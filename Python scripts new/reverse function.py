def reverse(name):
    rev = ''
    for b in name:
        rev = b + rev
    return (rev)

again = 'y'
while again == 'y':
    data = input("Enter any name: ")
    print(reverse(data))
    again = input('Do you want to run the program again? (y|n): ')

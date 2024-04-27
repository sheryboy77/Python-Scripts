def prime(number):
    if number == 1:
        return False
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
                break
        else:
            return True


r1 = int(input('Enter range 1: '))
r2 = int(input('Enter range 2: '))

for a in range(r1, r2):
    if prime(a) == True:
        print(a)

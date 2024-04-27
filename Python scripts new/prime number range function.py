def Rprime(rangeL,rangeU):
    PrimeNum = []
    for a in range(rangeL,rangeU+1):
        if a > 2:
            for i in range(2, a):
                if a % i == 0:
                    break
            else:
                PrimeNum.append(a)
    return(PrimeNum)

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
        return("Found")
    else:
        return('Not Found')
    
r1 = int(input('Enter the lower limit: '))
r2 = int(input('Enter the upper limit: '))
Fnum = int(input('Enter the prime number you want to find in this range: '))

nums = Rprime(r1,r2)

Max = 0
Min = 999999
for l in range(len(nums)):
    if nums[l] > Max:
        Max = nums[l]
    if nums[l] < Min:
        Min = nums[l]


Sum = 0
for i in range(len(nums)):
    Sum = Sum + nums[i]

avg = Sum/len(nums)

print(f'\nThe prime numbers are: {nums}')
print(f'\nSum = {Sum}')
print(f'Average = {avg}')
print(f'Total numbers are = {len(nums)}')
print(f'Number {Fnum} ' + BinaryS(nums,Fnum))
print(f'The largest prime number is: {Max}')
print(f'The smallest prime numeber is: {Min}')

PrimeFile = open('Prime numbers.txt', 'w')
PrimeFile.write(str(nums) +
                f'\nSum = {Sum}' +
                f'\nAverage = {avg}' +
                f'\nTotal numbers are = {len(nums)}' +
                f'The largest prime number is: {Max}' +
                f'The smallest prime numeber is: {Min}')
PrimeFile.close()


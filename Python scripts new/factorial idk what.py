def fact(num,ans):
    Sum = 1
    first = True
    if first == True:
        first = False
        return(Sum)
    if first == False:
        ans = ans * num
    return(ans)



number = int(input('Enter the number : '))
ans = fact(number,number)
for a in range(number,2,-1):
    number = number - 1
    answer = 15
    answer = fact(number,answer)
print(answer)

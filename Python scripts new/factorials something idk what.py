def facts(num,add):
    for a in range(num,0,-1):
        num = num - 1
        add = add * num
        num = facts(num,add)
    return(add)



number = 5
print(facts(number,number))

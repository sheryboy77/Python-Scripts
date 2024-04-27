stack = []

BP = 0
TP = -1
SF = 4

def push(num):
    global BP,TP,SF
    if TP < SF:
        TP = TP + 1
        stack.insert(TP,num)
    else:
        print('stack is full')

def pop():
    global BP,TP,SF
    if TP = BP - 1:
        print('stack is empty')
    else:
        print(stack[TP])
        TP = TP - 1


push(212)
push(12)
push(35)
push(65)
push(82)
print(stack)
push(23)
pop()
push(23)
print(stack)

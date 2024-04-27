def large(x, y, z):
    if x > y:
        if y > z:
            return x
        else:
            if z > x:
                return z
            else:
                return x
    else:
        if y > z:
            return y
        else:
            return z


print("Enter any Three numbers: ")

a = int(input())
b = int(input())
c = int(input())

print("The largest number is ", large(a, b, c))

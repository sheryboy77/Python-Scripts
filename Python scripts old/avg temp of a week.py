Ttemp = 0
MinTemp = 100
MaxTemp = 0

for x in range(1, 8):
    temp = int(input(f"Enter the temperature for day {x}: "))

    if temp > MaxTemp:
        MaxTemp = temp
    if temp < MinTemp:
        MinTemp = temp

    Ttemp = Ttemp + temp

Avg = Ttemp/7

print("The average temp of the week is ", Avg)
print("The maximum temperature of the week is ", MaxTemp)
print("The minimum temperature of the week is ", MinTemp)

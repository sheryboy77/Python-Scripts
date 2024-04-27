Names = []
Weight = []
Weight2 = []
DWeight = []

for i in range(3):

    Names.append(str(input("Enter the name of the student: ")))

    wght = int(input("Enter the weight of the student: "))

    while wght<25 or wght>150:
        print("Weight is not in the limit of 25 to 150. Please reenter the weight")
        wght = int(input("Enter the weight of the student: "))
    
    Weight.append(wght)


for i in range(3):
    print("Student",Names[i],"has weight of",Weight[i],"kg")



for i in range(3):
    Weight2.append(int(input("Enter the final weight of the student: ")))

for i in range(3):

    DWeight.append(Weight2[i]-Weight[i])

    if DWeight[i] > 2.5:
        print(Names[i],"'s weight has increasd by",DWeight[i])
    elif DWeight[i] <-2.5:
        print(Names[i],"'s weight has decreased by",DWeight[i])

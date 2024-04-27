names = []
salary = []

for i in range(1, 6):
    names.append(input(f"Enter the name of employee {i}: "))
    salary.append(int(input(f"Enter the salary of employee {i}: ")))

for i in range(5):
    print("Employee", names[i], "got", (salary[i]+5000), "after bonus of 5000")

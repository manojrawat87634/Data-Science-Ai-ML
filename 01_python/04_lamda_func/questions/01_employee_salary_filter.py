employees = [("Rahul", 45000), ("Anita", 60000), ("Karan", 52000), ("Neha", 48000)]

high_salary = list(filter(lambda x: x[1] > 50000, employees))
print(high_salary)
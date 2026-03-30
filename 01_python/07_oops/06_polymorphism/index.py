class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Writing code")

class Designer(Employee):
    def work(self):
        print("Designing UI/UX")

class Manager(Employee):
    def work(self):
        print("Managing team")

employees = [Developer(), Designer(), Manager()]

for emp in employees:
    emp.work()
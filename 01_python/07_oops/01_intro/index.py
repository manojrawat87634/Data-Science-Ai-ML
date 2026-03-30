def add(a, b):
    return a + b

print(add(2, 3))


class Calculator:
    def add(self, a, b):
        return a + b


calc = Calculator()
print(calc.add(5, 7))


class Student:
    def introduce(self):
        print("Hi, I'm learning Python.")


student1 = Student()
student1.introduce()
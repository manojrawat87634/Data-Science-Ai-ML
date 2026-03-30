class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def save(self):
        with open("students.txt", "a") as f:
            f.write(f"{self.name},{self.marks}\n")

    @staticmethod
    def view():
        with open("students.txt", "r") as f:
            for line in f:
                name, marks = line.strip().split(",")
                print(name, marks)

s1 = Student("Rahul", 85)
s2 = Student("Anita", 90)

s1.save()
s2.save()

Student.view()
class Student:
    def __init__(self, name, roll_no, student_class, total_fees):
        self.name = name
        self.roll_no = roll_no
        self.student_class = student_class
        self.total_fees = total_fees
        self.fees_paid = 0
        self.marks = {}
        self.attendance = 0

    def show_info(self):
        print("\nStudent Details")
        print("----------------------")
        print(f"Name        : {self.name}")
        print(f"Roll No     : {self.roll_no}")
        print(f"Class       : {self.student_class}")
        print(f"Total Fees  : ₹{self.total_fees}")
        print(f"Fees Paid   : ₹{self.fees_paid}")
        print(f"Fees Due    : ₹{self.total_fees - self.fees_paid}")
        print(f"Attendance  : {self.attendance} days")
        print(f"Marks       : {self.marks}")

    def pay_fees(self, amount):
        if amount <= 0:
            print("Invalid fee amount!")
        elif self.fees_paid + amount > self.total_fees:
            print("Amount exceeds total fees!")
        else:
            self.fees_paid += amount
            print(f"₹{amount} fee paid successfully.")

    def check_fee_status(self):
        due = self.total_fees - self.fees_paid
        print(f"Fees Paid : ₹{self.fees_paid}")
        print(f"Fees Due  : ₹{due}")

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
        print(f"Marks added for {subject}.")

    def show_marks(self):
        print("\nMarks")
        print("-------------")
        for subject, marks in self.marks.items():
            print(f"{subject}: {marks}")

    def update_attendance(self, days):
        self.attendance += days
        print(f"Attendance updated by {days} days.")

s1 = Student("Rahul", 101, "10th", 50000)
s2 = Student("Priya", 102, "9th", 45000)


s1.show_info()

s1.pay_fees(20000)
s1.add_marks("Math", 95)
s1.add_marks("Science", 90)
s1.update_attendance(25)

s1.check_fee_status()
s1.show_marks()
s1.show_info()


s2.show_info()

s2.pay_fees(15000)
s2.add_marks("English", 88)
s2.add_marks("Computer", 92)
s2.update_attendance(22)

s2.check_fee_status()
s2.show_marks()
s2.show_info()
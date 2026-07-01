class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance

    def show_info(self):
        print("\nAccount Details")
        print("----------------")
        print(f"Name   : {self.name}")
        print(f"Email  : {self.email}")
        print(f"Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Creating users
u1 = User("abc", "abc@gmail.com", 5000)
u2 = User("xyz", "xyz@gmail.com", 3000)

# User 1 Operations
u1.show_info()
u1.deposit(2000)
u1.withdraw(1500)
u1.check_balance()

# User 2 Operations
u2.show_info()
u2.deposit(1000)
u2.withdraw(5000)
u2.check_balance()
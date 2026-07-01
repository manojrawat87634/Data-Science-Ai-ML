class Hotel:
    def __init__(self, customer, room_no, room_type):
        self.customer = customer
        self.room_no = room_no
        self.room_type = room_type
        self.bill = 0

    def show_info(self):
        print("\nCustomer Details")
        print("----------------")
        print("Customer :", self.customer)
        print("Room No  :", self.room_no)
        print("Room Type:", self.room_type)
        print("Bill     : ₹", self.bill)

    def order_food(self, amount):
        self.bill += amount
        print("Food ordered successfully.")

    def add_room_charge(self, amount):
        self.bill += amount
        print("Room charge added.")

    def checkout(self):
        print(f"Total Bill: ₹{self.bill}")
        print("Thank you for staying!")


h1 = Hotel("Rahul", 101, "Deluxe")

h1.show_info()
h1.add_room_charge(3000)
h1.order_food(800)
h1.checkout()
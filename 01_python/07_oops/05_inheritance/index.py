class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(self.brand, self.speed)

class Car(Vehicle):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def display(self):
        print(self.brand, self.speed, self.seats)

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

    def display(self):
        print(self.brand, self.speed, self.type)

c = Car("Toyota", 180, 5)
b = Bike("Yamaha", 120, "Sports")

c.display()
b.display()
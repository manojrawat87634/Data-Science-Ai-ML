class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __len__(self):
        return len(self.name)

p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)

print(p1)
print(p1 + p2)
print(len(p1))
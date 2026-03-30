products = [("Laptop", 50000), ("Phone", 20000), ("Tablet", 30000), ("Headphones", 5000)]

products_sorted = sorted(products, key=lambda x: x[1])
print(products_sorted)
# def order_total_calculation(order):
#     total = 0
#     for item in order:
#         total += item["price"] * item["quantity"]
#     return total

# # Example usage
# order = [
#     {"name": "item1", "price": 100, "quantity": 2},
#     {"name": "item2", "price": 50, "quantity": 3}
# ]

# print(order_total_calculation(order))



order = [
    {"name": "item1", "price": 100, "quantity": 2},
    {"name": "item2", "price": 50, "quantity": 3}
]

total = sum(map(lambda item: item["price"] * item["quantity"], order))

print(total)
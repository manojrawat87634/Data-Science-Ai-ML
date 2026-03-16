# import numpy as np

# A = np.array([[1,2],
#               [3,4]])

# B = np.array([[5,6],
#               [7,8]])

# result = np.dot(A,B)

# print(result)   


import numpy as np

# product features for different products
# columns: [rating, price_score, popularity, delivery_speed, return_rate, brand_score, discount_score]

products = np.array([
    [4.7, 7, 900, 8, 2, 9, 6],   # product1
    [4.2, 9, 700, 7, 3, 7, 8],   # product2
    [4.8, 6, 1200, 9, 1, 8, 5],  # product3
    [4.1, 8, 500, 6, 4, 6, 7]    # product4
])

# user preference vector
# how much the user cares about each factor
# [rating, price, popularity, delivery, return, brand, discount]

user_preferences = np.array([
    0.30,   # rating importance
    0.20,   # price importance
    0.15,   # popularity importance
    0.10,   # delivery importance
    0.05,   # return rate importance
    0.10,   # brand importance
    0.10    # discount importance
])

# recommendation score
recommendation_scores = products @ user_preferences

print(recommendation_scores)

# best recommended product
best_product = np.argmax(recommendation_scores)

print("Best product index:", best_product)
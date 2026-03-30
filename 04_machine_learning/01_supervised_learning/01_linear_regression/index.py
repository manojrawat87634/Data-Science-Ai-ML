import numpy as np
from sklearn.linear_model import LinearRegression

# Features: [size, toppings, cheese_quality]
X = np.array([
    [10, 2, 3],
    [12, 3, 4],
    [8,  1, 2],
    [15, 4, 5]
])

# Prices
y = np.array([200, 300, 150, 400])

model = LinearRegression()
model.fit(X, y)

# Predict new pizza
# size=11, toppings=2, cheese=3
prediction = model.predict([[11, 2, 3]])

print("Price:", prediction)
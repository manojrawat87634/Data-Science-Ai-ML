from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# X = [Size, Toppings, ExtraCheese]
X = np.array([
    [6, 1, 0],
    [8, 2, 0],
    [10, 2, 1],
    [12, 3, 1],
    [14, 4, 1]
])

y = np.array([100, 150, 200, 250, 300]) 

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)
print("Prediction", prediction) 
print("coef", model.coef_) # Coef the price increase or decrease of the per 1 unit of the size topping and extraCheese 
print("Intercept", model.intercept_) # Intercept is the Pizza price when size, topping and extracheese is 0 
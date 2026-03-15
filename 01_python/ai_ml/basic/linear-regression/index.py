from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split

x = np.array([[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]])
y = np.array([150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000])


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train, y_train)

predictions = model.predict(x_test)

print("Predictions ", predictions)
print("Slove (w)", model.coef_)
print("Intercept", model.intercept_)
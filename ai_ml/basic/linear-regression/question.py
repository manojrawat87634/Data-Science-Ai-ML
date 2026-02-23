import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# [Years of experience, Number of skills, Education level (0 = Basic, 1 = Graduate, 2 = Masters)]
X = np.array([
    [1, 3, 0],
    [2, 4, 0],
    [3, 5, 1],
    [4, 6, 1],
    [5, 7, 2],
    [6, 8, 2],
    [7, 9, 2],
    [8, 10, 2],
    [9, 12, 2],
    [10, 14, 2]
])

# Salary in ₹ (in thousands)
y = np.array([15, 20, 30, 35, 45, 50, 60, 65, 75, 80])

 
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)
print("Prediction", prediction)
print("Slope", model.coef_)
print("Intercept", model.intercept_)


new_candidate = np.array([[6, 20, 1]])
predicted_salary = model.predict(new_candidate)
print("Predicted Salary (in thousands): ₹", predicted_salary[0])
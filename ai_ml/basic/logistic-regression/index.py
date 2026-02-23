import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#  Hours Study, Attendance, Pratical Marks
X = np.array([
    [1, 60, 10],
    [2, 70, 20],
    [3, 65, 15],
    [4, 80, 35],
    [5, 85, 40],
    [6, 90, 50],
    [7, 95, 55],
    [8, 92, 60],
    [9, 96, 70],
    [10, 98, 80]
])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print("Prediction", predictions)
print("Actual", y_test)
print("Accuraccy", accuracy_score(y_test, predictions))

new_student = np.array([[14, 98, 10]])
result = model.predict(new_student)
print("Will Pass?" , "Yes" if result[0] == 1 else "No")
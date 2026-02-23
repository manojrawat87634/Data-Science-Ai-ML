from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


X = [
    [750, 60000, 0, 1],
    [680, 35000, 0, 1],
    [620, 30000, 1, 1],
    [590, 20000, 0, 0],
    [720, 45000, 0, 1],
    [610, 15000, 1, 0]
]

y = [1, 1, 0, 0, 1, 0]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

print(x_test)
prediction = model.predict(x_test)
print("Prediction", prediction)
print("Real Data", y_test)
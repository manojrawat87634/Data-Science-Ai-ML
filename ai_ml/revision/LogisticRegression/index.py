import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

ages = np.random.randint(18, 65, 1000)
salaries = np.random.randint(20000, 150000, 1000)
seen_ads = np.random.randint(0, 2, 1000)
purchased = (salaries > 70000).astype(int)  # simple rule
data = {
    'Age': ages,
    'Salary':salaries,
    'Seen_Ad': seen_ads,
    'Purchased': purchased
}

df = pd.DataFrame(data)
X = df.drop("Purchased", axis=1)
y = df['Purchased']

x_train, x_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(x_train, y_train)
# print("Predicted Data")
# print(model.predict(x_test))
# print("Real Data")
# print(y_test)


new_user = pd.DataFrame({'Age' : [30], 'Salary' : [45000], 'Seen_Ad' : [1]})
# print(new_user)
new_prediction = model.predict(new_user)

print(new_prediction)
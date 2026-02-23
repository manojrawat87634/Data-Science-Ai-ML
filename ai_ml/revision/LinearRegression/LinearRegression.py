from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

data = {
    'Size' : [8, 10, 12, 14, 16, 8, 10, 12, 14, 16, 8, 10, 12, 14, 16],
    'Cheese' : [100, 150, 180, 200, 220, 120, 140, 160, 190, 230, 110, 135, 170, 210, 240],
    'Toppings' : [2, 3, 4, 5, 6, 2, 1, 3, 4, 5, 1, 2, 3, 5, 6],
    'Crust' : ['Thin', 'Thick', 'Stuffed', 'Thin', 'Thick', 'Stuffed', 'Thin', 'Thick', 'Stuffed', 'Thin',
              'Thick', 'Stuffed', 'Thin', 'Thick', 'Stuffed'],
    'Vegetarian' : ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes'],
    'Price' : [6.99, 9.49, 13.99, 14.49, 16.99, 8.49, 7.99, 12.49, 14.99, 15.99, 7.49, 9.99, 11.99, 15.49, 17.49]
}

df = pd.DataFrame(data)
df.to_excel('my.xlsx', index=False)
# print(df)
df['Vegetarian'] = df['Vegetarian'].map({'Yes': 1, 'No': 0})
# One-hot encode 'Crust'
df = pd.get_dummies(df, columns=['Crust'])

X = df.drop('Price', axis=1) # What is drop 
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2,  random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)
print(prediction)

print("Coeficient", model.coef_)
print("Intercept", model.intercept_)

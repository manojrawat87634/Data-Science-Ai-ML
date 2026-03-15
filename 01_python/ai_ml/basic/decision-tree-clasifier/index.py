from sklearn.tree import DecisionTreeClassifier, plot_tree

# Credit Score, Salary, previous_loan_filled, 
X = [
    [750, 60000, 0, 1],
    [680, 35000, 0, 1],
    [620, 30000, 1, 1],
    [590, 20000, 0, 0],
    [720, 45000, 0, 1],
    [610, 15000, 1, 0]
]

y = [1, 1, 0, 0, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)
new_applicant = [[700, 40000, 0, 1]]
prediction = model.predict(new_applicant)
print(prediction)

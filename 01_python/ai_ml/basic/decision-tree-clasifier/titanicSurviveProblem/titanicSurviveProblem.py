import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Create a mini Titanic-like dataset
data = pd.DataFrame({
    'pclass' : [3, 1, 3, 1, 2, 3, 1, 3],
    'gender' : ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female'],
    'age' : [22, 38, 26, 35, 28, 2, 54, 19],
    'survived' : [0, 1, 1, 1, 0, 0, 0, 1]
})

# Step 2: Encode categorical data
# print(data['gender'])
data['gender'] = data['gender'].map({'male': 0, 'female': 1})
# print(data['gender'])

"# Step 3: Split into features and target"
X = data[['pclass', 'gender', 'age']]
# print(X)
y = data['survived']

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 5: Train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 8: Print the decision tree as text
tree_rules = export_text(model, feature_names=list(X.columns))
print("\nDecision Tree Rules:\n")
print(tree_rules)
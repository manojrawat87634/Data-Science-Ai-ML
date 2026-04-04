import numpy as np

# Categories: Food, Travel, Shopping, Bills, Entertainment
categories = np.array(["Food", "Travel", "Shopping", "Bills", "Entertainment"])

# Example: Expenses for 7 days (rows = days, cols = categories)
expenses = np.array([
    [200, 50, 100, 300, 150],
    [180, 20, 50, 300, 100],
    [220, 0, 0, 300, 80],
    [150, 30, 200, 300, 120],
    [300, 60, 150, 300, 200],
    [250, 40, 100, 300, 180],
    [270, 20, 80, 300, 160]
])

# 1. Total spending
total_spent = np.sum(expenses)
print("Total Spending:", total_spent)

# 2. Spending per category
category_totals = np.sum(expenses, axis=0)
print("\nSpending by Category:")
for cat, val in zip(categories, category_totals):
    print(f"{cat}: {val}")

# 3. Highest spending category
max_index = np.argmax(category_totals)
print("\nHighest Spending Category:", categories[max_index])

# 4. Daily total expenses
daily_totals = np.sum(expenses, axis=1)
print("\nDaily Spending:", daily_totals)

# 5. Day with highest spending
max_day = np.argmax(daily_totals)
print("Highest Spending Day: Day", max_day + 1)

# 6. Average daily spending
avg_daily = np.mean(daily_totals)
print("Average Daily Spending:", avg_daily)

# 7. Detect high spending days (> average)
high_spending_days = np.where(daily_totals > avg_daily)[0] + 1
print("High Spending Days:", high_spending_days)

# 8. Percentage spent per category
percentages = (category_totals / total_spent) * 100
print("\nCategory Percentages:")
for cat, pct in zip(categories, percentages):
    print(f"{cat}: {pct:.2f}%")
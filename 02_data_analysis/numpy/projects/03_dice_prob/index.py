import numpy as np

# Number of simulations
n = 100000

# Simulate rolling two dice
dice1 = np.random.randint(1, 7, n)
dice2 = np.random.randint(1, 7, n)

# Sum of both dice
sums = dice1 + dice2

# 1. Probability of getting sum = 7
prob_7 = np.mean(sums == 7)
print("Probability of sum = 7:", prob_7)

# 2. Count frequency of each sum (2 to 12)
values, counts = np.unique(sums, return_counts=True)

print("\nSum Frequencies:")
for v, c in zip(values, counts):
    print(f"Sum {v}: {c}")

# 3. Convert counts to probabilities
probabilities = counts / n

print("\nProbabilities:")
for v, p in zip(values, probabilities):
    print(f"Sum {v}: {p:.4f}")

# 4. Simulate a simple game
# Rule: win ₹10 if sum = 7, lose ₹5 otherwise
wins = (sums == 7)

profit = np.where(wins, 10, -5)

total_profit = np.sum(profit)
avg_profit = np.mean(profit)

print("\nTotal Profit:", total_profit)
print("Average Profit per Game:", avg_profit)
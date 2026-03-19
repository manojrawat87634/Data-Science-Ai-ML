import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ASIANPAINT.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')

# Plot Closing Price
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'], label='Close Price')

plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()

plt.show()
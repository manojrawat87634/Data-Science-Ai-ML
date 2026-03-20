import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 50, 60, 70, 80]

plt.hist(marks, bins=5, color='blue')

plt.title("Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

plt.show()
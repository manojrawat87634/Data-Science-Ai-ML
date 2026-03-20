import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
students = [120, 90, 60, 150]

plt.pie(students, labels=labels, autopct='%1.1f%%')

plt.title("Students Distribution by Course")

plt.show()
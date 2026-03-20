import matplotlib.pyplot as plt

# Categories and values
courses = ["Python", "Java", "C++", "JavaScript"]
students = [120, 90, 60, 150]

# Create bar chart
plt.bar(courses, students)

# Labels
plt.title("Students per Course")
plt.xlabel("Courses")
plt.ylabel("Number of Students")

# Show graph
plt.show()
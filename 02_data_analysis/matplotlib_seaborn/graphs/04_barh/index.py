import matplotlib.pyplot as plt

# Categories and values
courses = ["Python", "Java", "C++", "JavaScript", "Web Development Using Javascript"]
students = [120, 90, 60, 150, 43]

# Create bar chart
plt.barh(courses, students)

# Labels
plt.title("Students per Course")
plt.xlabel("Courses")
plt.ylabel("Number of Students")

# Show graph
plt.show()
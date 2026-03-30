students = [  {'name': "Rahul","marks" :  78
}, {'name': "Anita","marks" :  92
}, {'name': "Karan","marks" :  85
}, {'name': "Neha","marks" :  88
}]

students.sort(key=lambda x: x.get("marks"))
print(students)
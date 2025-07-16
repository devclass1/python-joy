# Create a dictionary of student records
students = {
    'student1': {
        'name': 'Amit Roy',
        'age': 15,
        'class': '10A'
    },
    'student2': {
        'name': 'Sumon Cahtterjee',
        'age': 16,
        'class': '11B'
    },
    'student3': {
        'name': 'Selim Khan',
        'age': 14,
        'class': '9C'
    },
    'student4': {
        'name': 'Josef Matt',
        'age': 17,
        'class': '12A'
    },
    'student5': {
        'name': 'Sinu Selvum',
        'age': 15,
        'class': '10B'
    }
}

# Print the table header
print("\nStudent Records")
print("-" * 40)
print(f"{'No.':<5} {'Name':<20} {'Age':<5} {'Class':<5}")
print("-" * 40)

# Print each student's information in table format
for i, (key, student) in enumerate(students.items(), 1):
    print(f"{i:<5} {student['name']:<20} {student['age']:<5} {student['class']:<5}")

print("-" * 40)

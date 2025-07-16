# Initialize an empty dictionary to store student records
students = {}

# Number of students to input
num_students = 5

print("Enter details for 5 students:")

# Get input for each student
for i in range(1, num_students + 1):
    print(f"\nStudent {i}:")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    class_ = input("Enter student class: ")
    
    # Add to dictionary with student ID as key
    students[f'student{i}'] = {
        'name': name,
        'age': age,
        'class': class_
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

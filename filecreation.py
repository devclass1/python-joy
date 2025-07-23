# Get input from user
user_string = input("Enter the string you want to write to the file: ")
filename = input("Enter the name of the file to write to (e.g., 'output.txt'): ")

# Write to file
try:
    with open(filename, 'w') as file:
        file.write(user_string)
    print(f"Successfully wrote to '{filename}'")
except:
    print("Error writing to file")
